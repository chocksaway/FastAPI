import requests
import json

url = "http://127.0.0.1:8000/stream"
with requests.get(url, stream=True) as resp:
    resp.raise_for_status()
    for line in resp.iter_lines(decode_unicode=True):
        if not line:
            continue
        obj = json.loads(line)
        print("Received:", obj)