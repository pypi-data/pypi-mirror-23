from flask import Flask
from flask import request
from flask_api import status
from flask_cors import CORS, cross_origin
import os
import json
import requests
import StringIO
import codecs
from engine import Engine
from elasticsearch_mapping.generate import generate_from_project_config
from elasticsearch_indexing.index_knowledge_graph import index_knowledge_graph_fields
from urllib import unquote
from urlparse import urlparse

app = Flask(__name__)
CORS(app, supports_credentials=True)
engine = None
default_project_url = None
default_es_endpoint = None
current_project = "static"

_location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def load_project_json_file(file_name):
    file = json.load(codecs.open(os.path.join(_location__, file_name),
                                  'r', 'utf-8'))
    return file

def get_engine():
    global engine
    if engine:
        return engine
    else:
        import sys
        c = load_json_file(sys.argv[11])
        engine = Engine(c)
        set_engine(engine)
        return engine

def get_default_es_endpoint():
    global engine
    global default_es_endpoint
    if default_es_endpoint:
        return default_es_endpoint
    if engine:
        execute_component = get_engine().config["coarse"]["execute"]["components"][0]
        if "endpoints" in execute_component:
            default_es_endpoint = execute_component["endpoints"]
        if "host" in execute_component and "port" in execute_component:
            default_es_endpoint = ["{}:{}".format(execute_component["host"], execute_component["port"])]
    return default_es_endpoint

@app.route("/")
def hello():
    return "DIG Sandpaper\n"

def post_url(url, data):
    url = unquote(url)
    parsed_url = urlparse(url)
    # for some reason requests is ignoring usernames and passwords in urls
    if parsed_url.username:
        response = requests.post(url, auth=(parsed_url.username, parsed_url.password), data=data)
    else:
        response = requests.post(url, data=data)
    return response

def put_url(url, data):
    url = unquote(url)
    parsed_url = urlparse(url)
    # for some reason requests is ignoring usernames and passwords in urls
    if parsed_url.username:
        response = requests.put(url, auth=(parsed_url.username, parsed_url.password), data=data)
    else:
        response = requests.put(url, data=data)
    return response

def get_url(url):
    url = unquote(url)
    parsed_url = urlparse(url)
    # for some reason requests is ignoring usernames and passwords in urls
    if parsed_url.username:
        response = requests.get(url, auth=(parsed_url.username, parsed_url.password))
    else:
        response = requests.get(url)
    return response

def get_project_config(url, project):
    if url and project:
        response = get_url('{}/projects/{}'.format(url, project))
    elif url and not project:
        response = get_url(url)
    elif not url and project:
        response = get_url('{}/projects/{}'.format(default_project_url, project))
    else:
        return "Please provide either a url and/or a project as url params to retrieve fields to generate an elasticserach mapping\n", status.HTTP_400_BAD_REQUEST

    project_config = response.json()
    return project_config

def call_generate_mapping(url, project, project_config=None):
    if not project_config:
        project_config = get_project_config(url, project)
    return generate_from_project_config(project_config)

@app.route("/mapping/generate", methods=['GET'])
def generate_mapping():
    url = request.args.get('url', None)
    project = request.args.get('project', None)
    m = call_generate_mapping(url, project)
    return json.dumps(m)

@app.route("/mapping", methods=['PUT','POST'])
def add_mapping():
    url = request.args.get('url', None)
    project = request.args.get('project', None)
    project_config = get_project_config(url, project)
    m = call_generate_mapping(url, project, project_config)
    index = request.args.get('index', project_config["index"]["full"])
    endpoint = request.args.get('endpoint', get_default_es_endpoint())
    if not isinstance(endpoint, basestring):
        endpoint = endpoint[0]
    put_url('{}/{}'.format(endpoint, index),
            data=json.dumps(m))
    return "index {} added for project {}\n".format(index, project)

def jl_file_iterator(file):
    line = file.readline()
    while line :
        document = json.loads(line)
        yield document
        line = file.readline()


def _index_fields(request):
    if (request.headers['Content-Type'] == 'application/x-gzip'):
        gz_data_as_file = StringIO.StringIO(request.data)
        uncompressed = gzip.GzipFile(fileobj=gz_data_as_file, mode='rb')
        jls = uncompressed.read()
    elif (request.headers['Content-Type'] == 'application/json' or
          request.headers['Content-Type'] == 'application/x-jsonlines'):
        jls = request.data
    else:
        return "Only supported content types are application/x-gzip, application/json and application/x-jsonlines", status.HTTP_400_BAD_REQUEST
    reader = codecs.getreader('utf-8')
    jls_as_file = reader(StringIO.StringIO(jls))
    jls = [json.dumps(jl) for jl in [index_knowledge_graph_fields(jl) for jl in jl_file_iterator(jls_as_file)] if jl is not None]
    return jls

@app.route("/indexing/fields", methods=['POST'])
def index_fields():
    jls = _index_fields(request)
    indexed_jls = "\n".join(jls)
    if (request.headers['Content-Type'] == 'application/x-gzip'):
        indexed_jls_as_file = StringIO.StringIO()
        compressed = gzip.GzipFile(
            filename=FILENAME, mode='wb', fileobj=indexed_jls_as_file)
        compressed.write(indexed_jls)
        compressed.close()
        return indexed_jls_as_file.getvalue()
    else:
        return indexed_jls

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

