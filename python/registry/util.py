import requests
import json
from json import load

def upload_schema(schema_name):
    url = "http://localhost:18080/api/artifacts"
    with open("avro/test1.avsc") as f:
        data = json.load(f)
    headers = {"Content-type": "application/json", "X-Registry-ArtifactId": schema_name}
    kwargs = {"headers": headers, "json": data}

    requests.post(url, **kwargs)

def retrive_schema(schema_name):
    return requests.get(f"http://localhost:18080/api/artifacts/{schema_name}").text
