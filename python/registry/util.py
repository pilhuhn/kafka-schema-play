import requests
import json
from json import load


def upload_schema(schema_name, update=False):
    url = "http://localhost:18080/api/artifacts"
    if update:
        url = url + "/" + schema_name + "/versions"
    with open("avro/test1.avsc") as f:
        data = json.load(f)
    headers = {"Content-type": "application/json", "X-Registry-ArtifactId": schema_name}
    kwargs = {"headers": headers, "json": data}

    requests.post(url, **kwargs)


def retrieve_schema(schema_name):
    return requests.get(f"http://localhost:18080/api/artifacts/{schema_name}").text
