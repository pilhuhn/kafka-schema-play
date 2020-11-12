import avro.schema
import requests
import json
from json import load


def upload_schema(schema_name, file):
    url = "http://localhost:18080/api/artifacts"
    with open(file) as f:
        data = json.load(f)
    params = {"ifExists": "UPDATE"}
    headers = {"Content-type": "application/json", "X-Registry-ArtifactId": schema_name}
    kwargs = {"headers": headers, "json": data, "params": params}

    requests.post(url, **kwargs)

def retrieve_schema(schema_name, version=None):
    path = ""
    if version not in [None, "None"]:
        path = f"versions/{version}"

    schema_json = requests.get(f"http://localhost:18080/api/artifacts/{schema_name}/{path}").text
    return avro.schema.parse(schema_json)

def get_parsed_schema(schema):
    return avro.schema.parse(json.dumps(schema))
