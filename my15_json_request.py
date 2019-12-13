import requests
import json

response = requests.get("https://api.punkapi.com/v2/beers/?ips=27")
response_json = response.json()

print(response_json[0]['name'])