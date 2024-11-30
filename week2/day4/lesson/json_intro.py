import json

#we convert a python dict into a json file
my_family = {
    "parents":['Beth', 'Jerry'],
    "children":['Summer', 'Morty']
}

json_file = 'family.json'

with open('family.json', 'w') as f:
    json.dump(my_family, f) #dump(name python dict, file object)

#from python dict to a json string
json_my_family = json.dumps(my_family)
print(json_my_family)

#we convert a json file into a python dict
with open('family.json', 'r') as f:
    my_family = json.load(f)
    # print(my_family)

#load a JSON string into a python dict:
parsed_family = json.loads(json_my_family)
print('python dict after loads():', parsed_family)

#JSON strings:

