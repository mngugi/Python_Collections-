# a python program the prints  nested lists of twoWheels, fourWheels and sixWheels Vehicles


twoWheels = ['Honda', 'Kawasaki', 'Yamaha']
fourWheels = ['Toyota', 'Nissan','Ford']
sixWheels = ['Isuzu','Scania','Actross']

# Nested all the three lists of Automobiles

nestedAutoMobiles = [['Honda', 'Kawasaki', 'Yamaha'],['Toyota', 'Nissan','Ford'],['Isuzu','Scania','Actross'] ]
nestedAutoMobiles[0].append('TVS')
nestedAutoMobiles[1].append('Peugot')
nestedAutoMobiles[2].append('Mitsubishi-Fuso')

print(nestedAutoMobiles[0])
print (len(nestedAutoMobiles[1]))

#twoWheels.append(['TVS'])
nestedAutoMobiles.append(['tenWheelers'])

print ('---------')
for i in twoWheels:
    print(i)

print('-----------')

for j in nestedAutoMobiles:
    print(j)


info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }


print(info)

color = info['personal_data']['physical_features']['color']
print('Here is color elemets:', color)

    
    


