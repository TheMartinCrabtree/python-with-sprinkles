import json


# reading json
jsonObj = '{"name": "John", "age": 30}'
parsedJsonObj = json.loads(jsonObj)
print(parsedJsonObj["name"])

# writing json
pythonObj = { "name": "Dave", "age": 33}
convJson = json.dumps(pythonObj)
print(convJson)