import requests
import json

from requests.models import Response

res = requests.get("http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")

for data in res.json()["items"]:
    print(data["title"])