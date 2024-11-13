import json
import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
# data = json.load(response.txt)
print(response.text)

data = json.loads(response.text)
print(data)

with open("chuck_norris_jokesssssss.json", "a+") as file:
    json.dump(data, file, indent=2, sort_keys=True)