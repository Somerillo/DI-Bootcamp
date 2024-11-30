import json
import requests
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

response = requests.get('https://api.chucknorris.io/jokes/random')
print(response.text)

data = json.loads(response.text)
print(data)

#200 = ok
#400 = bad request
#404 = not found

with open(dir_path + 'chuck_norris_jokes.json', 'a+') as file:
    json.dump(data, file, indent=2, sort_keys=True)
