#splitting is, to divide an array into several parts
# a set of functions that work both horizontally with the hsplit() function and vertically with the vsplit() function.

import numpy as np
Arr = np.arange(12).reshape((3, 4))
Arr1 = np.arange(16).reshape((4, 4))
Arr2 = np.arange(10).reshape((2, 5))
print(Arr)

print(" ")
print("Horizontal split")
[B,C]=np.hsplit(Arr,2)
print(B)
print("")
print(C)

print(" ")
print("Vertical split")
[D,E]=np.vsplit(Arr1,2)
print(D)
print("")
print(E)

'''
A more complex command is the split() function, which allows you to split the array into
nonsymmetrical parts. In addition, passing the array as an argument, you have also to specify the indexes
of the parts to be divided. If you use the option axis = 1, then the indexes will be those of the columns; if
instead the option is axis = 0, then they will be the row indexes.
For example, if you want to divide the matrix into three parts, the first of which will include the first
column, the second will include the second and the third column, and the third will include the last column,
then you must specify three indexes in the following way.
'''
print("split() function which splits the array into nonsymmetrical parts")

[Arr,Arr1,Arr2]=np.split(Arr,[1,3],axis=1)
print(Arr)
print(" ")
print(Arr1)
print(" ")
print(Arr2)


