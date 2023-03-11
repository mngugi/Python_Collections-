original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_version = original[:]
copied_outer_list = []

for inner_list in original:
    copied_outer_list = []
    for item in inner_list:
        copied_outer_list.append(item)
    copied_outer_list.append(copied_outer_list)
print("-------- Now look at the copied version -----------")
print(copied_outer_list)
original[0].append("k-nines")


print(copied_outer_list)

print("---------------- Old look at the copied version ------------------------")

print('Copied Version:',copied_version)
print('Copied version is original:',copied_version is original)
print('Copied version == original:',copied_version == original)
print( 'Append Canines in the original list')
original[0].append(['canines'])
print(original)

print(copied_version)
print('--------------------------------------------------------------=---------')
a = ''' Assuming that you don’t want to have aliased lists inside of your nested
 list, then you’ll need to perform nested iteration. '''
print(a)
print('------------------------------------------------------------------------')

