items = [5,6,8,9,10,12,15,]
multiply_By_two = [value * 2 for value in items]
multiply_By_two_two = map(lambda value: value * 10, items)
print(multiply_By_two)
print(multiply_By_two_two)
print(list(multiply_By_two_two))

print('---------------------------------------------------')

def keep_events(items2):
    moduloList = [item for item in items2 if item % 2 == 0]
    return moduloList
print(keep_events([0,2,3,6,18,8,90,120,12,4,8,9,7]))

print('-------------------------------------------------')


import json

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},
                   {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'},
                   {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'},
                   {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'},
                   {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'},
                   {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

inner_list = tester['info']

compri = [d['name'] for d in inner_list]
print(compri)
