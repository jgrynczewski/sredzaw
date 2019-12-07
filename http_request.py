import requests
import json

response = requests.get("https://api.punkapi.com/v2/beers?name=Buuz")
# print(response.json())
response_json  = response.json()
#print(raw_response_json)
print(response_json[0]['name'])