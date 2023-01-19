import numpy as np
xarr= np.arange(0,9).reshape(3,3)
print (xarr)
yarr= np.ones((3,3))
print(yarr)
print(" ")

print(" ")
print("Matrx Product")
xy = np.dot(xarr,yarr)
print(xy)

print(" ")
print("Matrx Product using xarr.dot(yarr)")
xyi = xarr.dot(yarr)
print(xyi)

