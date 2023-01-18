'''
 vertical stacking
with the vstack() function, which combines the second array as new rows of the first array. In this case you
have a growth of the array in the vertical direction. By contrast, the hstack() function performs horizontal
stacking; that is, the second array is added to the columns of the first array.

'''

import numpy as np
arr1= np.arange(5)
arr2= np.ones(5)
arr3= np.zeros(5)
print("Arrays ")
print(arr1,arr2,arr3)

print("this is vertical stacking")
a= np.vstack((arr1,arr2,arr3))
print(a)

print(" ")
print("this is horizontal stacking")
b= np.hstack((arr1,arr2,arr3))
print(b)

print(" ")
print("this is row stacking")
c= np.row_stack((arr1,arr2,arr3))
print(c)

print(" ")
print("this is column stacking")
d= np.column_stack((arr1,arr2,arr3))
print(d)
