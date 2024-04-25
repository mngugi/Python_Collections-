import numpy as np
import time

def xarr():
    arry = np.arange(0,9).reshape(3,3)
    print ("\nThe matrix is\n",arry)
    return arry

print("The matrix:\n", xarr())

def yarr():
    yarr = np.ones((3,3))
    print (yarr)
    return yarr

print("\nThe matrix:\n", yarr())


print("\nMatrx Product\n")
xy = np.dot(xarr(),yarr())
print(xy)

print("\nMatrx Product using xarr.dot(yarr) Functions\n")
xyi = xarr().dot(yarr())
print(xyi)

