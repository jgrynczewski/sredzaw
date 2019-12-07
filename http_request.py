import requests

response = requests.get("https://api.punkapi.com/v2/beers?beer_name=Buzz")
response_json = response.json()

print(response_json[0]['name'])