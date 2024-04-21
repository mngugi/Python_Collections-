import array as arr

# create an array of 5 integers using a function arr1()
def arr1():
    array1 = arr.array('i', [4, 6, 7, 9, 8])
    row = ''
    for n in array1:
        row += str(n) + ' '
    return array1

print("================================")
print('row', arr1())

