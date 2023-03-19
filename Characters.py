import re

charcter = 'moussasosa'
splitChar = charcter.split('ous')
print('split ous from moussasos ')
print(splitChar)
print('join ous from moussasos ')
print('-----------------------')
joinChar = 'ous'.join(splitChar)
print(joinChar)
j = re.findall(r'[aeiou]', charcter)
i = re.findall(r'[^aeiou]', charcter)
print(j)
print(i)