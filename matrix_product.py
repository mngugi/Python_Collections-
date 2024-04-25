import numpy as np

def xarr():
    arry = np.arange(0,9).reshape(3,3)
    print (arry)
    return arry

print("The matrix:", xarr())

def yarr():
    yarr = np.ones((3,3))
    
    print (yarr)
    return yarr

print("The matrix:", yarr())


print("\nMatrx Product")
xy = np.dot(xarr(),yarr())
print(xy)

print(" ")
print("Matrx Product using xarr.dot(yarr) Functions")
xyi = xarr().dot(yarr())
print(xyi)

