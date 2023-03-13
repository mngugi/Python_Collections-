import  requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page))

print(page.text[:150])
print(page.url)

print('--------------------------------')
x = page.json()
print(type(x))

print('-------------First Item ---------------')
print(x[0])

print('whole list printed')
print(json.dumps(x, indent=2))

print('-----------------------------------------------------------')
kval_pairs = {'rel_rhy': 'funny'}
page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched

