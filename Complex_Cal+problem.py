
import numpy as np
import array as arr

# create an array of 5 integers using a function arr1()
print("================================")
def arr1():
    array1 = arr.array('i', [4,6,7,9,8] )
    row = ''
    for n in array1:
        row += str(n) + ' '
        print('row',arr1() )




#print("\nArray2\n")

def arr2():
    array2 = arr.array('i', [2,3,4,5,4] )
    row = ''
    for n in array2:
        row += str(n) + ' '
    print(row)

arr2()
print ("---------------------------------------------------- ")
print("\n Mathematical Operations using functions()")
# Add 4 to each element of the array
print ("\nAddition operator +4: \n")
def add_4(array1, array2):
    updated_array1 = [x + 4 for x in array1]
    updated_array2 = [x + 4 for x in array2]
    row1 = ''
    row2 = ''
    for n in updated_array1:
        row1 += str(n) + ' '
    for n in updated_array2:
        row2 += str(n) + ' '
    print(row1 + '\n' + row2)

array1 = arr.array('i', [4, 6, 7, 9, 8])
array2 = arr.array('i', [2, 3, 4, 5, 4])

add_4(array1, array2)
print ("---------------------------------------------------- ")
# Subtract 4 to each element of the array
print ("\nSubtract operator -4: \n")
def add_4(array1, array2):
    updated_array1 = [x - 4 for x in array1]
    updated_array2 = [x - 4 for x in array2]
    row1 = ''
    row2 = ''
    for n in updated_array1:
        row1 += str(n) + ' '
    for n in updated_array2:
        row2 += str(n) + ' '
    print(row1 + '\n' + row2)

array1 = arr.array('i', [4, 6, 7, 9, 8])
array2 = arr.array('i', [2, 3, 4, 5, 4])

add_4(array1, array2)
print ("---------------------------------------------------- ")
# multiply by 4 to each element of the array
print ("\nMultiplication operator x4: \n")
def add_4(array1, array2):
    updated_array1 = [x * 4 for x in array1]
    updated_array2 = [x * 4 for x in array2]
    row1 = ''
    row2 = ''
    for n in updated_array1:
        row1 += str(n) + ' '
    for n in updated_array2:
        row2 += str(n) + ' '
    print(row1 + '\n' + row2)

array1 = arr.array('i', [4, 6, 7, 9, 8])
array2 = arr.array('i', [2, 3, 4, 5, 4])

add_4(array1, array2)
print ("---------------------------------------------------- ")
# Divide by 4 to each element of the array
print ("\nDivision operator -4: \n")
def add_4(array1, array2):
    updated_array1 = [x / 4 for x in array1]
    updated_array2 = [x / 4 for x in array2]
    row1 = ''
    row2 = ''
    for n in updated_array1:
        row1 += str(n) + ' '
    for n in updated_array2:
        row2 += str(n) + ' '
    print(row1 + '\n' + row2)

array1 = arr.array('i', [4, 6, 7, 9, 8])
array2 = arr.array('i', [2, 3, 4, 5, 4])

add_4(array1, array2)
print ("---------------------------------------------------- ")
# Modulus 4 to each element of the array
print ("\nModule operator -4: \n")
def add_4(array1, array2):
    updated_array1 = [x - 4 for x in array1]
    updated_array2 = [x - 4 for x in array2]
    row1 = ''
    row2 = ''
    for n in updated_array1:
        row1 += str(n) + ' '
    for n in updated_array2:
        row2 += str(n) + ' '
    print(row1 + '\n' + row2)

array1 = arr.array('i', [4, 6, 7, 9, 8])
array2 = arr.array('i', [2, 3, 4, 5, 4])

add_4(array1, array2)
print ("---------------------------------------------------- ")
# Sum the arrays to each element of the array
print (" Add the 2 arrays: \n")
def add_arrays(array1, array2):
    sum_array = [x + y for x, y in zip(array1, array2)]
    row = ''
    for n in sum_array:
        row += str(n) + ' '
    print(row)

array1 = arr.array('i', [4, 6, 7, 9, 8])
array2 = arr.array('i', [2, 3, 4, 5, 4])

add_arrays(array1, array2)
print ("---------------------------------------------------- ")
#Division of the arrays to each element of the array
print (" Divide the 2 arrays: \n")
def add_arrays(array1, array2):
    sum_array = [x / y for x, y in zip(array1, array2)]
    row = ''
    for n in sum_array:
        row += str(n) + ' '
    print(row)

array1 = arr.array('i', [4, 6, 7, 9, 8])
array2 = arr.array('i', [2, 3, 4, 5, 4])

add_arrays(array1, array2)
print ("---------------------------------------------------- ")
# Modulus the arrays to each element of the array
print (" Modulus of the 2 arrays: \n")
def add_arrays(array1, array2):
    sum_array = [x + y for x, y in zip(array1, array2)]
    row = ''
    for n in sum_array:
        row += str(n) + ' '
    print(row)

array1 = arr.array('i', [4, 6, 7, 9, 8])
array2 = arr.array('i', [2, 3, 4, 5, 4])

add_arrays(array1, array2)

print ("---------------------------------------------------- ")
print ("Arithmetic operations using sine and square root: ")

import array
import numpy as np

def sine_arrays(array1, array2):
    sum_array = np.array([x + y for x, y in zip(array1, array2)])
    sine_array = np.sin(np.sqrt(sum_array))
    row = ''
    for n in sine_array:
        row += str(n) + ' '
    print(row)

array1 = array.array('i', [4, 6, 7, 9, 8])
array2 = array.array('i', [2, 3, 4, 5, 4])

sine_arrays(array1, array2)
print ("---------------------------------------------------- ")
print (" Multidimentional operations: ")

def arr1():
    array1 = np.array([4,6,7,9,8], dtype=int)
    array1 = np.arange(0,8).reshape(2,4)
    row = ''
    for n in array1:
        row += str(n) + ' '
    print(row)

arr1()


print("\nArray2\n")

def arr2():
    array2 = np.array([2,3,4,5,4], dtype=int)
    array2 = np.arange(0,8).reshape(2,4)
    row = ''
    for n in array2:
        row += str(n) + ' '
    print(row)

arr2()

print ("---------------------------------------------------- ")


print ("Multidimentional array multiplied by ones: ")

def arr1():
    array1 = np.array([4,6,7,9,8], dtype=int)
    array1 = np.ones((2,4))
    return array1

def arr2():
    array2 = np.array([2,3,4,5,4], dtype=int)
    array2 = np.ones((2,4))
    return array2

array1 = arr1()
array2 = arr2()
result = array1 * array2
print(result)


def arr1():
    array1 = np.array([4,6,7,9,8], dtype=int)
    array1 = np.ones((2,4))
    row = ''
    for n in array1:
        row += str(n) + ' '
    print(row)

arr1()


print("\nArray2\n")

def arr2():
    array2 = np.array([2,3,4,5,4], dtype=int)
    array2 = np.ones((2,4))
    row = ''
    for n in array2:
        row += str(n) + ' '
    print(row)

arr2()

