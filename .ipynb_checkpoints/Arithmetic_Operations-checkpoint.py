'''
---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    custom_cell_magics: kql
    text_representation:
      extension: .py
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.2
  kernelspec:
    display_name: .venv
    language: python
    name: python3
---
'''
import numpy as np
import pyfiglet # type: ignore

def display_title(title):
    ascii_art = pyfiglet.figlet_format(title)
    print(ascii_art)

if __name__ == "__main__":
    display_title("Arithmetic Operations")
# create an array of 5 integers
arr = np.arange(5)
print("array1", arr)
arr2 = np.arange(5,10)
print ("array2 ",arr2)
print(" ")
print ("Addition operator: ")
a = arr+4
print(a)

print(" ")
print ("Subtraction operator: ")
s = arr-4
print(s)

print(" ")
print ("Multiplication operator: ")
m = arr+4
print(m)

print(" ")
print ("Division operator: ")
d = arr/2
print(d)

print(" ")
print ("Modulus operator: ")
md = arr%4
print(md)

print(" ")
print (" ================================ ")
print ("Arithmetic operations using multidimensional arrays: ")
print(" ")
print("Addition operator")
ai = arr+arr2
print(ai)

print(" ")
print("Subtraction operator")
ai = arr-arr2
print(ai)

print(" ")
print ("Multiplication operator: ")
mi = arr+arr2
print(mi)

print(" ")
print ("Division operator: ")
di = arr/arr2
print(d)

print(" ")
print ("Modulus operator: ")
mdi = arr%arr2
print(mdi)

print(" ")
print (" ================================ ")
print ("Arithmetic operations using sine and square root: ")

print(" ")
print ("sine operator: ")
sinarr = np.sin(arr)
print(sinarr)

print(" ")
print ("square root operator: ")
sqrtarr = np.sqrt(arr)
print(sqrtarr)

print(" ")
print (" ================================ ")
print (" Multidimentional operations: ")

Arr= np.arange(0,8).reshape(2,4)
print(Arr)

print(" ")
print ("Multidimentional array multiplied by ones: ")
Arr2= np.ones((2,4))
print(Arr2)

print(" ")
C= Arr2 * Arr
print(C)





















