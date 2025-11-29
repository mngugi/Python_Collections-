import xml.etree.ElementTree as ET

data = '''<person>
<name>Maradonna</name>
<phone type="intl">
+254303030
</phone>
<email hide="yes"></email>
</person>'''

tree = ET.fromstring(data)

print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
print('--------------------------------------')

input = ''' <stuff>
<users>
<user x = "2">
<id>001</id>
<name>Messi</name>
</user>
<user x = "7">
<id>0011</id>
<name>Wanchop</name>
</user>

</users>
</stuff>
'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User Count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('id', item.find('id').text)
    print('Attribute', item.get('x'))