@app.route("/indexing", methods=['POST'])
def index():
    endpoint = request.args.get('endpoint', get_default_es_endpoint())
    if not isinstance(endpoint, basestring):
        endpoint = endpoint[0]
    index = request.args.get('index', None)
    t = request.args.get('type', "ads")
    jls = _index_fields(request)
    log_requests =  get_engine().config.get("indexing",{}).get("log_requests", None)
    if log_requests:
        with open(os.path.join(log_requests, "indexing.{}.jl".format(index)), "a") as myfile:
            for jl in jls:
                myfile.write(jl)
    url = "{}/{}/{}/_bulk".format(endpoint, index, t)
    counter = 0
    after_filtering = len(jls)
    failed = 0
    succeeded = 0
    # this is inefficent
    for chunk in chunker(jls, 100):
        bulk_request = ""
        bulk_request_format = '{"index":{}}\n'
        for c in chunk:
            doc_id = json.loads(c).get("doc_id", None)
            if doc_id:
                doc_request = '{"index":{"_id":"' + doc_id + '"}}\n' + c + '\n'
            else:
                doc_request = bulk_request_format + c + '\n'
            bulk_request = bulk_request + doc_request
        counter += len(chunk)
        r = post_url(url, bulk_request)
        bulk_response = r.json()
        for doc_response in bulk_response.get("items", []):
            index_response = doc_response.get("index", {})
            failed = index_response.get("shards", {}).get("failed", 0)
            succeeded = index_response.get("shards", {}).get("succeeded", 0)
        log_responses =  get_engine().config.get("indexing",{}).get("log_responses", None)
        if log_responses:
            with open(os.path.join(log_responses, "indexing.{}.responses.jl".format(index)), "a") as myfile:
                myfile.write(json.dumps(bulk_response))

    return "Posted {} documents. {} succeeded. {} 0 failed.\n".format(counter, succeeded, failed)

@app.route("/search", methods=['POST'])
def search():
    query = json.loads(request.data)
    (qs, rs) = get_engine().execute_coarse(query)
    answers = get_engine().execute_fine(qs, rs)
    return json.dumps(answers)


def coarse_results_to_dict(r):
    if isinstance(r, list):
        return [rr.to_dict() for rr in r]
    else:
        return r.to_dict()


@app.route("/search/coarse", methods=['POST'])
def coarse():
    query = json.loads(request.data)
    log_requests =  get_engine().config.get("coarse",{}).get("log_requests", None)
    if log_requests:
        with open(os.path.join(log_requests, "coarse.{}.jl".format(current_project)), "a") as myfile:
            myfile.write(json.dumps(query))
    (qs, rs) = get_engine().execute_coarse(query)
    qs_with_rs = [{"query": q, "result": coarse_results_to_dict(r)} for q, r in zip(qs, rs)]
    return json.dumps(qs_with_rs)

@app.route("/search/coarse/generate", methods=['POST'])
def coarse_generate():
    query = json.loads(request.data)
    qs = get_engine().generate_coarse(query)
    return json.dumps(qs)



@app.route("/search/fine", methods=['POST'])
def fine():
    return "Hello World!\n"

def set_engine(e):
    global engine
    engine = e

def set_default_project_url(d):
    global default_project_url
    default_project_url = d

def set_default_es_endpoint(d):
    global default_es_endpoint
    default_es_endpoint = d


@app.route("/config", methods=['POST'])
def config():
    url = request.args.get('url', None)
    project = request.args.get('project', None)
    global current_project
    current_project = project
    project_config = get_project_config(url, project)
    endpoint = request.args.get('endpoint', get_default_es_endpoint())
    index = request.args.get('index', project_config["index"]["full"])
    if not request.data:
        default_c = load_project_json_file("default_config.json")
    else:
        default_c = json.loads(request.data)
    c = default_c
    execute_component = c["coarse"]["execute"]["components"][0]
    execute_component.pop("host", None)
    execute_component.pop("port", None)
    if isinstance(endpoint, basestring):
        endpoints = list()
        endpoints.append(unquote(endpoint))
    else:
        endpoints = endpoint
    execute_component["endpoints"] = endpoints
    generate_components = c["coarse"]["generate"]["components"]
    preprocess_components = c["coarse"]["preprocess"]["components"]
    predicate_type_mapping = {}
    type_field_mapping = {}
    type_group_field_mapping = {}
    field_weight_mapping = {}
    methods=["extract_from_landmark", "other_method"]
    segments=["title", "content_strict", "other_segment"]
    for gc in generate_components:
        if gc["name"] == "TypeIndexMapping":
            gc["type_index_mappings"]["Ad"] = index
        if gc["name"] == "TypeFieldGroupByMapping":
            type_group_field_mapping = gc["type_field_mappings"]
        if gc["name"] == "TypeFieldMapping":
            type_field_mapping = gc["type_field_mappings"]
        if gc["name"] == "FieldWeightMapping":
            field_weight_mapping = gc["field_weight_mappings"]
    for pc in preprocess_components:
        if pc["name"] == "PredicateDictConstraintTypeMapper":
           predicate_type_mapping = pc["predicate_range_mappings"]
        
    for field_name, spec in project_config["fields"].iteritems():
        predicate_type_mapping[field_name] = field_name.lower()
        type_group_field_mapping[field_name] = "indexed.{}.high_confidence_keys".format(field_name)
        fields = list()
        if "email" not in field_name and "website" not in field_name and "tld" not in field_name:
            fields.extend(type_field_mapping["owl:Thing"])
        for method in methods:
            for segment in segments:
                fields.append("indexed.{}.{}.{}.value".format(field_name, method, segment))
                if "email" in field_name:
                    fields.append("indexed.{}.{}.{}.key".format(field_name, method, segment))
        type_field_mapping[field_name] = fields
    
    #add field weight mapping

    set_engine(Engine(c))
    return "Applied config for project {}\n".format(project)


def load_json_file(file_name):
    rules = json.load(codecs.open(file_name, 'r', 'utf-8'))
    return rules
