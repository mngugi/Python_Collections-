# -*- coding: utf-8 -*-
"""
Spyder Editor
Author : Mwangi
Purpose : Simple program to append data types creating a lists

[]: This is the literal syntax for creating an empty list in Python.
empty = []: This assigns the empty list to the variable empty.
For example the expected outcome is :
1. Append an integer
-------------------
2. Append a float
-------------------
3. Append a double (float in Python)
-------------------
4. Append a string
-------------------
-------------------
[21, 50.0889, 2.0, 'Stingo', 'Stingo is a funny name!', ':0 , :))']
-------------------
"""
from typing import List, Union

# Define a list that can hold integers, floats, and strings
empty: List[Union[int, float, str]] = []

print("1. Append an integer")
print("-------------------")
empty.append(21)

print("2. Append a float")
print("-------------------")
empty.append(50.0889)

print("3. Append a double (float in Python)")
print("-------------------")
empty.append(2.0)

print("4. Append a string")
print("-------------------")
empty.append('Stingo')
print("-------------------")
empty.append("Stingo is a funny name!")
empty.append(":0 , :))")

print(empty)
print("-------------------")
