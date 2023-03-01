# python program that gets data from Apples iTunes

import json

aString = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(aString)
d = json.loads(aString)
print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])


def objects(obj):
    return json.dumps(obj,sort_keys=True, indent=2)
j =  {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}
print(j)
print(objects(j))