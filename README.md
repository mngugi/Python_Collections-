## hello.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor
Author : Mwangi
Purpose : Simple hello world function
programming starts at function modules
"""
def Hello():
    p = ("Hello World Coders")
    return p
    
# call the function hello()    
print("Call the phrase in the function:", Hello())
```

This code demonstrates how to define and call a function in Python.

A function is a block of code that performs a specific task and can be called by name. In Python, you can define a function using the `def` keyword, followed by the function name and a set of parentheses `()`. The code block inside the function is indented.

In this code, the function `Hello()` simply returns the string `"Hello World Coders"`. To call the function, you can use its name followed by parentheses `()`. When the function is called, the code inside the function will be executed and the returned value will be printed.

Functions can also take arguments, which are values that can be passed to the function when it is called. The arguments are placed inside the parentheses in the function definition, and can be used inside the function as variables.
Functions can also return a value using the return keyword. The returned value can be stored in a variable or used in an expression.
Overall, functions are a useful tool for organizing and reusing code in your programs.

---
## pythonkeywords.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor
Author : Mwangi
Purpose : a program to print pythons keywords 
"""
import keyword 
print('Python Keywords are:')
print (keyword.kwlist)
```
This code imports the keyword module and uses it to print a list of Python keywords.

The keyword module is a built-in module in Python that provides functions for testing whether a string is a keyword in Python. The `kwlist` attribute of the keyword module is a list of all the keywords in Python.

In this code, the import statement is used to import the keyword module, and the print function is used to print a message and the list of keywords stored in the `kwlist` attribute.

The output of this code will be a list of all the keywords in Python, such as `and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, while, and with.` These keywords are reserved words in Python and cannot be used as variable names or function names.

### Alternatively use a Function Method

```python

import keyword 
def keywords():
    j = keyword.kwlist
    return j    
 # Call the function    
print ("Python Keyword lists:", keywords())   

```
The code imports the keyword module, which provides a list of keywords for the Python programming language. Then, the keywords function is defined, which returns the list of keywords stored in the kwlist attribute of the keyword module. Finally, the function is called and the list of keywords is printed.

The output of the code will be a list of all the keywords in Python, like this: 

```
Python Keyword lists: ['and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'False', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'None', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'True', 'try', 'while', 'with', 'yield']

```

---


## mathOperators.py
**Code:**
```python 
# Basic level mathematics using python
# Author mwangi ngugi

# Addition examples 
print ( " ---- Addition a =  (1+2) and (ai = -1+2.5) ---- " )
a = 1 + 2
ai= -1 + 2.5
print('Answers',  a , ',' , ai)

#Subtraction examples 
print ( "---- Subtraction b=(31-2) and bi=( -9-9) ----" )
b = 31 - 2
bi = -9-9
print('Answers',  b, ',', bi)

#Multiplication examples
print ( "---- Multiply c=(4*20) and ci=( 2.5 * 6.5) ----" )
c = 4*20
ci = 2.5*6.5
print('Answers',  c, ',', ci)

#Division examples
print(" ---- Division  d = ( 9/2.5 ) and di = (0.75/0.5) ---- ")
d = ( 9/2.5 )
di = (0.75/0.5)
print('Answers', d , ',' , di)

#Floor Division examples
'''
The floor division operator divides the first number by the second
number and then rounds down the result to the next lowest integer. This
becomes interesting when one of the numbers is negative.
Reference Source : DOING MATH WITH PYTHON
USE PROGRAMMING TO EXPLORE ALGEBRA ,STATISTICS , CALCULUS , AND MORE! page 3
AMIT SAHA 
'''
print(" *** Floor Division  d = ( 9//2.5 ) and di = (0.75//0.5) ---- ")
e = ( 9//2.5 )
ei = (0.75//0.5)
print('Answers', e , ',' , ei)

# Remainder or Modulo (%) examples
print(" ---- Remainder  f = ( 7%3 ) and fi = (0.8%0.6) ---- ")
f = ( 7%3 )
fi = (0.8%0.6)
print('Aswers', f , ',' , fi)

# Exponential examples
print(" ---- Exponential   g = ( 5**4 ) and gi = ( 9 **(1/4)) ---- ")
g = 5**4 
gi = 9 **(1/4)
print('Answers', g , ',' , gi)

# Combinations PEDMAS or BODMAS
print ( " ---- Mathematical Combinations h = 5**2 + 4/2 - 10  and hi = 24+6 - (12 -3) + 24**2 / 10  ---- " )
h = 5**2 + 4/2 - 10 
hi = 24+6 - (12 -3) + 24**2 / 10
print('Answers', h , ',' , hi)             

print ( " *************** End ****************" )

```
This code performs a series of basic mathematical operations using Python.

The code first prints a message and then uses the `+` operator to perform addition. It stores the result in a variable a and then in `ai`. It then prints the results of these operations.

The code then uses the - operator to perform subtraction and stores the results in variables `b` and `bi`. It then prints the results of these operations.

The code then uses the `*` operator to perform multiplication and stores the results in variables `c` and `ci`. It then prints the results of these operations.

The code then uses the `/ `operator to perform division and stores the results in variables d and di. It then prints the results of these operations.

The code then uses the `//` operator to perform floor division and stores the results in variables `e` and `ei`. It then prints the results of these operations.

The code then uses the `%` operator to perform modulo (remainder) operations and stores the results in variables `f` and `fi`. It then prints the results of these operations.

The code then uses the `**` operator to perform exponential operations and stores the results in variables `g` and `gi`. It then prints the results of these operations.

Finally, the code performs some more complex mathematical operations that involve multiple operations and stores the results in variables h and hi. It then prints the results of these operations.

In Python, the order of operations follows the standard order of operations (PEDMAS or BODMAS). This means that exponentiation is performed before multiplication and division, which are performed before addition and subtraction. Parentheses can be used to specify the order of operations if needed.

**Using Functions**

```python
# reusing the same code but in python functions()
print ( " Addition a =  (1+2) and (ai = -1+2.5) " )

def Addition():
    a = 1+2
    ai = -1+2.5
    print("[Addition Answers: ", a , ",", ai)
Addition()

print ( " Subtraction b=(31-2) and bi=( -9-9) " )
#Subtraction examples 
def Subtraction():
    b = 31 - 2
    bi = -9-9
    print('[Subtraction Answers',  b, ',', bi)
Subtraction()

#Multiplication
print ( "Multiply c=(4*20) and ci=( 2.5 * 6.5)" )
def multiply():
    c = 4*20
    ci = 2.5*6.5
    print('[Multiplication Answers',  c, ',', ci)
multiply()

print("Floor Division  d = ( 9//2.5 ) and di = (0.75//0.5)")
#Floor Division examples
'''
The floor division operator divides the first number by the second
number and then rounds down the result to the next lowest integer. 
'''
def floor():
    e = ( 9//2.5 )
    ei = (0.75//0.5)
    print('[Floor Answers', e , ',' , ei)
floor()

# Remainder or Modulo (%) examples
print("Remainder  f = ( 7%3 ) and fi = (0.8%0.6) ")
def modulo():
    f = ( 7%3 )
    fi = (0.8%0.6)
    print('[Modulo Answers', f , ',' , fi)
modulo()

# Exponential examples
print("Exponential   g = ( 5**4 ) and gi = ( 9 **(1/4))")
def exponential():
    g = 5**4 
    gi = 9 **(1/4)
    print('[Exponential Answers', g , ',' , gi)
exponential()

# Combinations PEDMAS or BODMAS
print ( "Mathematical Combinations h = 5**2 + 4/2 - 10  and hi = 24+6 - (12 -3) + 24**2 / 10" )
def pedmas():
    h = 5**2 + 4/2 - 10 
    hi = 24+6 - (12 -3) + 24**2 / 10
    print('[PEDMAS or BODMAS Answers', h , ',' , hi,'\n')
pedmas()

print ( " *************** End ****************" )

```

The alternative code provided implements the basic mathematical operations such as addition, subtraction, multiplication, floor division, modulo, exponential, and combinations of these operations (PEDMAS or BODMAS). Each operation is defined as a function and can be called independently. When executed, the code will produce the following output:

```python

Addition a =  (1+2) and (ai = -1+2.5) 
[Addition Answers:  3 , 1.5
Subtraction b=(31-2) and bi=( -9-9) 
[Subtraction Answers 29 , -18
Multiply c=(4*20) and ci=( 2.5 * 6.5)
[Multiplication Answers 80 , 16.25
Floor Division  d = ( 9//2.5 ) and di = (0.75//0.5)
[Floor Answers 3.0 , 1.0
Remainder  f = ( 7%3 ) and fi = (0.8%0.6) 
[Modulo Answers 1 , 0.19999999999999973
Exponential   g = ( 5**4 ) and gi = ( 9 **(1/4))
[Exponential Answers 625 , 2.080083823051904
Mathematical Combinations h = 5**2 + 4/2 - 10  and hi = 24+6 - (12 -3) + 24**2 / 10
[PEDMAS or BODMAS Answers 11.0 , 212.8 

*************** End ****************

```

---

### Arithmetic_operations.py
**Code:**
```python

import numpy as np
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


```

**A complex version of this Code**
```Python

import numpy as np
import array as arr

# create an array of 5 integers using a function arr1()

def arr1():
    array1 = arr.array('i', [4,6,7,9,8] )
    row = ''
    for n in array1:
        row += str(n) + ' '
    print(row)

arr1()


print("\nArray2\n")

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


```

code creates two arrays of integers, array1 and array2, and performs various mathematical operations on them. The functions used to perform the operations all have the same name add_4, please chose a different name to avoid confusion. It would be better to have descriptive names for the functions that clearly indicate what they do, like add_four, subtract_four, multiply_by_four, divide_by_four, and modulus_four.

You also use a for loop to create a string representation of each array after the mathematical operations have been performed, but then you print the string representation, which is not the best way to display the arrays.

**Simple version of this code**

It's better to use the built-in print function to display the arrays, either directly or by converting them to a NumPy array first. For example:

```python

import numpy as np
import array as arr

def display_array(arr):
    print(np.array(arr))

def arr1():
    return arr.array('i', [4,6,7,9,8] )

def arr2():
    return arr.array('i', [2,3,4,5,4] )

def add_four(arr):
    return [x + 4 for x in arr]

def subtract_four(arr):
    return [x - 4 for x in arr]

def multiply_by_four(arr):
    return [x * 4 for x in arr]

def divide_by_four(arr):
    return [x / 4 for x in arr]

def modulus_four(arr):
    return [x % 4 for x in arr]

array1 = arr1()
array2 = arr2()

print("Array1:")
display_array(array1)

print("Array2:")
display_array(array2)

print("Add Four:")
display_array(add_four(array1))
display_array(add_four(array2))

print("Subtract Four:")
display_array(subtract_four(array1))
display_array(subtract_four(array2))

print("Multiply by Four:")
display_array(multiply_by_four(array1))
display_array(multiply_by_four(array2))

print("Divide by Four:")
display_array(divide_by_four(array1))
display_array(divide_by_four(array2))

print("Modulus Four:")
display_array(modulus_four(array1))
display_array(modulus_four(array2))

```

This code separates the creation of the arrays from the operations performed on them, which makes the code more readable and easier to understand. The use of descriptive function names and the display_array function make it clear what each operation does and what the resulting arrays look like.


---

### matrix_product.py
**Code:**

```python
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

```

---

### increment_decrement.py
**Code:**

```python

import numpy as np
import math
print ("Array of :")
arr = np.arange(5)
print(arr)

print(" ")
print("Increment by 1")
arr[0:5] +=1
print(arr)

print(" ")
print("Increment by 1")
arr[0:5] -=1
print(arr)


print(" ")
print("Increment by 5")
arr[0:5] +=5
print(arr)

print(" ")
print("Increment by multiplication of 1")
arr[0:5] *=5
print(arr)

```
---
### Median 

```Html
an algorithm to find the median of a given dataset:

    1. Arrange the dataset in ascending order.
    2. Check if the number of values in the dataset is odd or even:
        -If odd, the median is the middle value of the dataset.
        -If even, the median is the average of the two middle values of the dataset.
   3. Return the median as the output.


```
Here is the python code

```Python

from statistics import median
T=(15,5,1,7,4,10)
print(median(T)

def find_median(dataset):
    dataset_sorted = sorted(dataset)
    n = len(dataset_sorted)
    if n % 2 == 1:
        median = dataset_sorted[n//2]
    else:
        median = (dataset_sorted[n//2 - 1] + dataset_sorted[n//2])/2
    return median


```
The find_median() function takes a dataset as input, arranges it in ascending order using the sorted() function, checks if the number of values is odd or even using the modulus operator, and returns the median as output.


---

## tutology.py 
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor
Author : Mwangi
Purpose : a simple program to compute a simple truth and false 
"""

# print the OR logical operation 
print('-------or----------')
print (True or True)
print('-----------------')
print (True or False)
print('-----------------')
print (False or True)
print('-----------------')
print (False or False)
print('-----------------')
# print the ANd logical operation 
print('-------And----------')
print (True and True)
print('-----------------')
print (True and False)
print('-----------------')
print (False and True)
print('-----------------')
print (False and False)
print('-----------------')

```
This code is using the logical operators or and and to perform boolean operations. The `or `operator returns `True` if either of the operands is `True`, and `False` if both operands are `False`. The and operator returns `True` only if both operands are `True`, and `False` if either operand is `False`.

The code first prints the result of the or operator applied to various combinations of `True` and `False` operands. Then, it prints the result of the and operator applied to the same combinations of operands.

The output of this code will be:
```
-------or----------
True
True
True
False
-------And----------
True
False
False
False
```

---
### queston5.py
**Code**

```python
x = 5
y = 10

x= (x > 10 or y > 5)
y = not (x > 10 or y > 5)
z = (x and y)

print(z.__or__(y))

```

Here's how the code works step by step:

    x is assigned the value 5, and y is assigned the value 10.
    The expression x > 10 or y > 5 evaluates to False or True, which is True because at least one of the conditions is true (the second one).
    x is then assigned the value True because of the previous expression.
    The expression not (x > 10 or y > 5) is equivalent to not True, which evaluates to False.
    y is assigned the value False because of the previous expression.
    z is assigned the value False because x is True and y is False.
    z.__or__(y) is equivalent to False or False, which evaluates to False.


---


## in.py

**Code:**
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor
Author : Mwangi
Purpose : the 'in ' and 'is' are keywords in python :
    - in checks if a container contains a vlaue
    - is used to test object identity
"""
if 'a' in 'Pandas':
    print ("there are 2 a letters in the word pandas")
else :print (" Panda is a python data science package")

for i in 'Pandas':
    print (i, end="")
    
    print ('\r')
    
    print ("is",''is'') # if a letter value is found and correct print is True
```
This code demonstrates how to use the in and is keywords in Python.

The in keyword is used to check if a value is contained in a container, such as a list, tuple, or string. In the first example, the `in` keyword is used to check if the string `"a"` is contained in the string `"Pandas"`. If the value is found, the condition is `True`, and the code block `print("there are 2 a letters in the word pandas")` is executed. If the value is not found, the condition is `False` and the code block `print(" Panda is a python data science package")` is executed instead.

The for loop in the second example iterates over the characters in the string `"Pandas"` and prints each character.

The is keyword is used to test object identity. It returns `True` if the two objects being compared are the same object, and `False` if they are not. In the third example, the is keyword is used to compare the string `"''is''"` with the empty string. Because these are two different objects, the condition is False.Overall, the in and is keywords are useful tools for testing values and object identity in your programs.

---
## inputexample.py 
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
Author: Mwangi 
a simple user input function example 
"""

x = input()
y = 'x is ineger'
z = int(x) +1
w = float(x) + 2.5
```

This code is a simple script that takes user input and assigns it to the variable `x`. The variable `x` is then converted to an integer and assigned to the variable `z`, and is also converted to a float and assigned to the variable `w`. The variable `y` is assigned the string value '`x is ineger`' (note the typo in the string).

Here is a breakdown of what each line does:

`x = input()` - This line prompts the user to enter some input, which is then stored as a string in the variable x.
`y = 'x is ineger'` - This line assigns the string value `'x is ineger'` to the `variable y`.
`z = int(x) + 1` - This line converts the value of `x` to an integer using the `int()` function, adds `1` to it, and assigns the result to the variable z.
`w = float(x) + 2.5` - This line converts the value of `x` to a float using the `float()` function, adds` 2.5 `to it, and assigns the result to the variable `w`.

---
## inputs.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor
Author:Mwangi
Purpose: A program for variable input
    
"""
#input variables
first_name = input("First Name: ")
Middle_name = input("Middle Name: ")
Last_name = input("First Name: ")
age = input("Age : ")
gender = input("Gender: ")
title = input("Title: ")

# print output
print(title)
print(first_name)
print(Middle_name)
print(Last_name)
print(age, "years")
print(gender)

```
This code is a simple program that asks the user to input their first name, middle name, last name, age, gender, and title. It then prints out these variables in the specified order.

The first line of the code, `# -*- coding: utf-8 -*-`, is called a "shebang" and is used to specify the encoding of the script. It is not necessary for the code to run, but it is a good practice to include it at the top of your Python scripts, especially if they contain non-ASCII characters.

The next line, `"""`, marks the beginning and end of a multi-line string, which is used as a documentation string (also known as a docstring) for the script. Docstrings provide a brief description of the purpose of the script and are usually placed at the top of the script, immediately after the shebang.

The next three lines are input statements that prompt the user to enter their first name, middle name, and last name, respectively. The inputs are stored in the variables `first_name, Middle_name,` and `Last_name.`

The next line is an input statement that prompts the user to enter their age, which is stored in the age variable. The line after that is an input statement that prompts the user to enter their gender, which is stored in the gender variable. The final input statement prompts the user to enter their title, which is stored in the title variable.

The final six lines of the code are print statements that print out the variables in the specified order. The `print()` function takes the variables as arguments and prints them to the screen.

Overall, this code is a simple program that prompts the user to input their personal information, and then prints out this information in a formatted way.


---

The statement `if __name__ == "__main__"`: is a standard idiom in Python that is used to determine if a file is being run as the main program or if it's being imported as a module into another program.

When a Python script is executed, the interpreter sets the special name variable to "main". So, the code inside the block `if __name__ == "__main__"`: is executed only when the script is run as the main program, not when it's imported as a module into another program. This allows you to use the code in the script as a library of functions in another script.

Here's a simple example:

```python

def some_function():
    print("This function can be imported and used in another script.")

if __name__ == "__main__":
    print("This script is being run as the main program.")
    some_function()

```

When this script is run as the main program, the output would be:

**Output**

`This script is being run as the main program.`
`This function can be imported and used in another script.`

However, if the script is imported as a module into another script, the code inside the if __name__ == "__main__": block will not be executed, and only the function some_function() will be available for use.


---

## 1. mainfunction.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor
Author : Mwangi
Purpose : a simple main example 
"""
print ('is this a main function example ?') #this code will be executed first 

def main():
    print('yes it is main method function') # then this will be excuted second 
    
# for the code to excute the main method then a condition is given i.e.,
    
if __name__ == '__main__':
    main()
    
# the mainfunction can be imported in another program file i.e
# import mainfunction
# note this will call print ('is this a main function example ?')
```
This code demonstrates how to use the `main()` function in Python.

The `main()` function is a special function in Python that is often used as the entry point for a program. It is usually defined at the bottom of a program file, and is called when the program is run.

In this code, the `main()` function simply prints the string "`yes it is main method function`". The if statement at the bottom of the code checks if the current file is being run as the main program, using the built-in variable `__name__`. If `__name__` is equal to '`__main__'`, it means that the current file is being run as the main program, and the main() function is called.

This structure is often used in Python programs to allow the code in the file to be imported and used in other programs, without executing the `main()` function. If the file is imported as a module, the `__name__` variable will be set to the name of the module, and the `main()` function will not be called.Overall, the `main()` function is a useful way to organize and structure your code, and to specify the entry point for a program.

## 2. importmainfunction.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor
Author : Mwangi
Purpose : this program imports mainfunction 
"""
# note this will call print ('is this a main function example ?') first and 
# print ("call mainfunction ") second
import mainfunction
print ("call mainfunction ")
```

This code demonstrates how to import a module in Python.

In Python, a module is a file that contains a collection of related functions and variables. You can use the import statement to import a module and use its functions and variables in your program.

In this code, the module `mainfunction` is imported using the `import` statement. When the module is imported, the code in the module is executed. In this case, the code in the module mainfunction includes a print statement that prints the string `"is this a main function example ?"`

After the module is imported, the code in the current file continues to execute, and the string `"call mainfunction"` is printed.

Importing a module allows you to reuse code and organize your program into multiple files. It is a common practice to put related functions and variables in a module, and then import the module into your program when needed.Overall, importing modules is a useful way to structure and organize your code, and to reuse code across multiple programs.

---
### More Functions Example
```python

# python dictionary program that keeps cattle data
# create a dictionary called cattle_dict
# create a function getget_cattle
# use a for loop to iterate through the cattle_dict 
# and nested it using an if statement condition to select the 
# correct cow number

cattle_dict = [{'number': 258, 'name freshian': 'blackwhite','product': 'lean milk'
               },{'number': 259, 'name holsten': 'blackwhite','product': 'fat milk'},
               {'number': 257, 'name boran': 'brown','product': 'beef'} ]

def get_cattle(number):
    for cow in cattle_dict:
        if cow ['number'] == number:
            return cow
print(get_cattle(257))

cattle_dict = {258:{'number': 258, 'name freshian': 'blackwhite','product': 'lean milk'
               },259:{'number': 259, 'name holsten': 'blackwhite','product': 'fat milk'},
               257:{'number': 257, 'name boran': 'brown','product': 'beef'} }

def get_cattle(number):
   return cattle_dict[number]
print(get_cattle(257))

```
This code that creates a dictionary called cattle_dict, defines a function called get_cattle, and prints the result of calling get_cattle with the argument 257. The function get_cattle takes a number argument and returns a dictionary with the cattle data that matches the given number.

Here's how the code works:

    The cattle_dict dictionary contains three dictionaries, each with the cattle data for a different cow. The cattle data includes a number, a name that specifies the breed of the cow, and a product that the cow is used for (milk or beef).
    The get_cattle function takes a number argument, which is the number of the cow whose data we want to retrieve.
    The function uses a for loop to iterate through each dictionary in cattle_dict.
    For each dictionary, the function uses an if statement to check if the number key in the dictionary matches the number argument passed to the function.
    If a match is found, the function returns the dictionary with the cattle data for the corresponding cow.
    If no match is found, the function returns None.

In this case, calling get_cattle(257) returns


The function get_cattle takes a number argument and returns the corresponding cattle dictionary from the cattle_dict based on the number key.

In the given cattle_dict, there are three cattle dictionaries with keys 257, 258, and 259. The function get_cattle will return the cattle dictionary that matches the number argument.

In this case, when we call get_cattle(257), it will return the dictionary {'number': 257, 'name boran': 'brown', 'product': 'beef'} because this dictionary corresponds to the 257 key in cattle_dict.

Therefore, the output of print(get_cattle(257)) will be:

{'number': 257, 'name boran': 'brown', 'product': 'beef'}



## global_nonlocal.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor
Author : Mwangi
Purpose : Global and non-local:
    
    - global : This keyword is used to define a variable inside the function to be of a global scope.
    
"""

# initialize a global variable i

i = 140
j = 'stringos'

#read
def read():
     print (i)
     print (j)
     print ('----')
     
# change the value of i to 410
def mod1() :
    global i
    i = 410
    print ('----')
def mod_1a() :
    global j 
    j = 'strings' 
    print ('----')
# read the values and printing the results     
read()
mod1()
read()
mod_1a()
read()

```

This code demonstrates how to use the `global` keyword to access global variables from within a function.

In Python, variables defined outside of a function are considered global variables, and can be accessed from anywhere in the program. However, variables defined inside a function are considered local variables, and are only accessible within the function.

The global keyword is used to define a variable inside a function as a global variable, rather than a local variable. This allows you to access and modify the value of the global variable from within the function.

In this code, the variables `i` and `j` are defined outside of any function and are therefore global variables. The function `read()` simply prints the values of these global variables.

The function `mod1()` uses the global keyword to define the global variable `i` as a global variable inside the function. It then modifies the value of `i to be 410`. The function `mod_1a()` does the same thing with the global variable `j`.

When the functions are called and the values of the global variables are printed, you can see that the values have been modified by the functions.It's important to note that using the global keyword is generally not recommended, as it can make your code more difficult to understand and maintain. Instead, it is generally better to pass the global variables as arguments to the function, and return the modified values if necessary.

---

## functions.py
**Code:** 


```python
"""
Author : Mwangi
Purpose : two  basic python  functions
for computing a sentence and calculating profit 
"""
print(" ----- Example 1 ---- \n")
def  simple():
      p = print(" this is a function simple()")
# call the function 
simple()   

print(" ----- Example 2 ---- \n")

def profit( ):
      buying_price  = 12000
      selling_price  = 15000
      Net_Profit = selling_price - buying_price
      print ("Net profit is : ", Net_Profit)
profit()
```
This code demonstrates how to define and call functions in Python.

A function is a block of code that performs a specific task and can be called by name. In Python, you can define a function using the def keyword, followed by the function name and a set of parentheses `().` The code block inside the function is indented.

In the first example, the function `simple()` simply prints a sentence. To call the function, you can simply use its name followed by parentheses `()`. When the function is called, the code inside the function will be executed.

In the second example, the function `profit()` calculates the profit from selling a product given the buying price and the selling price. The function first defines the variables `buying_price` and `selling_price`, and then calculates the profit by subtracting the buying price from the selling price. Finally, it prints the profit. To call the function, you can use its name followed by `parentheses ()`.

Functions can also take arguments, which are values that can be passed to the function when it is called. The arguments are placed inside the parentheses in the function definition, and can be used inside the function as variables.

Functions can also return a value using the return keyword. The returned value can be stored in a variable or used in an expression.

Overall, functions are a useful tool for organizing and reusing code in your programs.

---


**Code:**
## decisions.py


```python
# -*- coding: utf-8 -*-
"""
Spyder Editor
Author : Mwangi
Purpose : decision making python program
"""
# if condition

a = 5 ;
if (a > 7):
    print ("5 is less than 7")
print ("STOP1!")

# if else condition

b = 10 ;
if (b < 11 ) :
    print ("10 is less than 11")
    
else:    
    print ("STOP2!")
# nested if 


i = 10
if (i == 10): 
    #  First if statement 
    if (i < 15): 
        print ("i is smaller than 15") 
    # Nested - if statement 
    # Will only be executed if statement above 
    # it is true 
    if (i < 12): 
        print ("i is smaller than 12 too") 
    else: 
        print ("i is greater than 15") 


#if-elif-else ladder        
#c = 2
c = 20        
d = 'done'

if (c == 20):
    print ("c is twenty")
elif (c == 25):
    print("c is twentyfive")
elif ('is a string data type '):
    print ('d is string')
else:
    
    print ('STOP3 and EXIT!!!!')

```

This code demonstrates different types of decision making statements in Python.

The `if` statement allows you to execute a block of code if a certain condition is met. In the first example, the condition is `a > 7`. If this condition is `True`, the code block `print("5 is less than 7")` will be executed. `If` the condition is `False`, the code block will be skipped.

The `if-else` statement allows you to specify two code blocks: one to be executed if the condition is `True`, and another to be executed if the condition is `False`. In the second example, the condition is `b < 11`. If this condition is `True`, the code block `print("10 is less than 11")` will be executed. If the condition is `False`, the code block `print("STOP2!")` will be executed instead.

The nested if statement allows you to use an if statement inside another `if` statement. In the third example, the inner if statement's condition is `i < 12`. This inner `if` statement will only be executed if the outer `if` statement's condition, `i == 10`, is `True`. If the outer `if` statement's condition is `False`, the inner `if` statement will be skipped.

The `if-elif-else` ladder allows you to specify multiple conditions and execute different code blocks based on which condition is met. In the fourth example, the program checks the value of` c` and executes the corresponding code block based on the value. If `c is 20`, the code block `print("c is twenty")` will be executed. If `c is 25`, the code block `print("c is twentyfive")` will be executed. If `c` is neither `20` nor `25`, the code block `print("STOP3 and EXIT!!!!")` will be executed.

It's also worth noting that you can use any expression as a condition in an if statement, as long as it evaluates to a boolean value `(True or False)`. In the fourth example, the condition '`is a string data type `' is a string literal, which is always True when used as a condition. This means that the code block `print('d is string')` will always be executed.

---
## loops.py
**Code:**

```python
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 21:40:39 2019
Author : Mwangi
Purpose : For and while loops
     
"""
print("-------- for loop --------\n")

clubs = ["Manchester united", "Chelsea", "Juventus", "Milan"]
for c in clubs:
    print(c)
    
print("-------- while loop --------\n")

i = 0
while i < 10:
    print(i)
    i +=1 
    
print("--------while and break loop --------\n")    
    
j = 0
while j < 10 :
    j += 1
    if j == 5:
        
        print("-------- break here then continue --------\n")
        continue
    print(j)

```
This code defines a list of strings called clubs and iterates over it using a `for` loop. It prints each element in the list to the console.

The code also defines a variable `i` and uses a while loop to iterate as long as `i` is less than 10. Inside the loop, it prints the value of `i` and increments `i by 1` on each iteration.

Finally, the code defines a variable `j` and uses a while loop to iterate as long as `j` is less than 10. Inside the loop, it increments `j` by 1 and then checks if `j` is equal to `5`. If it is, it prints a message and uses the continue statement to skip the rest of the loop and move on to the next iteration. Otherwise, it prints the value of `j`.

The for loop and the while loop are two common types of loops in Python that are used to repeat a block of code a certain number of times. The for loop is used to iterate over a sequence (such as a list or tuple) or other iterable object, while the while loop is used to repeat a block of code as long as a certain condition is met. The break and continue statements can be used to control the flow of the loop, allowing you to exit the loop early or skip certain iterations.

## appendlist.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor
Author : Mwangi
Purpose : Simple program to append data types creating a lists
"""
empty = []
print("1.Append an integer")
print("-------------------")
empty.append(21)
print("2.Append a float")
print("-------------------")
empty.append(50.0889)
print("3.Append a double")
print("-------------------")
empty.append(2.0)
print("4.Append a string")
print("-------------------")
empty.append('Stingo')
print("-------------------")
print(empty)
print("-------------------")
```
This code defines an empty list called "empty", and then uses the `append()` method to add several different data types to the list. The `append()` method adds an element to the end of a list.
The first element that is added is an `integer (21)`, the second element is a `float (50.0889)`, the third element is a `double (2.0)`, and the fourth element is a `string ('Stingo').` After all of the elements have been added to the list, the code prints the list using the print() function. The output of the code will be a list containing the four elements that were added, in the order they were added: 
`[21, 50.0889, 2.0, 'Stingo']`.

---

## SimpleFraction.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
Author: Mwangi 
a simple fraction example 
 Fraction(numerator, denominator)
"""

from fractions import Fraction
f = Fraction(5,10)
print (f)

```

This code imports the Fraction class from the fractions module and creates a new Fraction object with a numerator of 5 and a denominator of 10. The Fraction class is a built-in Python class that represents fractions.

When you run this code, it will print the fraction as a string, like this:

`Printed answer is : 1/2`
The Fraction class has a number of useful methods that you can use to perform operations on fractions, such as addition, subtraction, multiplication, and division. 

For example, you can add two fractions like this:

```python
```f1 = Fraction(1, 2)```
```f2 = Fraction(3, 4)```
```f3 = f1 + f2```
```print(f3)  # prints 7/4```
```
You can also use the Fraction class to convert a decimal number to a fraction. For example:
```python

`f = Fraction.from_float(0.25)`
`print(f)  # prints 1/4`

```
---
## Classes in Python

Purpose : this is  classes and objects in python 
Other than functions Python is an Object Oriented Language.In Python everything is an object both in properties and methods. 

##  **ClassesObjetcs.py**
**Code:**
```python


# -*- coding: utf-8 -*-
""" 
Author : Mwangi
Purpose : this is a classes and objects in python  
"""
class Football:
    Effort = 10

    def Gkeeper(self):
        print("Makes saves")
        self.Effort = 3
        

    def Defenders(self):
        if self.Effort >= 4:
            print("Good defending")
        else:
                print("Not good enough add a defensive midfielder")

    def Midfielders(self):
        if self.Midfielders >= 5:
            print("Team is 65% complete")
        else:
                 print("Add 2 good strikers")

    def Strikers(self):
        if self.Strikers >= 7: 
            print("That is a very good team")


    soccer = Football()

    soccer.Gkeeper()
    soccer.Defenders()
    soccer.Midfielders()
    soccer.Strikers()


```

This code defines a class called Football with four methods: `Gkeeper(), Defenders(), Midfielders(),` and `Strikers()`. The `Gkeeper()` method prints a message and sets the value of the Effort field to 3. The Defenders method checks the value of the Effort field and prints a message based on its value. The Midfielders and Strikers methods also check the values of their respective fields and print messages based on those values.

To create an object of this class, you can use the Football class name followed by parentheses and assign the result to a variable, like this:

`soccer = Football()`
You can then call the object's methods by using the dot notation and passing the object as the first argument to the method. For example:

`soccer.Gkeeper()`
This will call the `Gkeeper()` method on the soccer object and execute the code inside the method.

The self keyword is used to refer to the current object within the class methods. It is equivalent to this in Java. When you call a method on an object, the object is automatically passed as the first argument to the method, so you don't need to specify it explicitly.

---

##  **ClassesandObjects.py**
**Code:**

```python
# -*- coding: utf-8 -*-
""" 
Author : Mwangi
Purpose : this is a classes and objects in python  
"""
#class Football has 4 functions
class Football:
    Effort = 10
    Defenders = 10

    def Gkeeper(self):
        print("Makes saves")
        self.Effort = 10
        

    def Defenders(self):
        if self.Effort >= 10:
            print("Good defending")
        else:
                print("Not good enough add a defensive midfielder")

    def Midfielders(self):
        if self.Midfielders >= 10:
            print("Team is 65% complete")
        else:
                 print("Add 2 good strikers")

    def Strikers(self):
        if self.Strikers >= 10: 
            print("That is a very good team")

# defining objects
    
    def main():
         soccer = Football()
         soccer.Gkeeper()
         soccer.Defenders()
         soccer.Midfielders()
         soccer.Strikers()

    if __name__ == " __main__":
        main()
```
This code defines a class called Football with four methods: `Gkeeper(), Defenders(), Midfielders(), and Strikers()`. The `Gkeeper()` method prints a message and sets the value of the Effort field to 10. The Defenders method checks the value of the Effort field and prints a message based on its value. The Midfielders and Strikers methods also check the values of their respective fields and print messages based on those values.

The main function creates an object of the Football class and calls its methods. The `if __name__ == "__main__"` block is used to specify that the main function should be executed when the script is run directly, rather than when it is imported by another script.

To run this script, you can use the python command followed by the name of the script file:python football.py
This will create an object of the Football class, call its methods, and print the messages that are produced by those methods.

---

**list_sets_dictionaries.py**
**Code**
```python
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:47:20 2019
Author:Mwangi
Purpose: Lists ,Sets and Dictionaries in Python
- A list is a container which we used to store multiple data
- Set is also another python collection data type. Set’s can’t have duplicates.
- Dictionary is also a python collection data type. These are unordered, changeable 
- and indexed. In python dictionaries are written using curly brackets. “{}”. Dictionaries have keys and values.
"""
print("---------Lists----------\n")

Lists_Participants = [10,21,23,36,25,14,78,96,85,74,41,52,63,30,20,]
print (Lists_Participants)
print(Lists_Participants[2])
print(Lists_Participants[7])
print(Lists_Participants[5])
print(Lists_Participants[9])

print("---------Sets----------\n")

names = {'Ben','Penalty', 'Curtis', 'Yidah','Curtis', 'Everton', 'Yidah'}
for i in names:
    print(i)
    

print("---------Dictionaries----------\n")

names = {'Ben - ':'Male ','Penalty - ':'Sports', 'Curtis - ':'Male', 'Yidah - ':'Player','Curtis - ':'Boy','Everton - ':'Club', 'Yidah - ':'Man'}
for i, j  in names.items():
    print(i+j)
```

This code is a program that demonstrates the use of lists, sets, and dictionaries in Python.
The first part of the code is a list called `Lists_Participants`, which contains 15 integers. The list is then printed to the screen using the `print()` function.The next four lines of code print out the third, eighth, sixth, and tenth elements of the list, respectively. This is done by using the list indexing syntax, which allows you to access specific elements of the list by their position in the list.

The second part of the code is a set called names, which contains six strings. A set is a collection data type in Python that is unordered and does not allow duplicates. The code then uses a for loop to iterate through the set and print out each element.

The third part of the code is a dictionary called names, which contains six key-value pairs. A dictionary is a collection data type in Python that is unordered, changeable, and indexed. It is written using curly brackets, and it consists of keys and values. The code then uses a for loop to iterate through the dictionary and print out each key-value pair.Overall, this code is a simple program that demonstrates the use of lists, sets, and dictionaries in Python, and how to access and print their elements.


### listsIteration.ipynb
**Code:**

```python
# Lists and Iteration  

cars = ["Benz", "Toyota","Audi", "BMW", "Renault"]
for i in cars:
    print (i)
print("------------\n")
for j in cars:
    if len(j) > 4:
        print(j)
print("--------------\n")
print("Print for loop within the list")
cars_long= [ i for i in cars if len(i) > 3]
print(cars_long)
print("--------------\n")
print("Contacts for each car:\n")
car_contact = {"Benz-": "benz@daimler.co", "Toyota-":"toyota@toyota.jp.com","Audi-":"audi@quatro.ge.com", "BMW-":"bmw@bm.ge.com",
               "Renault-":"renault@renault.fr.com"}
for k,emails in car_contact.items():
    print(k,emails)

print ("---End!---")

```

This program defines a list of car names called cars, and then uses for loop to iterate over the list and print each element in the list.

In the first loop, it simply prints the car names. The output will be:

`Benz`
`Toyota`
`Audi`
`BMW`
`Renault`

In the second loop, it checks the length of each car name and if it is greater than 4 characters, it prints the name. The output will be:

`Toyota`
`Audi`
`Renault`

In the next section, it uses list comprehension to create another list called cars_long that contains only the names of the cars which have more than 3 characters. The output will be:


Print for loop within the list
`['Toyota', 'Audi', 'Renault']`

Then, it defines a dictionary called car_contact which contains the contact information of each car company, with the car name as the key and the email as the value. Finally, it uses a for loop and the items() method of the dictionary to iterate over the key-value pairs of the dictionary and print each pair. The output will be:

Contacts for each car:

`Benz- benz@daimler.co`
`Toyota- toyota@toyota.jp.com`
`Audi- audi@quatro.ge.com`
`BMW- bmw@bm.ge.com`
`Renault- renault@renault.fr.com`

The code ends by printing "---End!---".

---
## tryExcept.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
Author: Mwangi 
a try ... except error handler 
"""
try:
    x = int(input("Enter an integer number: "))
    
except ValueError:
    print("Invalid Number! Try again ")

```
The code is a basic implementation of a `try-except` block in Python. The try block contains the code that might throw an exception, and the except block contains the code that will handle the exception if it is raised.

In this case, the try block is attempting to cast the user's input to an integer using the `int()` function. If the input cannot be cast to an integer (for example, if the user enters a string or a float), a `ValueError` will be raised. The except block will catch this error and print a message to the user, telling them to try again.

This is a useful way to handle errors and ensure that your code continues to run smoothly even if something goes wrong. You can use try-except blocks to handle a wide variety of errors, including syntax errors, type errors, and other exceptions that might occur while your code is running.

---

## Graphical User Interface

**Code:**
```python
# code creates a textbox
import tkinter as tk
from tkinter import *

win = Tk()
win.resizable(False, False)
win.title("Text Box Widget")

text = Text(win, height=10)
text.pack()

win.mainloop()

```

The code creates a GUI using the Tkinter library in Python. The first code creates a text box widget and the second code creates a label widget. The code uses the Tk() function to create a Tkinter window and the .resizable() function to make the window non-resizable. The .title() function sets the title of the window. The Text() and Label() functions are used to create the text box and label widgets, respectively. The .pack() function is used to add the widgets to the window. Finally, the .mainloop() function is used to keep the window open until the user closes it.
**Output**

![Screenshot from 2023-01-16 13-49-07](https://user-images.githubusercontent.com/6685756/212662009-dc2fce75-fc28-41ae-b2e9-79359327cd59.png)


---

### Creat_textbox_withtext.py
**Code:**

```python
# code creates a textbox
import tkinter as tk
from tkinter import *

win = Tk()
win.resizable(False, False)
win.title("Text Box Widget")

text = Text(win, height=10)
text.pack()

text.insert('1.0', 'Insert module allows us to insert text')

win.mainloop()

```

This code creates a text box widget using the Tkinter library in Python. The Tk() function creates a Tkinter window and the .resizable() function makes the window non-resizable. The .title() function sets the title of the window. The Text() function is used to create the text box widget. The .pack() function adds the widget to the window. The .insert() function is used to insert text into the text box. Finally, the .mainloop() function is used to keep the window open until the user closes it.
 
**Output**

![Screenshot from 2023-01-16 14-10-16](https://user-images.githubusercontent.com/6685756/212664993-8f09924b-eae9-4d3f-93f3-903a07e11385.png)

---

### File_Delete.py
**Code:**

```python
# this code deletes files from the directory folder

import os
from tkinter import *

# Create an instance of tkinter window
win = Tk()
win.geometry("700x250")

def Delete_File():
    if os.path.exists("remove3.txt"):
        os.remove("remove3.txt")
    else:
        print("The file does not exist") 
    
Delete_btn = Button(win, text="Delete", command=Delete_File)
Delete_btn.pack()

win.mainloop()

```
This code deletes a file called "remove3.txt" from a directory folder. The code uses the Tkinter library in Python to create an instance of a tkinter window. The .geometry() function is used to set the size of the window. The Delete_File() function is used to delete the file from the directory folder using the os.remove() function. The Delete_btn is a button widget used to call the Delete_File() function when clicked. The .pack() function is used to add the button widget to the window. Finally, the .mainloop() function is used to keep the window open until the user closes it.


**Output**


![Screenshot from 2023-01-16 14-37-14](https://user-images.githubusercontent.com/6685756/212669581-2cbf62bd-4119-483a-89b6-c23d0d48c72c.png)

---

### buttonMsgBox_GUI.py
**Code:**
```python
# this code displays a message in a message box

from tkinter import *
import tkinter as tk
from tkinter import messagebox

r = tk.Tk()

def echoPhraseInMsgBox():
    return messagebox.showinfo("Button Pressed")
   


button = tk.Button(r, text='Print', width=25, command=echoPhraseInMsgBox)

button.pack()
r.mainloop()

```
This code creates a button widget using the Tkinter library in Python. The Tk() function creates a Tkinter window. The echoPhraseInMsgBox() function is used to display a message in a message box when the button is pressed using the messagebox.showinfo() function. The button widget is created using the Button() function and is added to the window using the .pack() function. The .mainloop() function is used to keep the window open until the user closes it.

**Output**

![Screenshot from 2023-01-16 15-30-14](https://user-images.githubusercontent.com/6685756/212678657-10fafed3-0dd4-44fa-aebb-1d3d6cf75ba3.png)

---

### button_GUI.py
**Code:**
```python
# In this code a function echoPhrase() is created and
# it is called by the press of a button in other words 
# a button can be used for argument parsing.
# This code also demonstrates customization of functions in python.


from tkinter import *
import tkinter as tk

r = tk.Tk()
def echoPhrase():
    print("Echoed message is, Button Pressed")

r.title('Buttons')
button = tk.Button(r, text='Print', width=25, command=echoPhrase)

button.pack()

```
This code creates a button widget using the Tkinter library in Python. The Tk() function creates a Tkinter window and the .title() function sets the title of the window. The echoPhrase() function is used to print a message when the button is pressed. The button widget is created using the Button() function and is added to the window using the .pack() function. Finally, the .mainloop() function is used to keep the window open until the user closes it.

**Output**

![Screenshot from 2023-01-16 15-35-56](https://user-images.githubusercontent.com/6685756/212679975-0b9ecdea-87f5-4aff-bef1-6a3e69e4c786.png)

---

### fileOpen.py
**Code:**

```python
# this code demonstrates opening of files in python 
# the code only allows the user to open and read txt files.

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile

r = Tk()
# this function will open a text file only after button is pressed
def open_file():
    f = askopenfile(mode ='r', filetypes =[('text file', '*.txt')]) #only txt files will be opened
     if f is not None:
        content = f.read()
        print(content)
#Below code is reuseable in the event of opening a file is required
#with open("File_Open.txt", "r") as f:
#    Label(r, text=f.read()).pack()

bt= Button(r, text='Read', command= open_file)
bt.pack(side = TOP, pady = 50)    
    
    

r.mainloop()

```

This code creates a button widget using the Tkinter library in Python. The Tk() function creates a Tkinter window. The open_file() function is used to open a text file when the button is pressed using the askopenfile() function. The .read() function is used to read the contents of the file. The button widget is created using the Button() function and is added to the window using the .pack() function. Finally, the .mainloop() function is used to keep the window open until the user closes it.

**Output**

![Screenshot from 2023-01-16 15-46-17](https://user-images.githubusercontent.com/6685756/212681571-4f66fbe6-1c51-47f9-990e-a83d937539f4.png)

---

### test_mult_func.py
**Code:**
```python 
# Import tkinter and Button Widget
from tkinter import Tk
from tkinter.ttk import Button


# Demo function 1
def fun1():
	print("Function 1")


# Demo function 2
def fun2():
	print("Function 2")


if __name__ == "__main__":
	# Creating top-level window
	master = Tk()

	# Setting window title
	master.title("Bind multiple function to Button")

	# Setting window Dimensions
	master.geometry("400x250")

	# Creating a button with more than one command using lambda
	button = Button(master, text="Button", command=lambda: [fun1(), fun2()])

	# Attaching button to the top-level window
	# Always remember to attach your widgets to the top-level
	button.pack()

	# Mainloop that will run forever
	master.mainloop()
```
This code creates a button widget using the Tkinter library in Python. The Tk() function creates a Tkinter window and the .title() function sets the title of the window. The .geometry() function is used to set the size of the window. The button widget is created using the Button() function and is added to the window using the .pack() function. The command argument of the Button() function is used to bind multiple functions to the button using the lambda keyword. Finally, the .mainloop() function is used to keep the window open until the user closes it.

**Output**


![Screenshot from 2023-01-16 15-51-09](https://user-images.githubusercontent.com/6685756/212682466-0c7c068e-4abb-46f1-8b3a-4552393f3c53.png)

---
# Matplotlib
### Matplot_Numpy.ipynb
**Code:**

```python
import math
import matplotlib.pyplot as plt
import numpy as np
print("Plot thickness of a line using linewidth")
plt.plot([1,2,4,2,1,0,1,2,1,4],linewidth=2.0)
plt.show()

t = np.arange(0,5,0.1)
y1 = np.sin(2*np.pi*t)
y2 = np.sin(2*np.pi*t)
plt.subplot(211)
plt.plot(t,y1,'b-.')
plt.subplot(212)
plt.plot(t,y2,'r--')

```

The first code block plots a line graph using the Matplotlib library, with a specified line width of 2.0. The second code block uses the NumPy library to create two arrays of data (t and y1, y2) and plots them using the Matplotlib library. The subplot function is used to create two subplots in a single figure, with the first plot using a blue dashed-dot line style and the second plot using a red dashed line style. The plt.show() function is used to display the figure.


**Output:**
[Plotted  Graphs ](https://github.com/mngugi/Python_Programming-/blob/master/Matplot_Numpy.ipynb)

### Pyplot.ipynb
**Code:**
```python
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
a='''pass a list of numbers or an array to the plt.plot() function, matplotlib assumes it is the
sequence of y values of the chart, and it associates them to the natural sequence of values x: 0,1,2,3, ... .  '''
print(a)
plt.plot([0,1,2,3,4,5,6,7,8,9])
plt.show()

print(" ")
print("Using ro to represent the blue line using dots ")
plt.plot([0,2,4,6,8,10],'ro')
plt.show()

print(" ")
print("Add, x,ylabels,text,grid axis range and title ")
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Times New Roman')
#plt.xlabel('Counting',color='gray')
#plt.ylabel('Square values',color='gray')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(1.1,12,r'$y = x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})
plt.grid(True)
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.savefig('my_chart.png')

```
**Output**

[Pyplot.ipynb Graphs ](https://github.com/mngugi/Python_Programming-/blob/master/Pyplot.ipynb)



This code uses the Matplotlib library to create a line plot. In the first code block, a simple line plot is created by passing a list of numbers to the plt.plot() function. Matplotlib assumes that the list represents the y-values of the chart, and it associates them to the natural sequence of x-values: 0,1,2,3, ...

In the second code block, the same list of numbers is passed to the plt.plot() function, but this time it is followed by the string 'ro', which tells Matplotlib to represent the line using red dots.

In the third code block, the axis range is set by the plt.axis() function, the title of the plot is set by plt.title() function, x and y labels are commented out here, the text is added to the plot by plt.text() function, a grid is added to the plot by plt.grid(True) function and a list of x, y values are plotted using red dots. plt.savefig() function is used to save the figure as an image file ('my_chart.png').

It also uses pandas library but it is not being used here in the given code snippet.

---

## Numpy
### Array Manipulation

### joining_arrays.py
**Code:**

```python
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

```

This code uses the NumPy library to demonstrate different ways of stacking arrays. It creates four 1D arrays: arr1, arr2, arr3 and arr4.

The first method demonstrated is vertical stacking, which is done using the np.vstack() function. This function takes a tuple of arrays as an argument and concatenates the arrays along the vertical axis (i.e., adding new rows to the first array). In the code, the np.vstack() function is used to stack arr1, arr2, and arr3 vertically, resulting in a new array a with 3 rows and 5 columns.

The second method demonstrated is horizontal stacking, which is done using the np.hstack() function. This function also takes a tuple of arrays as an argument and concatenates the arrays along the horizontal axis (i.e., adding new columns to the first array). In the code, the np.hstack() function is used to stack arr1, arr2, and arr3 horizontally, resulting in a new array b with 1 row and 15 columns.

The third method demonstrated is row stacking, which is done using the np.row_stack() function. This function is same as vstack. In the code, the np.row_stack() function is used to stack arr1, arr2, and arr3 vertically, resulting in a new array c with 3 rows and 5 columns.

The fourth method demonstrated is column stacking, which is done using the np.column_stack() function. This function is same as hstack. In the code, the np.column_stack() function is used to stack arr1, arr2, and arr3 horizontally, resulting in a new array d with 1 row and 15 columns.


### spliting_arrays.py
**Code:**

```python
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

```
 This code uses the NumPy library to demonstrate different ways of splitting arrays. It creates three 2D arrays: Arr, Arr1, Arr2.

The first method demonstrated is horizontal splitting, which is done using the np.hsplit() function. This function takes two arguments, first the array that needs to be split and second the indices where the array needs to be split. In the code, the np.hsplit() function is used to split Arr into two parts by index 2, resulting in two new arrays B and C with 3 rows and 2 columns each.

The second method demonstrated is vertical splitting, which is done using the np.vsplit() function. This function takes two arguments, first the array that needs to be split and second the indices where the array needs to be split. In the code, the np.vsplit() function is used to split Arr1 into two parts by index 2, resulting in two new arrays D and E with 2 rows and 4 columns each.

The third method demonstrated is np.split() function, which allows you to split the array into nonsymmetrical parts. It takes three arguments, first the array that needs to be split, second the indices where the array needs to be split and third the axis along which the array needs to be split. In the code, the np.split() function is used to split Arr2 into three parts by the indices 1, 3 along the axis 1, resulting in three new arrays with 2 rows and 1 column, 1 row and 2 column and 2 rows and 2 columns.

---

### Data_Management.py
**Code:**

```python
import numpy as np
import pandas as pd

store = "Cartwheeldata.csv"
df = pd.read_csv(store)
#pd.set_option('display.max_columns', None)

type(df)
df.head()
pd.set_option('display.max_columns', False)
print(df)

```
This code is using two libraries, numpy and pandas.
It is loading a CSV file "Cartwheeldata.csv" into a DataFrame object (df) by using the pandas library's read_csv() function. The "store" variable is storing the file name and path of the CSV file.

The type() function is used to check the type of df. The output will be 'pandas.core.frame.DataFrame'.

The head() function is used to display the first 5 rows of the DataFrame.

The pd.set_option('display.max_columns', False) line will limit the number of columns displayed when using the print(df) statement, to prevent the output from becoming too wide and difficult to read.

The final print(df) statement will display the entire DataFrame object.

---

### Data_Management_cols.py
**Code:**

```python
import numpy as np
import pandas as pd

store = "Cartwheeldata.csv"
df = pd.read_csv(store)
df_cols = df.columns
print(df_cols) 

```
This code is using two libraries, numpy and pandas.
It is loading a CSV file "Cartwheeldata.csv" into a DataFrame object (df) by using the pandas library's read_csv() function. The "store" variable is storing the file name and path of the CSV file.

The df.columns will return the column names of the dataframe.

The variable df_cols is storing the columns of the dataframe.

The final print(df_cols) statement will display the column names of the dataframe.

### Data_Management_groupby.py
**Code:**

```python

import numpy as np
import pandas as pd

a = '''
This output indicates that we have two types of combinations.
Case 1: Gender = F & Gender Group = 1
Case 2: Gender = M & GenderGroup = 2.
This validates our initial assumption that these two fields 
essentially portray the same information.
'''
print(a)
store = "Cartwheeldata.csv"
df = pd.read_csv(store)

j = df.groupby(['Gender', 'GenderGroup']).size()
print(j)

```
This code is using two libraries, numpy and pandas.

The first print statement is a string variable which explains the output that will be given later.

It is loading a CSV file "Cartwheeldata.csv" into a DataFrame object (df) by using the pandas library's read_csv() function. The "store" variable is storing the file name and path of the CSV file.

The variable j is storing the result of the groupby function on the 'Gender' and 'GenderGroup' columns of the dataframe. The size() function returns the count of rows for each group.

The final print(j) statement will display the count of rows for each unique combination of 'Gender' and 'GenderGroup' columns. This will validate the assumption mentioned in the string variable 'a' that these two fields essentially portray the same information.

---

###  Data_Management_splice.py
**Code:**

```python

import numpy as np
import pandas as pd

store = "Cartwheeldata.csv"
df = pd.read_csv(store)
i = df.loc[:, "Wingspan"]

print(i)

```

This code is using two libraries, numpy and pandas.

It is loading a CSV file "Cartwheeldata.csv" into a DataFrame object (df) by using the pandas library's read_csv() function. The "store" variable is storing the file name and path of the CSV file.

The df.loc[] function is used for indexing by label and it accepts a boolean array of the same length as the axis being selected. In this case the location is selected by the column "Wingspan".

The variable i is storing the selected column "Wingspan" from the dataframe.

The final print(i) statement will display the values of the column "Wingspan" of the dataframe.

---

### Data_Management_splice2.py

**Code:**
```python
import numpy as np
import pandas as pd

store = "Cartwheeldata.csv"
df = pd.read_csv(store)
i = df.loc[:, ["Wingspan", "Height", "Age"]]

print(i)

```
This code is similar to the previous example, but it is now selecting multiple columns of the dataframe using the df.loc[] function. Instead of a single column, it is now passing a list of column names ["Wingspan", "Height", "Age"]. This will select the columns "Wingspan", "Height", and "Age" of the dataframe.

The final print(i) statement will display the values of the selected columns "Wingspan", "Height", "Age" of the dataframe.

---

### phoneNum-locate.ipynb
**Code:**
```python

#from opencage.geocoder import OpenCageGeocode
import phonenumbers
#from myphone import number
from phonenumbers import geocoder

number = "+254716$$$###"
phnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(phnumber,"en")
print(location)

```
This code is trying to use the phonenumbers library from the libphonenumber library. This library provides functionality for parsing, formatting, and validating international phone numbers.

In this code, the phonenumbers.parse method is used to parse the phone number string number and store the resulting phonenumber object in the phnumber variable. Then the geocoder.description_for_number method is used to get a human-readable description of the geographic area that the phone number belongs to, and it returns the location in English.

However, the phone number string number is not valid, as it contains multiple $ characters. You need to provide a valid phone number for the code to work.

```python
from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

```
This code is is also using the phonenumbers library, specifically the carrier module. This module provides functionality for determining the carrier (mobile operator) of a phone number.

In this code, the phonenumbers.parse method is used to parse the phone number string number and store the resulting phonenumber object in the service_pro variable. Then the carrier.name_for_number method is used to determine the name of the carrier for the given phone number, and it returns the name in English.

However, just like the previous code, the phone number string number is not valid, and you need to provide a valid phone number for the code to work.

```python

import opencage
from opencage.geocoder import OpenCageGeocode
import phonenumbers
#from myphone import number
from phonenumbers import geocoder
import folium


key = 'b2cc20773cab4ee3aec2ee1430ff287c'

geocoder = OpenCageGeocode(key)
query = str(location)

results = geocoder.geocode(query)
print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

srcMap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(srcMap)

srcMap.save("searchlocation.html")


```

This code is using a number of different libraries and APIs to perform geocoding and create a map. Here is a brief overview of what the code does:

    Imports the opencage library and the OpenCageGeocode class from the opencage.geocoder module, as well as the phonenumbers and folium libraries.

    Sets a key variable to an API key for the OpenCage Geocoding API.

    Initializes an instance of the OpenCageGeocode class, passing in the API key.

    Sets the query variable to the string value of location.

    Calls the geocode method on the geocoder object, passing in the query variable, and stores the result in the results variable.

    Extracts the latitude and longitude from the first result in the results list and stores them in the lat and lng variables, respectively.

    Creates a folium map centered at the latitude and longitude, with a zoom level of 9.

    Adds a marker to the map at the latitude and longitude, with a popup showing the location string.

    Saves the map to an HTML file.

This code will only work if the location variable has a valid value, and if the OpenCage Geocoding API is accessible and has not reached its usage limit for the given API key.

**Code Output:**

```xml
[{'annotations': {'DMS': {'lat': "1° 26' 31.08588'' N", 'lng': "38° 25' 53.03100'' E"}, 'MGRS': '37NDB3674759389', 'Maidenhead': 'KJ91fk16sb', 'Mercator': {'x': 4278163.6, 'y': 159461.66}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?relation=192798#map=16/1.44197/38.43140', 'note_url': 'https://www.openstreetmap.org/note/new#map=16/1.44197/38.43140&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=1.44197&mlon=38.43140#map=16/1.44197/38.43140'}, 'UN_M49': {'regions': {'AFRICA': '002', 'EASTERN_AFRICA': '014', 'KE': '404', 'SUB-SAHARAN_AFRICA': '202', 'WORLD': '001'}, 'statistical_groupings': ['LEDC']}, 'callingcode': 254, 'currency': {'alternate_symbols': ['Sh'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'KES', 'iso_numeric': '404', 'name': 'Kenyan Shilling', 'smallest_denomination': 50, 'subunit': 'Cent', 'subunit_to_unit': 100, 'symbol': 'KSh', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇰🇪', 'geohash': 'sb724w8bh6qgzqejc5kw', 'qibla': 3.79, 'roadinfo': {'drive_on': 'left', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1675136340, 'astronomical': 1675132020, 'civil': 1675135020, 'nautical': 1675133520}, 'set': {'apparent': 1675179600, 'astronomical': 1675183920, 'civil': 1675180920, 'nautical': 1675182420}}, 'timezone': {'name': 'Africa/Nairobi', 'now_in_dst': 0, 'offset_sec': 10800, 'offset_string': '+0300', 'short_name': 'EAT'}, 'what3words': {'words': 'consortium.undesirable.spite'}, 'wikidata': 'Q114'}, 'bounds': {'northeast': {'lat': 4.62, 'lng': 41.9067502}, 'southwest': {'lat': -4.8995204, 'lng': 33.9096888}}, 'components': {'ISO_3166-1_alpha-2': 'KE', 'ISO_3166-1_alpha-3': 'KEN', '_category': 'place', '_type': 'country', 'continent': 'Africa', 'country': 'Kenya', 'country_code': 'ke'}, 'confidence': 1, 'formatted': 'Kenya', 'geometry': {'lat': 1.4419683, 'lng': 38.4313975}}, {'annotations': {'DMS': {'lat': "0° 1' 39.25704'' N", 'lng': "36° 6' 19.59984'' E"}, 'MGRS': '37MAV7777096948', 'Maidenhead': 'KI89bx23pj', 'Mercator': {'x': 4019239.685, 'y': -3048.688}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?node=9566095121#map=16/-0.02757/36.10544', 'note_url': 'https://www.openstreetmap.org/note/new#map=16/-0.02757/36.10544&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=-0.02757&mlon=36.10544#map=16/-0.02757/36.10544'}, 'UN_M49': {'regions': {'AFRICA': '002', 'EASTERN_AFRICA': '014', 'KE': '404', 'SUB-SAHARAN_AFRICA': '202', 'WORLD': '001'}, 'statistical_groupings': ['LEDC']}, 'callingcode': 254, 'currency': {'alternate_symbols': ['Sh'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'KES', 'iso_numeric': '404', 'name': 'Kenyan Shilling', 'smallest_denomination': 50, 'subunit': 'Cent', 'subunit_to_unit': 100, 'symbol': 'KSh', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇰🇪', 'geohash': 'kzcxvdgpmu6dhw4v22nj', 'qibla': 9.38, 'roadinfo': {'drive_on': 'left', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1675136760, 'astronomical': 1675132440, 'civil': 1675135500, 'nautical': 1675134000}, 'set': {'apparent': 1675180320, 'astronomical': 1675184580, 'civil': 1675181580, 'nautical': 1675183080}}, 'timezone': {'name': 'Africa/Nairobi', 'now_in_dst': 0, 'offset_sec': 10800, 'offset_string': '+0300', 'short_name': 'EAT'}, 'what3words': {'words': 'widgets.humane.rainmaker'}}, 'bounds': {'northeast': {'lat': -0.0075714, 'lng': 36.1254444}, 'southwest': {'lat': -0.0475714, 'lng': 36.0854444}}, 'components': {'ISO_3166-1_alpha-2': 'KE', 'ISO_3166-1_alpha-3': 'KEN', 'ISO_3166-2': ['KE-31'], '_category': 'place', '_type': 'village', 'continent': 'Africa', 'country': 'Kenya', 'country_code': 'ke', 'state': 'Nakuru', 'village': 'Kenya'}, 'confidence': 7, 'formatted': 'Kenya, Nakuru', 'geometry': {'lat': -0.0275714, 'lng': 36.1054444}}, {'annotations': {'DMS': {'lat': "3° 2' 38.23764'' S", 'lng': "37° 41' 50.61552'' E"}, 'MGRS': '37MCS5524363460', 'Maidenhead': 'KI86uw39qk', 'Mercator': {'x': 4196454.612, 'y': -336743.674}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?way=613812253#map=16/-3.04395/37.69739', 'note_url': 'https://www.openstreetmap.org/note/new#map=16/-3.04395/37.69739&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=-3.04395&mlon=37.69739#map=16/-3.04395/37.69739'}, 'UN_M49': {'regions': {'AFRICA': '002', 'EASTERN_AFRICA': '014', 'KE': '404', 'SUB-SAHARAN_AFRICA': '202', 'WORLD': '001'}, 'statistical_groupings': ['LEDC']}, 'callingcode': 254, 'currency': {'alternate_symbols': ['Sh'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'KES', 'iso_numeric': '404', 'name': 'Kenyan Shilling', 'smallest_denomination': 50, 'subunit': 'Cent', 'subunit_to_unit': 100, 'symbol': 'KSh', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇰🇪', 'geohash': 'kz6y9vf7svtttz8pqwyr', 'qibla': 4.77, 'roadinfo': {'drive_on': 'left', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1675136160, 'astronomical': 1675131840, 'civil': 1675134900, 'nautical': 1675133340}, 'set': {'apparent': 1675180140, 'astronomical': 1675184460, 'civil': 1675181460, 'nautical': 1675182960}}, 'timezone': {'name': 'Africa/Nairobi', 'now_in_dst': 0, 'offset_sec': 10800, 'offset_string': '+0300', 'short_name': 'EAT'}, 'what3words': {'words': 'decoy.previews.sentence'}}, 'bounds': {'northeast': {'lat': -3.0397123, 'lng': 37.7019395}, 'southwest': {'lat': -3.0504031, 'lng': 37.6908888}}, 'components': {'ISO_3166-1_alpha-2': 'KE', 'ISO_3166-1_alpha-3': 'KEN', 'ISO_3166-2': ['KE-10'], '_category': 'place', '_type': 'neighbourhood', 'continent': 'Africa', 'country': 'Kenya', 'country_code': 'ke', 'residential': 'Rombo, Kajiado, Kenya', 'state': 'Kajiado County', 'village': 'Rombo'}, 'confidence': 8, 'formatted': 'Rombo, Kajiado, Kenya, Kajiado County, Kenya', 'geometry': {'lat': -3.0439549, 'lng': 37.6973932}}, {'annotations': {'DMS': {'lat': "0° 9' 14.48208'' N", 'lng': "37° 53' 47.37156'' E"}, 'MGRS': '37NCA7719917027', 'Maidenhead': 'KJ80wd76nx', 'Mercator': {'x': 4218618.205, 'y': 17030.98}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?way=725987930#map=16/0.15402/37.89649', 'note_url': 'https://www.openstreetmap.org/note/new#map=16/0.15402/37.89649&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=0.15402&mlon=37.89649#map=16/0.15402/37.89649'}, 'UN_M49': {'regions': {'AFRICA': '002', 'EASTERN_AFRICA': '014', 'KE': '404', 'SUB-SAHARAN_AFRICA': '202', 'WORLD': '001'}, 'statistical_groupings': ['LEDC']}, 'callingcode': 254, 'currency': {'alternate_symbols': ['Sh'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'KES', 'iso_numeric': '404', 'name': 'Kenyan Shilling', 'smallest_denomination': 50, 'subunit': 'Cent', 'subunit_to_unit': 100, 'symbol': 'KSh', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇰🇪', 'geohash': 'sb4byk53hrbtg9mc426q', 'qibla': 4.94, 'roadinfo': {'drive_on': 'left', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1675136340, 'astronomical': 1675132020, 'civil': 1675135080, 'nautical': 1675133580}, 'set': {'apparent': 1675179840, 'astronomical': 1675184160, 'civil': 1675181160, 'nautical': 1675182660}}, 'timezone': {'name': 'Africa/Nairobi', 'now_in_dst': 0, 'offset_sec': 10800, 'offset_string': '+0300', 'short_name': 'EAT'}, 'what3words': {'words': 'wavering.temperature.piglet'}}, 'bounds': {'northeast': {'lat': 0.1540899, 'lng': 37.8965466}, 'southwest': {'lat': 0.1539799, 'lng': 37.8964179}}, 'components': {'ISO_3166-1_alpha-2': 'KE', 'ISO_3166-1_alpha-3': 'KEN', 'ISO_3166-2': ['KE-26'], '_category': 'outdoors/recreation', '_type': 'park', 'continent': 'Africa', 'country': 'Kenya', 'country_code': 'ke', 'park': 'kenya', 'state': 'Meru County'}, 'confidence': 9, 'formatted': 'kenya, Meru County, Kenya', 'geometry': {'lat': 0.1540228, 'lng': 37.8964921}}, {'annotations': {'DMS': {'lat': "0° 47' 22.88544'' N", 'lng': "35° 20' 46.54464'' E"}, 'MGRS': '36MYE6112912641', 'Maidenhead': 'KI79qf10nl', 'Mercator': {'x': 3934727.932, 'y': -87322.246}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?way=542832856#map=16/-0.78969/35.34626', 'note_url': 'https://www.openstreetmap.org/note/new#map=16/-0.78969/35.34626&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=-0.78969&mlon=35.34626#map=16/-0.78969/35.34626'}, 'UN_M49': {'regions': {'AFRICA': '002', 'EASTERN_AFRICA': '014', 'KE': '404', 'SUB-SAHARAN_AFRICA': '202', 'WORLD': '001'}, 'statistical_groupings': ['LEDC']}, 'callingcode': 254, 'currency': {'alternate_symbols': ['Sh'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'KES', 'iso_numeric': '404', 'name': 'Kenyan Shilling', 'smallest_denomination': 50, 'subunit': 'Cent', 'subunit_to_unit': 100, 'symbol': 'KSh', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇰🇪', 'geohash': 'kzc5s24rex5922ycsuv9', 'qibla': 10.89, 'roadinfo': {'drive_on': 'left', 'road': 'Kamandura Mai-Mahiu Narok Rd, Bomet, Kenya', 'road_type': 'primary', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1675136880, 'astronomical': 1675132560, 'civil': 1675135620, 'nautical': 1675134120}, 'set': {'apparent': 1675180500, 'astronomical': 1675184820, 'civil': 1675181820, 'nautical': 1675183320}}, 'timezone': {'name': 'Africa/Nairobi', 'now_in_dst': 0, 'offset_sec': 10800, 'offset_string': '+0300', 'short_name': 'EAT'}, 'what3words': {'words': 'highly.grilling.diet'}}, 'bounds': {'northeast': {'lat': -0.7896904, 'lng': 35.3463449}, 'southwest': {'lat': -0.789836, 'lng': 35.3462624}}, 'components': {'ISO_3166-1_alpha-2': 'KE', 'ISO_3166-1_alpha-3': 'KEN', 'ISO_3166-2': ['KE-02'], '_category': 'road', '_type': 'road', 'continent': 'Africa', 'country': 'Kenya', 'country_code': 'ke', 'road': 'Kamandura Mai-Mahiu Narok Rd, Bomet, Kenya', 'road_type': 'primary', 'state': 'Bomet', 'town': 'Bomet'}, 'confidence': 9, 'formatted': 'Kamandura Mai-Mahiu Narok Rd, Bomet, Kenya, Bomet, Kenya', 'geometry': {'lat': -0.7896904, 'lng': 35.3462624}}, {'annotations': {'DMS': {'lat': "1° 19' 43.91076'' S", 'lng': "36° 43' 6.97908'' E"}, 'MGRS': '37MBU4613853003', 'Maidenhead': 'KI88iq61fb', 'Mercator': {'x': 4087496.445, 'y': -146951.537}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?node=5356825011#map=16/-1.32886/36.71861', 'note_url': 'https://www.openstreetmap.org/note/new#map=16/-1.32886/36.71861&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=-1.32886&mlon=36.71861#map=16/-1.32886/36.71861'}, 'UN_M49': {'regions': {'AFRICA': '002', 'EASTERN_AFRICA': '014', 'KE': '404', 'SUB-SAHARAN_AFRICA': '202', 'WORLD': '001'}, 'statistical_groupings': ['LEDC']}, 'callingcode': 254, 'currency': {'alternate_symbols': ['Sh'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'KES', 'iso_numeric': '404', 'name': 'Kenyan Shilling', 'smallest_denomination': 50, 'subunit': 'Cent', 'subunit_to_unit': 100, 'symbol': 'KSh', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇰🇪', 'geohash': 'kzf07w1dv9b8cecrwc49', 'qibla': 7.44, 'roadinfo': {'drive_on': 'left', 'road': 'Karen Plains Road', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1675136520, 'astronomical': 1675132200, 'civil': 1675135260, 'nautical': 1675133700}, 'set': {'apparent': 1675180260, 'astronomical': 1675184580, 'civil': 1675181520, 'nautical': 1675183020}}, 'timezone': {'name': 'Africa/Nairobi', 'now_in_dst': 0, 'offset_sec': 10800, 'offset_string': '+0300', 'short_name': 'EAT'}, 'what3words': {'words': 'revise.dramatic.unicorns'}}, 'bounds': {'northeast': {'lat': -1.3288141, 'lng': 36.7186553}, 'southwest': {'lat': -1.3289141, 'lng': 36.7185553}}, 'components': {'ISO_3166-1_alpha-2': 'KE', 'ISO_3166-1_alpha-3': 'KEN', 'ISO_3166-2': ['KE-30'], '_category': 'place_of_worship', '_type': 'place_of_worship', 'city': 'Nairobi', 'continent': 'Africa', 'country': 'Kenya', 'country_code': 'ke', 'house_number': '1509, Karen Rd, Nairobi', 'place_of_worship': 'Calvary Chapel Nairobi, Kenya', 'postcode': '00505', 'road': 'Karen Plains Road', 'state': 'Nairobi County', 'suburb': 'Karen'}, 'confidence': 9, 'formatted': 'Calvary Chapel Nairobi, Kenya, 1509, Karen Rd, Nairobi Karen Plains Road, Nairobi, 00505, Kenya', 'geometry': {'lat': -1.3288641, 'lng': 36.7186053}}, {'annotations': {'DMS': {'lat': "1° 14' 9.47076'' S", 'lng': "36° 45' 59.58000'' E"}, 'MGRS': '37MBU5146763284', 'Maidenhead': 'KI88js13xi', 'Mercator': {'x': 4092833.624, 'y': -136676.578}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?node=7686965507#map=16/-1.23596/36.76655', 'note_url': 'https://www.openstreetmap.org/note/new#map=16/-1.23596/36.76655&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=-1.23596&mlon=36.76655#map=16/-1.23596/36.76655'}, 'UN_M49': {'regions': {'AFRICA': '002', 'EASTERN_AFRICA': '014', 'KE': '404', 'SUB-SAHARAN_AFRICA': '202', 'WORLD': '001'}, 'statistical_groupings': ['LEDC']}, 'callingcode': 254, 'currency': {'alternate_symbols': ['Sh'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'KES', 'iso_numeric': '404', 'name': 'Kenyan Shilling', 'smallest_denomination': 50, 'subunit': 'Cent', 'subunit_to_unit': 100, 'symbol': 'KSh', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇰🇪', 'geohash': 'kzf0uwuxfxwdywsz2jt6', 'qibla': 7.35, 'roadinfo': {'drive_on': 'left', 'road': 'Ngecha Road', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1675136520, 'astronomical': 1675132200, 'civil': 1675135260, 'nautical': 1675133700}, 'set': {'apparent': 1675180200, 'astronomical': 1675184520, 'civil': 1675181520, 'nautical': 1675183020}}, 'timezone': {'name': 'Africa/Nairobi', 'now_in_dst': 0, 'offset_sec': 10800, 'offset_string': '+0300', 'short_name': 'EAT'}, 'what3words': {'words': 'joyously.overhear.voices'}}, 'bounds': {'northeast': {'lat': -1.2359141, 'lng': 36.7666}, 'southwest': {'lat': -1.2360141, 'lng': 36.7665}}, 'components': {'ISO_3166-1_alpha-2': 'KE', 'ISO_3166-1_alpha-3': 'KEN', 'ISO_3166-2': ['KE-30'], '_category': 'travel/tourism', '_type': 'hotel', 'city': 'Nairobi', 'continent': 'Africa', 'country': 'Kenya', 'country_code': 'ke', 'hotel': 'Sandalwood Kitisuru, Nairobi, Kenya', 'postcode': '11403', 'road': 'Ngecha Road', 'state': 'Nairobi County'}, 'confidence': 9, 'formatted': 'Sandalwood Kitisuru, Nairobi, Kenya, Ngecha Road, Nairobi, 11403, Kenya', 'geometry': {'lat': -1.2359641, 'lng': 36.76655}}, {'annotations': {'DMS': {'lat': "1° 20' 6.87552'' S", 'lng': "36° 42' 8.92332'' E"}, 'MGRS': '37MBU4434352295', 'Maidenhead': 'KI88ip49hn', 'Mercator': {'x': 4085701.24, 'y': -147657.095}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?node=5356849304#map=16/-1.33524/36.70248', 'note_url': 'https://www.openstreetmap.org/note/new#map=16/-1.33524/36.70248&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=-1.33524&mlon=36.70248#map=16/-1.33524/36.70248'}, 'UN_M49': {'regions': {'AFRICA': '002', 'EASTERN_AFRICA': '014', 'KE': '404', 'SUB-SAHARAN_AFRICA': '202', 'WORLD': '001'}, 'statistical_groupings': ['LEDC']}, 'callingcode': 254, 'currency': {'alternate_symbols': ['Sh'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'KES', 'iso_numeric': '404', 'name': 'Kenyan Shilling', 'smallest_denomination': 50, 'subunit': 'Cent', 'subunit_to_unit': 100, 'symbol': 'KSh', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇰🇪', 'geohash': 'kzf07hvvtsxsjcunq3ng', 'qibla': 7.47, 'roadinfo': {'drive_on': 'left', 'road': 'Acacia Drive', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1675136520, 'astronomical': 1675132200, 'civil': 1675135260, 'nautical': 1675133760}, 'set': {'apparent': 1675180260, 'astronomical': 1675184580, 'civil': 1675181520, 'nautical': 1675183080}}, 'timezone': {'name': 'Africa/Nairobi', 'now_in_dst': 0, 'offset_sec': 10800, 'offset_string': '+0300', 'short_name': 'EAT'}, 'what3words': {'words': 'darker.irrigate.kitchen'}}, 'bounds': {'northeast': {'lat': -1.3351932, 'lng': 36.7025287}, 'southwest': {'lat': -1.3352932, 'lng': 36.7024287}}, 'components': {'ISO_3166-1_alpha-2': 'KE', 'ISO_3166-1_alpha-3': 'KEN', 'ISO_3166-2': ['KE-30'], '_category': 'travel/tourism', '_type': 'hotel', 'city': 'Nairobi', 'continent': 'Africa', 'country': 'Kenya', 'country_code': 'ke', 'hotel': 'Karen Camp', 'house_number': 'Acacia Drive off Marula Lane, Off Karen Road, Nairobi, Kenya, Nairobi', 'road': 'Acacia Drive', 'state': 'Nairobi County', 'suburb': 'Karen'}, 'confidence': 9, 'formatted': 'Karen Camp, Acacia Drive off Marula Lane, Off Karen Road, Nairobi, Kenya, Nairobi Acacia Drive, Nairobi, Kenya', 'geometry': {'lat': -1.3352432, 'lng': 36.7024787}}, {'annotations': {'DMS': {'lat': "0° 41' 21.95412'' N", 'lng': "34° 46' 35.63940'' E"}, 'MGRS': '36MXE9770523760', 'Maidenhead': 'KI79jh34em', 'Mercator': {'x': 3871309.674, 'y': -76235.275}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?node=6102845270#map=16/-0.68943/34.77657', 'note_url': 'https://www.openstreetmap.org/note/new#map=16/-0.68943/34.77657&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=-0.68943&mlon=34.77657#map=16/-0.68943/34.77657'}, 'UN_M49': {'regions': {'AFRICA': '002', 'EASTERN_AFRICA': '014', 'KE': '404', 'SUB-SAHARAN_AFRICA': '202', 'WORLD': '001'}, 'statistical_groupings': ['LEDC']}, 'callingcode': 254, 'currency': {'alternate_symbols': ['Sh'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'KES', 'iso_numeric': '404', 'name': 'Kenyan Shilling', 'smallest_denomination': 50, 'subunit': 'Cent', 'subunit_to_unit': 100, 'symbol': 'KSh', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇰🇪', 'geohash': 'kzbsp67xb8x7wyctrhbj', 'qibla': 12.28, 'roadinfo': {'drive_on': 'left', 'road': 'Kisii-Kilgoris Road', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1675137060, 'astronomical': 1675132740, 'civil': 1675135740, 'nautical': 1675134240}, 'set': {'apparent': 1675180680, 'astronomical': 1675185000, 'civil': 1675181940, 'nautical': 1675183440}}, 'timezone': {'name': 'Africa/Nairobi', 'now_in_dst': 0, 'offset_sec': 10800, 'offset_string': '+0300', 'short_name': 'EAT'}, 'what3words': {'words': 'landscape.driveways.dampen'}}, 'bounds': {'northeast': {'lat': -0.6893817, 'lng': 34.7766165}, 'southwest': {'lat': -0.6894817, 'lng': 34.7765165}}, 'components': {'ISO_3166-1_alpha-2': 'KE', 'ISO_3166-1_alpha-3': 'KEN', 'ISO_3166-2': ['KE-16'], '_category': 'travel/tourism', '_type': 'hotel', 'city': 'Kisii', 'continent': 'Africa', 'country': 'Kenya', 'country_code': 'ke', 'hotel': 'Hotspot II Lounge, Kisii, Kenya', 'postcode': '40200', 'region': 'Nyanza', 'road': 'Kisii-Kilgoris Road', 'state': 'Kisii County'}, 'confidence': 9, 'formatted': 'Hotspot II Lounge, Kisii, Kenya, Kisii-Kilgoris Road, Kisii, 40200, Kenya', 'geometry': {'lat': -0.6894317, 'lng': 34.7765665}}, {'annotations': {'DMS': {'lat': "0° 29' 23.72820'' N", 'lng': "36° 58' 6.31992'' E"}, 'MGRS': '37MBV7389645814', 'Maidenhead': 'KI89lm62fk', 'Mercator': {'x': 4115305.935, 'y': -54173.716}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?node=4578372181#map=16/-0.48992/36.96842', 'note_url': 'https://www.openstreetmap.org/note/new#map=16/-0.48992/36.96842&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=-0.48992&mlon=36.96842#map=16/-0.48992/36.96842'}, 'UN_M49': {'regions': {'AFRICA': '002', 'EASTERN_AFRICA': '014', 'KE': '404', 'SUB-SAHARAN_AFRICA': '202', 'WORLD': '001'}, 'statistical_groupings': ['LEDC']}, 'callingcode': 254, 'currency': {'alternate_symbols': ['Sh'], 'decimal_mark': '.', 'html_entity': '', 'iso_code': 'KES', 'iso_numeric': '404', 'name': 'Kenyan Shilling', 'smallest_denomination': 50, 'subunit': 'Cent', 'subunit_to_unit': 100, 'symbol': 'KSh', 'symbol_first': 1, 'thousands_separator': ','}, 'flag': '🇰🇪', 'geohash': 'kzfm1nz9fxmw8bwvk62b', 'qibla': 7.09, 'roadinfo': {'drive_on': 'left', 'road': 'D432', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1675136520, 'astronomical': 1675132200, 'civil': 1675135260, 'nautical': 1675133760}, 'set': {'apparent': 1675180140, 'astronomical': 1675184460, 'civil': 1675181400, 'nautical': 1675182900}}, 'timezone': {'name': 'Africa/Nairobi', 'now_in_dst': 0, 'offset_sec': 10800, 'offset_string': '+0300', 'short_name': 'EAT'}, 'what3words': {'words': 'challenge.infuse.indulging'}}, 'bounds': {'northeast': {'lat': -0.4898745, 'lng': 36.9684722}, 'southwest': {'lat': -0.4899745, 'lng': 36.9683722}}, 'components': {'ISO_3166-1_alpha-2': 'KE', 'ISO_3166-1_alpha-3': 'KEN', 'ISO_3166-2': ['KE-36'], '_category': 'education', '_type': 'school', 'continent': 'Africa', 'country': 'Kenya', 'country_code': 'ke', 'road': 'D432', 'school': 'Kiandu Primary School, Kenya', 'state': 'Nyeri', 'town': 'Wamagana'}, 'confidence': 9, 'formatted': 'Kiandu Primary School, Kenya, D432, Wamagana, Kenya', 'geometry': {'lat': -0.4899245, 'lng': 36.9684222}}]
1.4419683 38.4313975

```

**Map output according to google maps.**
![image](https://user-images.githubusercontent.com/6685756/215794549-51d7903e-e944-4a29-848e-4da1d6695c1e.png)

**Map output according to open maps**
![image](https://user-images.githubusercontent.com/6685756/215795179-822c88df-46c7-41aa-88e2-8867c7ab2e7e.png)

---

### NLP 

#After installing nltk package download the packages required for
#this book using the code below.

```
import nltk
nltk.download()

```
Code below tells the interpreter to load all items from  NLTK book
`from nltk.book import *`

### Comon_context.py
**Code:**

```Python
#The term common_contexts allows us to examine just the contexts that are shared by
#two or more words, such as monstrous and very. We have to enclose these words by
#square brackets as well as parentheses, and separate them with a comma:

from nltk.book import*

print("  ")
print("Common Contexts")
text2.common_contexts(["monstrous","very"])

print ("Common contexts for nation, terror and god")
text4.common_contexts(["nation","terror","god"])

```
This code uses the Natural Language Toolkit (nltk) library in Python to find the common contexts between two or more words in a text. It imports two texts, "text2" and "text4" from the "nltk.book" corpus.

The first call to the "common_contexts" method finds the common contexts between the words "monstrous" and "very" in "text2". The second call finds the common contexts between the words "nation", "terror", and "god" in "text4". The results are displayed in the output.

---

### Count_Vocabulary.py
**Code:**
```python 
#count the words in a text in a variety of useful ways
# len is used to  length of a text from start to finish, in terms of the words
#and punctuation symbols that appear.
from nltk.book import *
print ("the number of words in Genesis is :")
l= len(text3)
print(l)

```
This code uses the Natural Language Toolkit (nltk) library in Python to count the number of words in the text "text3" from the "nltk.book" corpus.

The built-in "len" function is used to calculate the length of the text, which is the number of tokens (words and punctuation symbols) in the text. The result is stored in the variable "l" and then printed. This way, you can easily obtain the total number of words in a given text.

---

### Find_Text.py
**Code:**
```python
# this code finds out texts in text1
from nltk.book import *

print ("  ")
print ("==== Print texts from text1 =====")
print (text1)
print ("==== Print texts from text2 =====")
print (text2)

```

This code uses the Natural Language Toolkit (nltk) library in Python to print the texts "text1" and "text2" from the "nltk.book" corpus.

The code prints the contents of each text by referencing the variable containing the text. The first print statement outputs "text1" and the second print statement outputs "text2". This way, you can view the full contents of a text and examine it for further analysis.

---

### Search_Text.py
**Code:**
```python
# this code is used for searching texts 
# here we search the words monstrous in Moby Dick
# search for the words
#Sense and Sensibility for the word affection, using text2.concord
#ance("affection"). Search the book of Genesis to find out how long
#some people lived, using: text3.concordance("lived"). You could look
#at text4, the Inaugural Address Corpus, to see examples of English going
#back to 1789, and search for words like nation, terror,god
# concordance permits us to see words in context

from nltk.book import *
print ("   ")
print ("--- Search monstrous in Moby Dick ----!")
text1.concordance("monstrous")
print ("   ")
print ("--- Search affection in Sense and Sensibility using text2 ----!")
text2.concordance("affection")
print ("   ")
print ("--- Search lived in the book Genesis using text3 ----!")
text3.concordance("lived")
print ("   ")
print ("--- Search for nation,terror and god in the Inaugural Address Corpus using text4 ----!")
text4.concordance("nation")
text4.concordance("terror")
text4.concordance("god")

print (                         "===== end of example1 =====")

```
This code uses the Natural Language Toolkit (nltk) library in Python to search for specific words in texts from the "nltk.book" corpus.
The "concordance" method is used to search for specific words in the texts. The first call to the "concordance" method searches for the word "monstrous" in "text1", the second call searches for the word "affection" in "text2", the third call searches for the word "lived" in "text3", and the fourth set of calls searches for the words "nation", "terror", and "god" in "text4". The results display the word in context, showing the words surrounding the searched term in the text. This way, you can understand how the searched word is used in the text and get an idea of its context.

---

### Search_similar_Text.py
**Code:**
```python
#search for words that appear in a similar range of contexts
#by appending the term similar
#We can find out by appending the term
#then inserting the relevant word in parentheses
from nltk.book import*

print("  ")
print("Print similar range of words from text1")
text1.similar("monstrous")

print("  ")
print("Print similar range of words from text2")
text2.similar("monstrous")

```
This code uses the Natural Language Toolkit (nltk) library in Python to search for words that appear in a similar range of contexts as a specific word in two texts from the "nltk.book" corpus.

The "similar" method is used to search for words that appear in a similar range of contexts as the word specified in parentheses. The first call to the "similar" method searches for similar words to "monstrous" in "text1" and the second call searches for similar words in "text2". The results show a list of words that appear in a similar context as the searched word in the given text. This way, you can find words that are semantically related to the word you are searching for.

---

### cal_func_lexical.py
**Code:**
```python
# create a function lexical_diversity and another one for percentage
from nltk.book import *
import math 

def lexical_diversity(text):
    return len(text)/len(set(text))
    
    
def percentage(count,total):
    return 100*count/total
    
print ( lexical_diversity(text3))
print (lexical_diversity(text5))
print (percentage(4, 5))
print ( percentage(text4.count('a'), len(text4)))

```
This code defines two functions in Python using the Natural Language Toolkit (nltk) library. The first function, "lexical_diversity", takes a text as input and returns the lexical diversity score, which is the ratio of the number of tokens (words and punctuation) in the text to the number of unique tokens.

The second function, "percentage", calculates the percentage of a specific count relative to a total. The input parameters are the count and the total.

At the end, the code calls each function with different inputs and prints the results. The first call to "lexical_diversity" calculates the lexical diversity score for "text3". The second call calculates the lexical diversity score for "text5". The first call to "percentage" calculates the percentage of 4 out of 5, and the second call calculates the percentage of the word 'a' in "text4".

---

###
**Code:**
```Python
#calculate a measure of the lexical richness of the text. The next example
#shows us that each word is used 16 times on average
from nltk.book import *
import math 
lex = len(text3)/len(set(text3))
print ("  ")
print ("Average use of each word is: ")
print(lex)
print(" ")
print ("Word Count is : ")
lex2 = text3.count("smote")
print(lex2)
print(" ")
print("The percentage of the text from the word is: ")
lex3 =100 * text4.count("a")/len(text4)
print(lex3) 

print(" ")
print ("Word Count is : ")
lex4 = text5.count("lol")
print(lex4)
print(" ")
print("The percentage of the text from the word is: ")
lex5 =100 * text4.count("a")/len(text5)
print(lex5) 


```
**Output**

```Python 

  
Average use of each word is: 
16.050197203298673

Word Count is : 
25

The percentage of the text from the word is: 
1.0456414859557087

Word Count is : 
704

The percentage of the text from the word is: 
0.015640968673628082

```
---

```python 
#This code is for generating random texts
from nltk.book import *
text3.generate()

```
The generate() method is not available for the nltk Text object. If you want to generate random text, you can use other methods such as generating random sequences of words, using the random module and various language model techniques such as Markov models or n-grams.

### sorted.py
**Code:**
```python
# the python function set() can be used to obtain vocabularies
#By wrapping sorted() around the Python expression set(text3) , we obtain a sorted
#list of vocabulary items, beginning with various punctuation symbols and continuing
#with words starting with A. All capitalized words precede lowercase words. We dis-
#cover the size of the vocabulary indirectly, by asking for the number of items in the set,
#and again we can use len to obtain this number . Although it has 44,764 tokens, this
#book has only 2,789 distinct words, or “word types.”

from nltk.book import *
print ("Sorted text are :")
s=sorted(set(text3))
print(s)

print ("the number of vocabularies in the set is: ")
l=len(set(text3))
print(l)

```
Sorted text are:

```python
['!', "'", '(', ')', ',', ',)', '.', '.)', ':', ';', ';)', '?', '?)', 'A', 'Abel', 'Abelmizraim', 'Abidah', 'Abide', 'Abimael', 'Abimelech', 'Abr', 'Abrah', 'Abraham', 'Abram', 'Accad', 'Achamoth', 'Adah', 'Adam', 'Adbeel', 'Admah', 'Adoi', 'Adonai', 'Adonijah', 'Adullam', 'Afek', 'Aglah', 'Ahab', 'Ahaz', 'Ahban', 'Ai', 'Aijeleth', 'Ain', 'Akeldama', 'Akrabbim', 'Alameth', 'All', 'Alvan', 'Am', 'Amariah', 'Amaziah', 'Ambassador', 'Ammihud', 'Amon', 'Amram', 'Amraphel', 'Anaharath', 'Anammelech', 'Ananiah', 'And', 'Andreas', 'Angel', 'Anger', 'Aniam', 'Anipal', 'Anselm', 'Antichrist', 'Antipas', 'Antipatris', 'Aphrah', 'Apollyon', 'Apostle', 'Ar', 'Ararat', 'Araunah', 'Areli', 'Areliah', 'Arnon', 'Arodi', 'Arodite', 'Aron', 'Asa', 'Asaph', 'Ashan', 'Ashdod', 'Ashdothpisgah', 'Asher', 'Ashkelon', 'Ashpenaz', 'Ashur', 'Asia', 'Asshur', 'Assir', '


```

---

### comprehensions.py
**Code:**

```python
Using range function:
nines = [x for x in range(100) if x%9 == 0]
print(nines)
x_values = [i for i in range(12)]
print('code uses a list comprehension to generate the list of x values that\n' 
      'satisfy the equation 9x = [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99].',x_values)


```
code will generate the list of x values that satisfy the equation 9x = [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99] using a list comprehension with the range() function. The first print statement prints the list of nines which contains all the values of x between 0 and 99 that are divisible by 9. The second print statement prints a string that describes the code, followed by the list of x values that satisfy the equation 9x = [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99].

---

###  Mapping.ipynb
**Code:**

```python 
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
# set the filepath and load
fp = "District_Boundary.shp"
#reading the file stored in variable fp
map_df = gpd.read_file(fp)
# check data type so we can see that this is not a normal dataframe, but a GEOdataframe
map_df.head()
#plotting the map of the shape file preview of the maps without data in it
map_df.plot()

```
**Output**
[Mappint.ipynb](https://github.com/mngugi/Python_Programming-/blob/master/Mapping.ipynb)


This code uses the Python packages pandas, matplotlib, and geopandas to read and plot a shapefile containing district boundaries. Here is a step-by-step explanation of what the code does:

    The first three lines of code import the necessary packages: pandas, matplotlib, and geopandas.
    The next line sets the variable fp to the filepath of the shapefile we want to read.
    The following line reads the shapefile into a GeoDataFrame and stores it in the variable map_df.
    The head() method is then called on map_df to show the first few rows of data in the GeoDataFrame. This is optional and only serves to provide a preview of the data.
    Finally, the plot() method is called on map_df to plot the district boundaries on a map. This will show a preview of the map without any data on it.

Note that to see the plot, you may need to call the show() method of plt, like so:

`plt.show()`

Also note that the code assumes that the shapefile exists in the specified filepath and is properly formatted. If the shapefile is not found or is not in the correct format, the code will raise an error.

---

### Python_Widgets.ipynb

```python 
import ipywidgets as widgets

ignition = widgets.ToggleButton(
    value=False,
    description='Start Engine',
    button_style='success',
    tooltip='Engage your Engine',
    icon='rocket'
)

speed_slider = widgets.IntSlider(
    value=0,
    min=0,
    max=100,
    step=1,
    description='Speed:',
    orientation='horizontal',
    readout=True,
    readout_format='d'
)

output = widgets.Output()

display(ignition, speed_slider, output)

def on_value_change(change):
    with output:
        if change['new'] == True:
            print("Engine started at speed", speed_slider.value)
        else:   
            print("Engine stopped")

ignition.observe(on_value_change, names='value')

```
This creates an integer slider widget that allows you to select a value between 0 and 100, representing the speed of the engine. You can add this widget to the existing code by placing it after the ignition widget, and then updating the on_value_change function to use the speed_slider value when the engine is started.This code will now print out the speed value selected on the speed_slider widget when the engine is started.

---

### ExceptionsRecap.py
**Code:**

```Python 
# a python trying to access the third element in the array
# expected error message is IndexError: list index out of range

try:
    items_array = ['a', 'b']
    third = items_array[3]
    
    print("Out of the index range")
    print(third) 
except Exception:
    print('Fix the error and continue anyway')
   

# a python program type ZeroDivisionError
try:
    j = 4
    i = j/0
    print("Not mathematically acceptable")

except IndexError:
    print ("Error 2")


students = [('Timmy', 95, 'Will pass'), ('Martha', 70), ('Betty', 82, 'Will pass'), ('Stewart', 50, 'Will not pass'), ('Ashley', 68), ('Natalie', 99, 'Will pass'), ('Archie', 71), ('Carl', 45, 'Will not pass')]

passing = {'Will pass': 0, 'Will not pass': 0}
for tup in students:
    try:
        if tup[2] == 'Will pass':
            passing['Will pass'] += 1
        elif tup[2] == 'Will not pass':
            passing['Will not pass'] += 1
    except IndexError:   
        pass


nums = [5, 9, '4', 3, 2, 1, 6, 5, '7', 4, 3, 2, 6, 7, 8, '0', 3, 4, 0, 6, 5, '3', 5, 6, 7, 8, '3', '1', 5, 6, 7, 9, 3, 2, 5, 6, '9', 2, 3, 4, 5, 1]

plus_four = []

for num in nums:
    try:
        plus_four.append(num+4)
    except TypeError:
        plus_four.append('Error')


```
In the first block of code, the items_array has only two elements. Trying to access the third element (at index 3) will result in an IndexError, not the expected message "Out of the index range". Also, the print(third) statement will never be executed because the IndexError will cause the program to jump directly to the except block. To print the error message, you can modify the except block as follows:

```python

except IndexError as e:
    print('Error:', e)
    print('Fix the error and continue anyway')
```
This will print the error message generated by the IndexError, which will be "list index out of range".

In the second block of code, dividing a number by zero will result in a ZeroDivisionError, not the expected message "Not mathematically acceptable". To print the error message, you can modify the except block as follows:

```python

except ZeroDivisionError as e:
    print('Error:', e)
    print('Fix the error and continue anyway')
```
This will print the error message generated by the ZeroDivisionError, which will be "division by zero".

In the third block of code, some tuples in the students list have only two elements, so trying to access the third element (at index 2) will result in an IndexError. However, the except block will simply pass, which means that the program will not handle the error in any way. To handle the error, you can modify the except block as follows:

```python

except IndexError:
    print('Error: Tuple has no third element')
```
This will print a message indicating that a tuple has no third element.

In the fourth block of code, some elements in the nums list are strings, so trying to add them to an integer will result in a TypeError. However, the except block simply appends the string 'Error' to the plus_four list. To handle the error, you can modify the except block as follows:

```python

except TypeError:
    print('Error: Element is not a number')
    plus_four.append('Error')
```

This will print a message indicating that an element is not a number, and will also append the string 'Error' to the plus_four list.

---
### JsonRecap.py
**Code:**
```python 
# python program that gets data from Apples iTunes

import json

aString = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(aString)
d = json.loads(aString)
print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])


def objects(obj):
    return json.dumps(obj,sort_keys=True, indent=2)
j =  {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}
print(j)
print(objects(j))
```

---


```python 
import json

aString = '{"resultCount":25,"results":[{"wrapperType":"track","kind":"podcast","collectionId":10892}]}'
print(aString)

try:
    d = json.loads(aString)
except json.JSONDecodeError as e:
    print(f"Error: {e}")

print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])


def objects(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

j = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2': {'b': 3, 'c': "yes"}}
print(j)
print(objects(j))

```
Python program that uses the json library to parse and manipulate JSON data. Specifically, it defines a JSON string aString, loads it into a dictionary d using the json.loads() function, and prints some information about d. It also defines a function objects() that converts a Python object into a JSON string with pretty formatting.

Here's a brief explanation of what the program does:

The program starts by importing the json library, which provides functions for encoding and decoding JSON data.

The program defines a JSON string aString that contains information about a search result on Apple's iTunes platform. This string is printed to the console using the print() function.

The program uses the json.loads() function to parse the JSON string aString into a Python dictionary d. The try/except block is used to handle any errors that may occur during the parsing process, such as if the JSON string is not valid. If an error occurs, the error message is printed to the console.

The program prints some information about the parsed dictionary d, including its type, keys, and the value associated with the resultCount key.

The program defines a function objects() that takes a Python object as input, converts it to a JSON string using the json.dumps() function with pretty formatting options, and returns the resulting string.

The program creates a Python dictionary j and prints it to the console using the print() function. It then calls the objects() function with the j dictionary as input and prints the resulting JSON string to the console.

Overall, the program demonstrates how to use the json library to parse and manipulate JSON data in Python.

---
### NestedRecap.ipynb

**Code**
```python
# a python program the prints  nested lists of twoWheels, fourWheels and sixWheels Vehicles


twoWheels = ['Honda', 'Kawasaki', 'Yamaha']
fourWheels = ['Toyota', 'Nissan','Ford']
sixWheels = ['Isuzu','Scania','Actross']

# Nested all the three lists of Automobiles

nestedAutoMobiles = [['Honda', 'Kawasaki', 'Yamaha'],['Toyota', 'Nissan','Ford'],['Isuzu','Scania','Actross'] ]
nestedAutoMobiles[0].append('TVS')
nestedAutoMobiles[1].append('Peugot')
nestedAutoMobiles[2].append('Mitsubishi-Fuso')

print(nestedAutoMobiles[0])
print (len(nestedAutoMobiles[1]))

#twoWheels.append(['TVS'])
nestedAutoMobiles.append(['tenWheelers'])

print ('---------')
for i in twoWheels:
    print(i)

print('-----------')

for j in nestedAutoMobiles:
    print(j)

print('-----------')

info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }


print(info)

```

```python 
twoWheels = ['Honda', 'Kawasaki', 'Yamaha']
fourWheels = ['Toyota', 'Nissan', 'Ford']
sixWheels = ['Isuzu', 'Scania', 'Actross']

# Create a nested list that contains the three lists of vehicles
nestedAutoMobiles = [twoWheels, fourWheels, sixWheels]

# Append new items to each list
nestedAutoMobiles[0].append('TVS')
nestedAutoMobiles[1].append('Peugeot')
nestedAutoMobiles[2].append('Mitsubishi-Fuso')

# Add a new list of vehicles to the nested list
nestedAutoMobiles.append(['tenWheelers'])

# Print each list separately
print(nestedAutoMobiles[0])
print(nestedAutoMobiles[1])
print(nestedAutoMobiles[2])
print(nestedAutoMobiles[3])

# Print each item in the twoWheels list separately
for item in twoWheels:
    print(item)

# Print each nested list separately
for sublist in nestedAutoMobiles:
    print(sublist)

# Access nested data in a dictionary
print(info['personal_data']['name'])
print(info['personal_data']['physical_features']['color']['hair'])
print(info['other']['favorite_colors'][1])

```
The program already prints the nested lists of twoWheels, fourWheels and sixWheels vehicles. Note that the info dictionary at the end is unrelated to the previous code and was not used. It just shows an example of how to access nested data in a dictionary.

---
### flowcharts.ipynb
**Code**
```python
import PySimpleGUI as sg

# Define the layout of the window
layout = [
    [sg.Graph((800, 600), (0, 0), (800, 600), background_color='white', key='graph')],
    [sg.Button('Exit')]
]

# Create the window
window = sg.Window('My Flowchart', layout)

# Define the flowchart elements
elements = {
    'Start': (100, 500),
    'Process 1': (100, 400),
    'Process 2': (100, 300),
    'Decision': (300, 300),
    'Process 3': (500, 300),
    'End': (700, 500)
}

# Define the connections between the elements
connections = [
    ('Start', 'Process 1'),
    ('Process 1', 'Process 2'),
    ('Process 2', 'Decision'),
    ('Decision', 'Process 3', 'yes'),  # This connection has a label of 'yes'
    ('Decision', 'End', 'no'),
    ('Process 3', 'End')
]

# Start the event loop
while True:
    event, values = window.read()

    # Exit the program if the window is closed or the Exit button is clicked
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break

    # Get the graph object and clear it
    graph = window['graph']
    graph.erase()

    # Draw the elements of the flowchart
    for element, position in elements.items():
        graph.draw_text(element, position, font='Arial 12')
        graph.draw_rectangle((position[0] - 50, position[1] - 20), (position[0] + 50, position[1] + 20))

    # Draw the connections between the elements
    for connection in connections:
        start = elements[connection[0]]
        for i in range(1, len(connection)):
            end = elements[connection[i]]
            graph.draw_line(start, end)
            if i < len(connection) - 1:
                graph.draw_text(connection[i], ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2), font='Arial 12')
            start = end

# Close the window
window.close()

```
This code creates a PySimpleGUI window with a graph element and an Exit button. It also defines the elements and connections of the flowchart. The event loop reads events from the window and redraws the flowchart every time an event occurs. The flowchart is drawn by iterating over the elements and connections and using the graph object to draw rectangles, text, and lines. Finally, the window is closed when the event loop is exited.

---
### IndexPositions.py
**Code:**

```python
nums = [2, 7, 11, 15, 9]
nums2 = [1, 2, 3, 4, 6,5]

# Find the target value by adding the first elements of both lists
target = nums[0] + nums2[2]
print("Target value:", target)

# Check if the target value is present in the nums list
if target not in nums:
    print("Target value not found in nums")
else:
    # Find the index position of the target value in the nums list
    index = nums.index(target)
    print("Index position of target value:", index)

    # Iterate over all pairs of elements in the nums list
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # Check if the sum of the pair is equal to the target value
            if nums[i] + nums[j] == target:
                # Print the index positions of the pair
                print("Index positions of pair:", i, j)
```

This code finds the index positions of two elements in a list whose sum equals a target value.

The code first defines two lists, nums and nums2, and then calculates the target value by adding the first element of nums and the third element of nums2. It then checks if the target value is present in the nums list. If it is not, it prints a message indicating that the target value was not found. If it is present, the code finds the index position of the target value in the nums list and prints it.

The code then iterates over all pairs of elements in the nums list and checks if the sum of the pair is equal to the target value. If it is, the code prints the index positions of the pair.

Note that this code assumes that there is only one pair of elements whose sum equals the target value. If there are multiple pairs, this code will only find the first one it encounters.

---

### menutests.py
**Code**

```python
class MyClass1:
    def __init__(self):
        print("This is MyClass1")

class MyClass2:
    def __init__(self):
        print("This is MyClass2")
        

def main():
    while True:
        print("1. Class 1")
        print("2. Class 2")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            my_class = MyClass1()
        elif choice == '2':
            my_class = MyClass2()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()

```
This code defines two classes, MyClass1 and MyClass2, each with an __init__ method that simply prints a message to the console.

The main function presents the user with a menu of three choices:

    Choosing "1" creates an instance of MyClass1 and prints "This is MyClass1".
    Choosing "2" creates an instance of MyClass2 and prints "This is MyClass2".
    Choosing "3" quits the program.

The program loops until the user chooses to quit. If the user enters an invalid choice, the program prints "Invalid choice. Try again." and displays the menu again.

The if __name__ == '__main__': statement at the bottom of the code ensures that the main function is only called when the code is run as a script, and not when it is imported as a module.

---

### unpackingOperator.py
**Code:**

```python
a = {1,2,3,4}
b = {1,3,5,6}

c, *d, e = a | b

print(d)

# a python program that adds two number lists in reverser order 

l1 = [2,4,3]
l2 = [5,6,4]

# reverse the list

l1.reverse()
l2.reverse()


#result = [l1[i]+l2[i] for i in range(len(l1))]
result = [x+y for x,y in zip(l1,l2)]

print(result)


```
The | operator is used to perform a set union operation on the sets a and b.
The resulting set after the union operation is {1, 2, 3, 4, 5, 6}.
The elements of the resulting set are unpacked into variables c, *d, and e.
The * operator is used to assign all the elements except the first and last to variable d.
So d will contain the elements [2, 4, 6].
The two input lists l1 and l2 represent the numbers 342 and 465 respectively.
The lists are reversed so that we can start adding from the least significant digit.
The zip function is used to create tuples of corresponding elements from the two lists.
The tuples are then added using a list comprehension to produce a new list of sums.
Each sum is stored in the resulting list in reverse order, so we get the correct answer [7, 0, 8] which represents the number 807.

---

### DeepCopies.py
**Code**

```python
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


```
The code provided above creates a copy of the original list using the slice operator [:]. Then, it creates an empty list copied_outer_list and copies the elements of the inner_list into this new list. Finally, it appends copied_outer_list to itself, creating a self-referential list.

When the original list is modified by appending "k-nines" to the first sub-list using original[0].append("k-nines"), this change affects the original list but not the copied version or the self-referential list created earlier. This is because the slice operator only creates a shallow copy of the original list, meaning that the top-level list and its elements are copied but the elements themselves are not recursively copied.

To perform a deep copy of the original list, including all its sub-lists and their elements, you can use the copy module's deepcopy function. Here's an example:

```python

import copy

original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_version = copy.deepcopy(original)
```
This will create a new list copied_version that is a deep copy of original. Changes made to original will not affect copied_version, and vice versa.

### nestsedData.py
**Code**

```Json
res = {
  "search_metadata": {
    "count": 3,
    "completed_in": 0.015,
    "max_id_str": "536624519285583872",
    "since_id_str": "0",
    "next_results": "?max_id=536623674942439424&q=University%20of%20Michigan&count=3&include_entities=1",
    "refresh_url": "?since_id=536624519285583872&q=University%20of%20Michigan&include_entities=1",
    "since_id": 0,
    "query": "University+of+Michigan",
    "max_id": 536624519285583872
  },
  "statuses": [
    {
      "contributors": None,
      "truncated": False,
      "text": "RT @mikeweber25: I'm decommiting from the university of Michigan thank you Michigan for the love and support I'll remake my decision at the\u2026",
      "in_reply_to_status_id": None,
      "id": 536624519285583872,
      "favorite_count": 0,
      "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
      "retweeted": False,
      "coordinates": None,
      "entities": {
        "symbols": [],
        "user_mentions": [
          {
            "id": 1119996684,
            "indices": [
              3,
              15
            ],
            "id_str": "1119996684",
            "screen_name": "mikeweber25",
            "name": "Mikey"
          }
        ],
        "hashtags": [],
        "urls": []
      },
      "in_reply_to_screen_name": None,
      "in_reply_to_user_id": None,
      "retweet_count": 2014,
      "id_str": "536624519285583872",
      "favorited": False,
      "retweeted_status": {
        "contributors": None,
        "truncated": False,
        "text": "I'm decommiting from the university of Michigan thank you Michigan for the love and support I'll remake my decision at the army bowl",
        "in_reply_to_status_id": None,
        "id": 536300265616322560,
        "favorite_count": 1583,
        "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
        "retweeted": False,
        "coordinates": None,
        "entities": {
          "symbols": [],
          "user_mentions": [],
          "hashtags": [],
          "urls": []
        },
        "in_reply_to_screen_name": None,
        "in_reply_to_user_id": None,
        "retweet_count": 2014,
        "id_str": "536300265616322560",
        "favorited": False,
        "user": {
          "follow_request_sent": False,
          "profile_use_background_image": True,
          "profile_text_color": "666666",
          "default_profile_image": False,
          "id": 1119996684,
          "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme9/bg.gif",
          "verified": False,
          "profile_location": None,
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/534465900343083008/A09dIq1d_normal.jpeg",
          "profile_sidebar_fill_color": "252429",
          "entities": {
            "description": {
              "urls": []
            }
          },
          "followers_count": 5444,
          "profile_sidebar_border_color": "FFFFFF",
          "id_str": "1119996684",
          "profile_background_color": "C0DEED",
          "listed_count": 36,
          "is_translation_enabled": False,
          "utc_offset": None,
          "statuses_count": 6525,
          "description": "Mike Weber (U.S Army All American) DETROIT CTSENIOR State Champion",
          "friends_count": 693,
          "location": "",
          "profile_link_color": "0084B4",
          "profile_image_url": "http://pbs.twimg.com/profile_images/534465900343083008/A09dIq1d_normal.jpeg",
          "following": False,
          "geo_enabled": False,
          "profile_banner_url": "https://pbs.twimg.com/profile_banners/1119996684/1416261575",
          "profile_background_image_url": "http://abs.twimg.com/images/themes/theme9/bg.gif",
          "name": "Mikey",
          "lang": "en",
          "profile_background_tile": False,
          "favourites_count": 1401,
          "screen_name": "mikeweber25",
          "notifications": False,
          "url": None,
          "created_at": "Fri Jan 25 18:45:53 +0000 2013",
          "contributors_enabled": False,
          "time_zone": None,
          "protected": False,
          "default_profile": False,
          "is_translator": False
        },
        "geo": None,
        "in_reply_to_user_id_str": None,
        "lang": "en",
        "created_at": "Sat Nov 22 23:28:41 +0000 2014",
        "in_reply_to_status_id_str": None,
        "place": None,
        "metadata": {
          "iso_language_code": "en",
          "result_type": "recent"
        }
      },
      "user": {
        "follow_request_sent": False,
        "profile_use_background_image": True,
        "profile_text_color": "333333",
        "default_profile_image": False,
        "id": 2435537208,
        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
        "verified": False,
        "profile_location": None,
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/532694075947110400/oZEP5XNQ_normal.jpeg",
        "profile_sidebar_fill_color": "DDEEF6",
        "entities": {
          "description": {
            "urls": []
          }
        },
        "followers_count": 161,
        "profile_sidebar_border_color": "C0DEED",
        "id_str": "2435537208",
        "profile_background_color": "C0DEED",
        "listed_count": 0,
        "is_translation_enabled": False,
        "utc_offset": None,
        "statuses_count": 524,
        "description": "Delasalle '17 Baseball & Football.",
        "friends_count": 255,
        "location": "",
        "profile_link_color": "0084B4",
        "profile_image_url": "http://pbs.twimg.com/profile_images/532694075947110400/oZEP5XNQ_normal.jpeg",
        "following": False,
        "geo_enabled": False,
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/2435537208/1406779364",
        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
        "name": "Andrew Brooks",
        "lang": "en",
        "profile_background_tile": False,
        "favourites_count": 555,
        "screen_name": "31brooks_",
        "notifications": False,
        "url": None,
        "created_at": "Wed Apr 09 14:34:41 +0000 2014",
        "contributors_enabled": False,
        "time_zone": None,
        "protected": False,
        "default_profile": True,
        "is_translator": False
      },
      "geo": None,
      "in_reply_to_user_id_str": None,
      "lang": "en",
      "created_at": "Sun Nov 23 20:57:10 +0000 2014",
      "in_reply_to_status_id_str": None,
      "place": None,
      "metadata": {
        "iso_language_code": "en",
        "result_type": "recent"
      }
    },
    {
      "contributors": None,
      "truncated": False,
      "text": "RT @Plantedd: The University of Michigan moved a big Bur Oak yesterday. 65ft tall. 350+ tons. http://t.co/v2Y6vl3f9e",
      "in_reply_to_status_id": None,
      "id": 536624216305848320,
      "favorite_count": 0,
      "source": "<a href=\"http://tapbots.com/tweetbot\" rel=\"nofollow\">Tweetbot for i\u039fS</a>",
      "retweeted": False,
      "coordinates": None,
      "entities": {
        "symbols": [],
        "user_mentions": [
          {
            "id": 462890283,
            "indices": [
              3,
              12
            ],
            "id_str": "462890283",
            "screen_name": "Plantedd",
            "name": "David Wong"
          }
        ],
        "hashtags": [],
        "urls": [],
        "media": [
          {
            "source_status_id_str": "526276522374889472",
            "expanded_url": "http://twitter.com/Plantedd/status/526276522374889472/photo/1",
            "display_url": "pic.twitter.com/v2Y6vl3f9e",
            "url": "http://t.co/v2Y6vl3f9e",
            "media_url_https": "https://pbs.twimg.com/media/B021tLsIYAADq21.jpg",
            "source_status_id": 526276522374889472,
            "id_str": "526276519308845056",
            "sizes": {
              "small": {
                "h": 191,
                "resize": "fit",
                "w": 340
              },
              "large": {
                "h": 576,
                "resize": "fit",
                "w": 1024
              },
              "medium": {
                "h": 337,
                "resize": "fit",
                "w": 600
              },
              "thumb": {
                "h": 150,
                "resize": "crop",
                "w": 150
              }
            },
            "indices": [
              94,
              116
            ],
            "type": "photo",
            "id": 526276519308845056,
            "media_url": "http://pbs.twimg.com/media/B021tLsIYAADq21.jpg"
          }
        ]
      },
      "in_reply_to_screen_name": None,
      "in_reply_to_user_id": None,
      "retweet_count": 27,
      "id_str": "536624216305848320",
      "favorited": False,
      "retweeted_status": {
        "contributors": None,
        "truncated": False,
        "text": "The University of Michigan moved a big Bur Oak yesterday. 65ft tall. 350+ tons. http://t.co/v2Y6vl3f9e",
        "in_reply_to_status_id": None,
        "id": 526276522374889472,
        "favorite_count": 25,
        "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
        "retweeted": False,
        "coordinates": None,
        "entities": {
          "symbols": [],
          "user_mentions": [],
          "hashtags": [],
          "urls": [],
          "media": [
            {
              "expanded_url": "http://twitter.com/Plantedd/status/526276522374889472/photo/1",
              "display_url": "pic.twitter.com/v2Y6vl3f9e",
              "url": "http://t.co/v2Y6vl3f9e",
              "media_url_https": "https://pbs.twimg.com/media/B021tLsIYAADq21.jpg",
              "id_str": "526276519308845056",
              "sizes": {
                "small": {
                  "h": 191,
                  "resize": "fit",
                  "w": 340
                },
                "large": {
                  "h": 576,
                  "resize": "fit",
                  "w": 1024
                },
                "medium": {
                  "h": 337,
                  "resize": "fit",
                  "w": 600
                },
                "thumb": {
                  "h": 150,
                  "resize": "crop",
                  "w": 150
                }
              },
              "indices": [
                80,
                102
              ],
              "type": "photo",
              "id": 526276519308845056,
              "media_url": "http://pbs.twimg.com/media/B021tLsIYAADq21.jpg"
            }
          ]
        },
        "in_reply_to_screen_name": None,
        "in_reply_to_user_id": None,
        "retweet_count": 27,
        "id_str": "526276522374889472",
        "favorited": False,
        "user": {
          "follow_request_sent": False,
          "profile_use_background_image": True,
          "profile_text_color": "333333",
          "default_profile_image": False,
          "id": 462890283,
          "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
          "verified": False,
          "profile_location": None,
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/1791926707/Plantedd_Logo__square__normal.jpg",
          "profile_sidebar_fill_color": "DDEEF6",
          "entities": {
            "url": {
              "urls": [
                {
                  "url": "http://t.co/ZOnsCHvoKt",
                  "indices": [
                    0,
                    22
                  ],
                  "expanded_url": "http://www.plantedd.com",
                  "display_url": "plantedd.com"
                }
              ]
            },
            "description": {
              "urls": []
            }
          },
          "followers_count": 2598,
          "profile_sidebar_border_color": "C0DEED",
          "id_str": "462890283",
          "profile_background_color": "C0DEED",
          "listed_count": 61,
          "is_translation_enabled": False,
          "utc_offset": 0,
          "statuses_count": 8157,
          "description": "Hello, I'm the supervillain behind Plantedd. We're an online market for plant lovers plotting to take over the world by making it simple to find and buy plants.",
          "friends_count": 2664,
          "location": "UK",
          "profile_link_color": "0084B4",
          "profile_image_url": "http://pbs.twimg.com/profile_images/1791926707/Plantedd_Logo__square__normal.jpg",
          "following": False,
          "geo_enabled": False,
          "profile_banner_url": "https://pbs.twimg.com/profile_banners/462890283/1398254314",
          "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
          "name": "David Wong",
          "lang": "en",
          "profile_background_tile": False,
          "favourites_count": 371,
          "screen_name": "Plantedd",
          "notifications": False,
          "url": "http://t.co/ZOnsCHvoKt",
          "created_at": "Fri Jan 13 13:46:46 +0000 2012",
          "contributors_enabled": False,
          "time_zone": "Edinburgh",
          "protected": False,
          "default_profile": True,
          "is_translator": False
        },
        "geo": None,
        "in_reply_to_user_id_str": None,
        "possibly_sensitive": False,
        "lang": "en",
        "created_at": "Sun Oct 26 07:37:55 +0000 2014",
        "in_reply_to_status_id_str": None,
        "place": None,
        "metadata": {
          "iso_language_code": "en",
          "result_type": "recent"
        }
      },
      "user": {
        "follow_request_sent": False,
        "profile_use_background_image": True,
        "profile_text_color": "2A48AE",
        "default_profile_image": False,
        "id": 104940733,
        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme17/bg.gif",
        "verified": False,
        "profile_location": None,
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/2878477539/78e20432088b5ee2addc9ce3362fd461_normal.jpeg",
        "profile_sidebar_fill_color": "6378B1",
        "entities": {
          "description": {
            "urls": []
          }
        },
        "followers_count": 149,
        "profile_sidebar_border_color": "FBD0C9",
        "id_str": "104940733",
        "profile_background_color": "0C003D",
        "listed_count": 18,
        "is_translation_enabled": False,
        "utc_offset": 0,
        "statuses_count": 16031,
        "description": "Have you any dreams you'd like to sell?",
        "friends_count": 248,
        "location": "",
        "profile_link_color": "0F1B7C",
        "profile_image_url": "http://pbs.twimg.com/profile_images/2878477539/78e20432088b5ee2addc9ce3362fd461_normal.jpeg",
        "following": False,
        "geo_enabled": False,
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/104940733/1410032966",
        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme17/bg.gif",
        "name": "Heather",
        "lang": "en",
        "profile_background_tile": False,
        "favourites_count": 777,
        "screen_name": "froyoho",
        "notifications": False,
        "url": None,
        "created_at": "Thu Jan 14 21:37:54 +0000 2010",
        "contributors_enabled": False,
        "time_zone": "London",
        "protected": False,
        "default_profile": False,
        "is_translator": False
      },
      "geo": None,
      "in_reply_to_user_id_str": None,
      "possibly_sensitive": False,
      "lang": "en",
      "created_at": "Sun Nov 23 20:55:57 +0000 2014",
      "in_reply_to_status_id_str": None,
      "place": None,
      "metadata": {
        "iso_language_code": "en",
        "result_type": "recent"
      }
    },
    {
      "contributors": None,
      "truncated": False,
      "text": "RT @NotableHistory: Madonna, 18 year old freshman at the University of Michigan, 1976 http://t.co/x2dm1G67ea",
      "in_reply_to_status_id": None,
      "id": 536623674942439425,
      "favorite_count": 0,
      "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
      "retweeted": False,
      "coordinates": None,
      "entities": {
        "symbols": [],
        "user_mentions": [
          {
            "id": 844766941,
            "indices": [
              3,
              18
            ],
            "id_str": "844766941",
            "screen_name": "NotableHistory",
            "name": "OnThisDay & Facts"
          }
        ],
        "hashtags": [],
        "urls": [],
        "media": [
          {
            "source_status_id_str": "536610190334779392",
            "expanded_url": "http://twitter.com/NotableHistory/status/536610190334779392/photo/1",
            "display_url": "pic.twitter.com/x2dm1G67ea",
            "url": "http://t.co/x2dm1G67ea",
            "media_url_https": "https://pbs.twimg.com/media/B3EXbQkCMAEipwM.jpg",
            "source_status_id": 536610190334779392,
            "id_str": "536235587703812097",
            "sizes": {
              "small": {
                "h": 487,
                "resize": "fit",
                "w": 340
              },
              "large": {
                "h": 918,
                "resize": "fit",
                "w": 640
              },
              "medium": {
                "h": 860,
                "resize": "fit",
                "w": 600
              },
              "thumb": {
                "h": 150,
                "resize": "crop",
                "w": 150
              }
            },
            "indices": [
              86,
              108
            ],
            "type": "photo",
            "id": 536235587703812097,
            "media_url": "http://pbs.twimg.com/media/B3EXbQkCMAEipwM.jpg"
          }
        ]
      },
      "in_reply_to_screen_name": None,
      "in_reply_to_user_id": None,
      "retweet_count": 9,
      "id_str": "536623674942439425",
      "favorited": False,
      "retweeted_status": {
        "contributors": None,
        "truncated": False,
        "text": "Madonna, 18 year old freshman at the University of Michigan, 1976 http://t.co/x2dm1G67ea",
        "in_reply_to_status_id": None,
        "id": 536610190334779392,
        "favorite_count": 13,
        "source": "<a href=\"https://ads.twitter.com\" rel=\"nofollow\">Twitter Ads</a>",
        "retweeted": False,
        "coordinates": None,
        "entities": {
          "symbols": [],
          "user_mentions": [],
          "hashtags": [],
          "urls": [],
          "media": [
            {
              "expanded_url": "http://twitter.com/NotableHistory/status/536610190334779392/photo/1",
              "display_url": "pic.twitter.com/x2dm1G67ea",
              "url": "http://t.co/x2dm1G67ea",
              "media_url_https": "https://pbs.twimg.com/media/B3EXbQkCMAEipwM.jpg",
              "id_str": "536235587703812097",
              "sizes": {
                "small": {
                  "h": 487,
                  "resize": "fit",
                  "w": 340
                },
                "large": {
                  "h": 918,
                  "resize": "fit",
                  "w": 640
                },
                "medium": {
                  "h": 860,
                  "resize": "fit",
                  "w": 600
                },
                "thumb": {
                  "h": 150,
                  "resize": "crop",
                  "w": 150
                }
              },
              "indices": [
                66,
                88
              ],
              "type": "photo",
              "id": 536235587703812097,
              "media_url": "http://pbs.twimg.com/media/B3EXbQkCMAEipwM.jpg"
            }
          ]
        },
        "in_reply_to_screen_name": None,
        "in_reply_to_user_id": None,
        "retweet_count": 9,
        "id_str": "536610190334779392",
        "favorited": False,
        "user": {
          "follow_request_sent": False,
          "profile_use_background_image": True,
          "profile_text_color": "333333",
          "default_profile_image": False,
          "id": 844766941,
          "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/458461302696837121/rGlGdWsc.png",
          "verified": False,
          "profile_location": None,
          "profile_image_url_https": "https://pbs.twimg.com/profile_images/481243404320251905/gCr1cVP2_normal.png",
          "profile_sidebar_fill_color": "DDFFCC",
          "entities": {
            "url": {
              "urls": [
                {
                  "url": "http://t.co/9fTPk5A4wh",
                  "indices": [
                    0,
                    22
                  ],
                  "expanded_url": "http://notablefacts.com/",
                  "display_url": "notablefacts.com"
                }
              ]
            },
            "description": {
              "urls": []
            }
          },
          "followers_count": 73817,
          "profile_sidebar_border_color": "FFFFFF",
          "id_str": "844766941",
          "profile_background_color": "9AE4E8",
          "listed_count": 485,
          "is_translation_enabled": False,
          "utc_offset": -21600,
          "statuses_count": 38841,
          "description": "On This Day in History, Historical Pictures & other Interesting Facts....Historyfollower@gmail.com",
          "friends_count": 43594,
          "location": "",
          "profile_link_color": "0084B4",
          "profile_image_url": "http://pbs.twimg.com/profile_images/481243404320251905/gCr1cVP2_normal.png",
          "following": False,
          "geo_enabled": False,
          "profile_banner_url": "https://pbs.twimg.com/profile_banners/844766941/1411076349",
          "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/458461302696837121/rGlGdWsc.png",
          "name": "OnThisDay & Facts",
          "lang": "en",
          "profile_background_tile": True,
          "favourites_count": 1383,
          "screen_name": "NotableHistory",
          "notifications": False,
          "url": "http://t.co/9fTPk5A4wh",
          "created_at": "Tue Sep 25 03:08:59 +0000 2012",
          "contributors_enabled": False,
          "time_zone": "Central Time (US & Canada)",
          "protected": False,
          "default_profile": False,
          "is_translator": False
        },
        "geo": None,
        "in_reply_to_user_id_str": None,
        "possibly_sensitive": False,
        "lang": "en",
        "created_at": "Sun Nov 23 20:00:13 +0000 2014",
        "in_reply_to_status_id_str": None,
        "place": None,
        "metadata": {
          "iso_language_code": "en",
          "result_type": "recent"
        }
      },
      "user": {
        "follow_request_sent": False,
        "profile_use_background_image": True,
        "profile_text_color": "333333",
        "default_profile_image": False,
        "id": 818185729,
        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
        "verified": False,
        "profile_location": None,
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/486215801498640384/rz9o7LnF_normal.jpeg",
        "profile_sidebar_fill_color": "DDEEF6",
        "entities": {
          "description": {
            "urls": []
          }
        },
        "followers_count": 302,
        "profile_sidebar_border_color": "C0DEED",
        "id_str": "818185729",
        "profile_background_color": "C0DEED",
        "listed_count": 0,
        "is_translation_enabled": False,
        "utc_offset": None,
        "statuses_count": 395,
        "description": "Formerly with California Dept of General Services, now freelancing around the Sacramento area...",
        "friends_count": 1521,
        "location": "Citrus Heights, CA",
        "profile_link_color": "0084B4",
        "profile_image_url": "http://pbs.twimg.com/profile_images/486215801498640384/rz9o7LnF_normal.jpeg",
        "following": False,
        "geo_enabled": True,
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/818185729/1383764759",
        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
        "name": "M Duncan",
        "lang": "en",
        "profile_background_tile": False,
        "favourites_count": 6544,
        "screen_name": "MDuncan95814",
        "notifications": False,
        "url": None,
        "created_at": "Tue Sep 11 21:02:09 +0000 2012",
        "contributors_enabled": False,
        "time_zone": None,
        "protected": False,
        "default_profile": True,
        "is_translator": False
      },
      "geo": None,
      "in_reply_to_user_id_str": None,
      "possibly_sensitive": False,
      "lang": "en",
      "created_at": "Sun Nov 23 20:53:48 +0000 2014",
      "in_reply_to_status_id_str": None,
      "place": None,
      "metadata": {
        "iso_language_code": "en",
        "result_type": "recent"
      }
    }
  ]
}
```
```python
# python program to extract nested data
import  json
print(json.dumps(res, indent=2))

print('----------------------------------------')
print(type(res))
print(res.keys())
print('----------------------Extract-----------------------------------------')
res2 = res['statuses']
print(len(res2))
print(type(res2))

print('---------------------------------------------------------------------')
for res3 in res2[:1]:
    print("------------Level3 : a Tweet -----------------")
    print(json.dumps(res3, indent=2) [:30])
    print('---------------------------------------------------------------------')
    print(len(res3))
    print(res3.keys())
    print('---------------------------------------------------------------------')
    res4 = res3['user']
    print(res4)
    print(type(res4))  # it's a dictionary
    print(res4.keys())
    print('------------------Level 4 : the user who wrote the tweet ------------')
    print(res4['screen_name'], res4['created_at'])
print('---------------------------------------------------------------------')

for res3 in res2:
    res4 = res3['user']
    print(res4['screen_name'], res4['created_at'])
print('---------------------------------------------------------------------')
for res3 in res['statuses']:
    print(res3['user']['screen_name'], res3['user']['created_at'])

```
This program uses the JSON module in Python to extract nested data from a JSON object.

First, it imports the JSON module and prints the JSON object res using the json.dumps function with an indentation of 2 spaces.

Then, it prints the type of res and its keys.

Next, it extracts the 'statuses' key from res into res2, prints its length, type, and keys.

Then, it loops through the first item of res2 and prints its JSON representation, length, keys, and extracts the 'user' key into res4. It then prints the type and keys of res4 and extracts the 'screen_name' and 'created_at' keys from it.

Next, it loops through all items in res2 and extracts the 'user' key into res4, then prints the 'screen_name' and 'created_at' keys from res4.

Finally, it loops through all items in the 'statuses' key of res and prints the 'screen_name' and 'created_at' keys from the 'user' key of each item.

---
### Filter.py
**Code**
```python
def keep_events(nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list


print(keep_events([2,3,6,4,0,8,7,9,10,11,13,15,17]))

print("------------------------------")
def keepEvent(numbers):
    new_seq = filter(lambda numbers:  num % 2 ==0, numbers)
    return  list(new_seq)
print(keep_events([2,3,6,4,0,8,7,9,10,11,13,15,17]))

print("------------------------------")
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

filter_testing = filter(lambda word: "w" in word, lst_check)
filtered_words = list(filter_testing)

print(filtered_words)
print("------------------------------")

lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]

lst2 = filter(lambda word: "o" in word, lst)
filtered_lists = list(lst2)
print(filtered_lists)

```
The first two code snippets are attempting to accomplish the same task of filtering even numbers from a list of integers.

The first code snippet defines a function keep_events that takes a list of integers nums and creates an empty list new_list. It then iterates through each element num in nums and checks if it is even by using the modulo operator % to check if the remainder is zero when divided by 2. If it is even, num is appended to new_list. Finally, new_list is returned.

The second code snippet defines a function keepEvent that takes a list of integers numbers and uses the filter function to return a new sequence that contains only the even numbers in numbers. It does this by defining a lambda function that takes an argument num and checks if it is even, and passing this lambda function as the first argument to the filter function along with numbers. The filter function returns an iterator object that can be converted to a list using the list function, and this list is returned by keepEvent.

The third code snippet defines a list of strings lst_check and uses the filter function to return a new sequence that contains only the strings in lst_check that contain the character "w". It does this by defining a lambda function that takes an argument word and checks if it contains the character "w", and passing this lambda function as the first argument to the filter function along with lst_check. The filter function returns an iterator object that can be converted to a list using the list function, and this list is printed.

The fourth code snippet defines a list of strings lst and uses the filter function to return a new sequence that contains only the strings in lst that contain the character "o". It does this by defining a lambda function that takes an argument word and checks if it contains the character "o", and passing this lambda function as the first argument to the filter function along with lst. The filter function returns an iterator object that can be converted to a list using the list function, and this list is printed

### maps.py
**Code**
```python
def multiplication(a_list):
    new_list = []
    for any_value in a_list:
        new_element = 2 * any_value
        new_list.append(new_element)
    return  new_list

nums = [4,5,6,1,8]
print(nums)
print("Double the new list of number by  2:")
nums = multiplication(nums)
print(nums)

def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)

things = [2, 5, 9]

things4 = map((lambda value: 4*value), things)
print(list(things4))

# or all on one line
print(list(map((lambda value: 5*value), [1, 2, 3])))
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

greeting_doubled = list(map(lambda x: x*2, lst))
print(greeting_doubled)

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

def transformer(st):
    return st.upper()

abbrevs_upper = map(transformer, abbrevs)
abbrevs_upper = map(lambda st: st.upper(), abbrevs)
print(list(abbrevs_upper))

```

The code above demonstrates the use of the map function to apply a function to each element in a list and return a new list of the results.

The multiplication function takes a list a_list, creates a new empty list new_list, and iterates through each element in a_list. For each element, it multiplies it by 2 and appends the result to new_list. Finally, it returns new_list.

The triple function takes a single value and returns its triple (i.e., multiplies it by 3).

The tripleStuff function takes a list a_list and uses the map function to apply the triple function to each element in a_list. It returns a new list of the results.

The quadrupleStuff function is similar to tripleStuff, but it uses a lambda function instead of a named function to multiply each element by 4.

The code also demonstrates some examples of using map with lambda functions. For example, the code things4 = map((lambda value: 4*value), things) creates a new list things4 that contains each element of things multiplied by 4. Similarly, the code abbrevs_upper = map(lambda st: st.upper(), abbrevs) creates a new list abbrevs_upper that contains each element of abbrevs converted to uppercase using a lambda function.

The code also demonstrates some more complex examples of using map. For example, the code greeting_doubled = list(map(lambda x: x*2, lst)) creates a new list greeting_doubled that contains each element of lst repeated twice. The code abbrevs_upper = map(transformer, abbrevs) creates a new list abbrevs_upper that contains each element of abbrevs converted to uppercase using a named function transformer.

---

###  GET Request - to Search for images on Google
```python
import requests
u = {'q': 'hardcleats and softcleats', 'tbm':'isch'}
out = requests.get("https://www.google.com/search", params=u)
print(out.url)
print(out.text)

```
This code sends a GET request to Google Images with the query parameters "q=hardcleats and softcleats" and "tbm=isch", and then prints out the URL of the request and the text content of the response.

The requests library is used to send HTTP requests to websites. In this case, it is used to send a GET request to the Google Images search page with the specified query parameters.

The params parameter in the get method is used to specify the query parameters to send along with the request. In this case, the 'q' parameter specifies the search query, and the 'tbm' parameter specifies the type of search to perform (in this case, an image search).

The out.url statement is used to print out the URL of the request, which is the Google Images search page with the specified query parameters.

The out.text statement is used to print out the text content of the response, which is the HTML code of the search results page returned by Google Images. This can be parsed using tools like BeautifulSoup to extract the images or other information from the page.

---
### instaLoader.py
**Code**
```python
import instaloader
import pandas
import re
# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
# Loading the profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'mngugi7')
print(profile)

print('----------------------------------------------------------')
# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()

# Loading a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'mngugi7')
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers Count: ", profile.followers)
print("Following Count: ", profile.followees)
print("Bio: ", profile.biography)
print("External URL: ", profile.external_url)

print('---------------------------------------------------------')
# Creating an instance of Instaloader class
bot = instaloader.Instaloader()
profile = instaloader.Profile.from_username(bot.context, "mngugi7")
print("Username: ", profile.username)
print("Bio: ", profile.biography)
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)
print("Emails extracted from the bio:")
print(emails)

bot = instaloader.Instaloader()
bot.login(user="Your_username", passwd="Your_password")

# Loading a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'Your_target_account_insta_handle')

# Retrieving the usernames of all followers
followers = [follower.username for follower in profile.get_followers()]

# Converting the data to a DataFrame
followers_df = pd.DataFrame(followers)

# Storing the results in a CSV file
followers_df.to_csv('followers.csv', index=False)

# Retrieving the usernames of all followings
followings = [followee.username for followee in profile.get_followees()]

# Converting the data to a DataFrame
followings_df = pd.DataFrame(followings)

# Storing the results in a CSV file
followings_df.to_csv('followings.csv', index=False)

```

This Python code uses the Instaloader library to retrieve information from an Instagram profile and extract emails from the profile's bio. It also logs into an Instagram account, retrieves the usernames of followers and followees of a target Instagram profile, and stores the results in CSV files.

The first part of the code loads the profile from an Instagram handle and prints some basic information about the profile, such as the username, user ID, number of posts, followers count, following count, bio, and external URL.

The second part of the code extracts emails from the profile's bio using a regular expression.

The third part of the code logs into an Instagram account, loads a target Instagram profile, retrieves the usernames of its followers and followees, converts the data to DataFrames, and stores the results in CSV files named "followers.csv" and "followings.csv", respectively.

To use this code, you will need to have the Instaloader library installed and replace the placeholders "Your_username" and "Your_password" with your own Instagram account credentials and "Your_target_account_insta_handle" with the handle of the Instagram profile you want to retrieve follower and followee data from.


---

### NetworkSockets.py
**Code**

```python
import socket

lasocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lasocket.connect(('<xxxxx.com>', 80))

cmd = 'GET http://<xxxxx.com> HTTP/1.0\r\n\r\n'.encode()
lasocket.send(cmd)

while True:
    data = lasocket.recv(512)
    if (len(data) < 1 ):
        break
    print(data.decode(), end='')

lasocket.close()

```

This is a Python code snippet that demonstrates how to make a GET request to a web server using the sockets library in Python. Let's go through each line of the code:
import socket: This line imports the Python sockets library, which provides a low-level interface for network communication.
lasocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM): This line creates a new socket object using the socket.socket() method. The AF_INET parameter specifies that we want to use IPv4, and the SOCK_STREAM parameter specifies that we want to use the TCP protocol.
lasocket.connect(('<xxxxx.com>', 80)): This line connects to the web server at the specified IP address and port number. In this case, we are connecting to port 80, which is the default port for HTTP traffic.
cmd = 'GET http://<xxxxx.com> HTTP/1.0\r\n\r\n'.encode(): This line creates a GET request message that includes the URL of the web page we want to retrieve. The .encode() method is used to convert the string to bytes, which is required for sending the message over the network.
lasocket.send(cmd): This line sends the GET request message to the web server.
while True:: This line starts a loop that will continue until the break statement is executed.
data = lasocket.recv(512): This line reads up to 512 bytes of data from the web server.
if (len(data) < 1 ):: This line checks if no data was received, which indicates the end of the response message.
break: This line exits the loop if no data was received.
print(data.decode(), end=''): This line prints the received data as a string.
lasocket.close(): This line closes the connection to the web server.

Overall, this code connects to a web server, sends a GET request message, reads and prints the response message until the end of the message is reached, and then closes the connection.

---

### retrieveWebPage.py
**Code**
```python
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://<xxxxxx.com>/ffff.txt')

counts = dict()
for line in fhand:

    print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

```
This Python code snippet reads a text file from a web server using the urllib library and counts the occurrences of each word in the file. Let's go through each line of the code:

import urllib.request, urllib.parse, urllib.error: This line imports the necessary modules from the urllib library, which provides a set of high-level interfaces for working with URLs.

fhand = urllib.request.urlopen('http://<xxxxxx.com>/ffff.txt'): This line opens a connection to the specified URL using the urllib.request.urlopen() method and returns a file handle object that can be used to read the contents of the file.

counts = dict(): This line creates an empty dictionary called counts, which will be used to store the word counts.
for line in fhand:: This line starts a loop that iterates over each line in the file.
print(line.decode().strip()): This line prints each line of the file to the console, after decoding the bytes into a string and stripping any leading or trailing whitespace.
words = line.decode().split(): This line splits the line into a list of words using the split() method.
for word in words:: This line starts a loop that iterates over each word in the list.
counts[word] = counts.get(word, 0) + 1: This line updates the count for the current word by adding 1 to its current count in the counts dictionary. The get() method is used to retrieve the current count for the word, or 0 if it doesn't exist yet.
print(counts): This line prints the final word count dictionary to the console.
Overall, this code retrieves a text file from a web server, reads the contents of the file, counts the occurrences of each word, and prints the word counts to the console.

---

### XmlPy.py
**Code**
```python
import xml.etree.ElementTree as ET

data = '''<person>
<name>Maradonna</name>
<phone type="intl">
+254303030
</phone>
<email hide="yes"></email>
</person>'''

tree = ET.fromstring(data)

print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
print('--------------------------------------')

input = ''' <stuff>
<users>
<user x = "2">
<id>001</id>
<name>Messi</name>
</user>
<user x = "7">
<id>0011</id>
<name>Wanchop</name>
</user>
</users>
</stuff>
'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User Count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('id', item.find('id').text)
    print('Attribute', item.get('x'))

```
This Python code snippet reads a text file from a web server using the urllib library and counts the occurrences of each word in the file. Let's go through each line of the code:

import urllib.request, urllib.parse, urllib.error: This line imports the necessary modules from the urllib library, which provides a set of high-level interfaces for working with URLs.

fhand = urllib.request.urlopen('http://<xxxxxx.com>/ffff.txt'): This line opens a connection to the specified URL using the urllib.request.urlopen() method and returns a file handle object that can be used to read the contents of the file.

counts = dict(): This line creates an empty dictionary called counts, which will be used to store the word counts.
for line in fhand:: This line starts a loop that iterates over each line in the file.

print(line.decode().strip()): This line prints each line of the file to the console, after decoding the bytes into a string and stripping any leading or trailing whitespace.
words = line.decode().split(): This line splits the line into a list of words using the split() method.
for word in words:: This line starts a loop that iterates over each word in the list.
counts[word] = counts.get(word, 0) + 1: This line updates the count for the current word by adding 1 to its current count in the counts dictionary. The get() method is used to retrieve the current count for the word, or 0 if it doesn't exist yet.
print(counts): This line prints the final word count dictionary to the console.

Overall, this code retrieves a text file from a web server, reads the contents of the file, counts the occurrences of each word, and prints the word counts to the console.

---

### question1.py
**Code**

```python
class Compare:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __bool__(self):
        return  self.a is self.b

c1 = Compare([1,2,3], [1,2,3])

print(c1.__bool__())

```
The output of the code is False.

The class Compare takes two arguments a and b in the constructor and assigns them to the instance variables self.a and self.b.

The __bool__ method is defined to return True if self.a is the same object as self.b, and False otherwise.

In the given code, an instance c1 of the Compare class is created with arguments [1,2,3] and [1,2,3]. These are two different lists with the same contents, so self.a is self.b returns False. Therefore, when c1.__bool__() is called, it returns False.

Note that it is generally recommended to use the == operator to compare the values of objects, rather than the is operator, which checks if two objects are the same instance. In this case, using == instead of is would make the comparison return True, since the two lists have the same contents.

---

### question2.py
**Code**

```python
def tricky_list(lst):
    return lst[:-1] and lst[:-2] \
        if len(lst[1]) == len(lst[-1])\
        else lst[1:]

names = ["Ben", "Ken", "Len"]
print(tricky_list(names))

```

The output of the code is ["Ken"].

The tricky_list function takes a list lst as input. It first checks if the length of the second element of lst is equal to the length of the last element of lst. If this condition is true, it returns the slice of lst from the beginning up to the second-to-last element, skipping the last two elements. Otherwise, it returns a slice of lst from the second element to the end.

In the given code, the names list has three elements: "Ben", "Ken", and "Len". The length of the second element ("Ken") is 3, which is equal to the length of the last element ("Len"). Therefore, the function returns lst[:-1] and lst[:-2], which is equivalent to lst[:-2], resulting in a list with only the second element: ["Ken"].

Note that the use of the and operator in the return statement is a shorthand way of checking if the left-hand side is not an empty list before returning the right-hand side. If the left-hand side is an empty list, the expression evaluates to the empty list and short-circuits, not evaluating the right-hand side at all. If the left-hand side is not an empty list, the expression evaluates to the right-hand side. In this case, lst[:-1] and lst[:-2] are both non-empty lists, so the expression evaluates to lst[:-2].

---

### questio4.py
**Code**

```python
for i in range(1, 4):
    for j in range(1, 4):
        k = i*j
        print(k)
```
The code uses two nested for loops to iterate over the values 1, 2, and 3 for both i and j. For each pair of values, it multiplies i and j together and assigns the result to k. It then prints the value of k.

The first iteration of the outer loop sets i to 1. The inner loop then iterates over the values 1, 2, and 3 for j. For each value of j, the product i*j is computed and printed. This results in the values 1, 2, and 3 being printed in turn.

The second iteration of the outer loop sets i to 2. The inner loop then iterates over the values 1, 2, and 3 for j again. For each value of j, the product i*j is computed and printed. This results in the values 2, 4, and 6 being printed in turn.

The third and final iteration of the outer loop sets i to 3. The inner loop then iterates over the values 1, 2, and 3 for j yet again. For each value of j, the product i*j is computed and printed. This results in the values 3, 6, and 9 being printed in turn.

Therefore, the output of the code is as shown at the beginning.

---


### passwordGen.py
```python

import  random

lower = "abcdefghijklmnopqrst"
UPPER = "ABCDEFGHIJKLMNOPQRST"
numbers = "0123456789"
symbols = "[]{}()@#$%&,.-_*"

all = lower+UPPER+numbers+symbols

length = 16

password = "".join(r

```
This is a Python code for generating a random password. The password consists of lowercase and uppercase letters, numbers, and symbols. The length of the password is set to 16. When you run this code, it will generate a new password every time you execute it. The password will be a string of 16 characters randomly selected from the four different character sets.

Note that the 'all' variable is a string concatenation of all the character sets that the password can be composed of. The 'length' variable defines the length of the password. The 'password' variable is created by joining a random sample of 'length' characters from the 'all' variable using the join() method. Finally, the password is printed to the console.

It is important to note that while this code can generate a random password, it may not necessarily be a strong password. A strong password should ideally have a combination of uppercase and lowercase letters, numbers, and symbols, and should be at least 12 characters long. Additionally, the password should not be based on easily guessable information, such as the user's name or birthdate.

---

### question6.py
**Code**
```python
a = [7]
b = [12]
a = a*2

print ((a == b.extend(b)))

```

The expression a == b.extend(b) will return False because the extend() method does not return anything. When you call a = a*2, you are creating a new list that is twice the size of the original list. When you call b.extend(b), you are appending the contents of the list to itself. This does not change the size of the list, so the two lists are not equal.

---
### question7.py
```python
def numbers():
    yield 1
    yield 2

if __name__ == "__main__":
    x = numbers()
    next(x)
    next(x)
    next(x)

```
In the above code, the numbers() function is a generator function. It yields the values 1 and 2, one at a time. The if __name__ == "__main__" guard clause ensures that the code inside it is only executed when the script is run as the main script.

When the numbers() function is called, it returns a generator object. The next() function is used to iterate over the generator object. The first call to next() yields the value 1. The second call to next() yields the value 2. The third call to next() raises a StopIteration exception because the generator object has been exhausted.

```python
**output of the code:**
1
2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

```

---

### question8.py

**Code**

```python
def function(*args, b=2):
    results = (all(args),b)
    return  sum(results) == b

print(function(7,9,8,0,12, b=8))

```

The function function(*args, b=2) takes any number of positional arguments as *args and a default value of b=2.

In the function body, the variables results is assigned the tuple (all(args), b). Here, the built-in function all() returns True if all elements in the iterable args are true, and False otherwise.

The sum() function is used to add up the values in the tuple (all(args), b), which in this case will be either 0 or 1 plus the value of b.

Finally, the expression sum(results) == b checks if the sum of the tuple is equal to the value of b. The function returns True if this condition is met, and False otherwise.

When the function is called with the arguments function(7,9,8,0,12, b=8), it will return True because all(args) returns True since all the positional arguments are truthy values, and the sum of the tuple (1, 8) is equal to b=8.

Therefore, the output of the code will be True.

---

### questions9.py
**Code**
```python
def function(n):
    result = []
    for i in  range(n):
        result.append(lambda:i*2)
    return result


func = function(3)

for f in func:
    print(f())
    break
```
The code defines a function function that takes an integer n as input and returns a list of n lambda functions. Each lambda function, when called, returns the value of its index in the list multiplied by 2.

When the code calls function(3), it creates a list with 3 lambda functions that return 0, 1, and 2 respectively, each multiplied by 2.

The for loop then iterates over each function in the list and calls it using f(). Since each function returns its index multiplied by 2, the output of the loop will be:

The break statement is unnecessary because it causes the loop to terminate after the first iteration, but since the loop only has one iteration in this case, it doesn't affect the output.

---
### question10.py
**Code**

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)
y = np.sin(x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Wave')
plt.show()

```
The python code uses the NumPy library to create a one-dimensional array of 100 equally spaced values between 0 and 10, and then applies the sine function to each value of the array to obtain the corresponding y values.

Next, the code uses the Matplotlib library to create a line plot of the x and y values, and sets the labels for the x and y axes and the title of the plot.

Finally, the plt.show() function displays the plot.

Overall, this code creates a simple plot of the sine wave function.

---

### question11.py
```python
import  numpy as np
import  pandas as pd

df = pd.Series(np.random.randn(200),
               index=pd.date_range("1/1/2000", periods=200))

df.plot(kind="bar")

```
The code snippet you provided generates a Pandas Series object containing 200 random numbers from a normal distribution, with dates as indices, and then creates a bar plot of the data.

However, since bar plots are typically used to show the distribution of categorical data, it may not be the most appropriate plot type for a continuous variable like the one generated here.

If you want to visualize the distribution of the random numbers in the Series, you could use a histogram instead:

`df.hist()`
This will create a histogram of the data, with the x-axis representing the range of values and the y-axis representing the frequency of those values.

Alternatively, if you want to see how the values change over time, you could use a line plot:

`df.plot()`
This will create a line plot of the data, with the x-axis representing the dates and the y-axis representing the values.

===

### question12.py
**Code:**
```python
from string import Template

def strange_func(n):
    template = Template('$x is not the $y letter')
    result = []

    for i in range(n):
        result.append(lambda x: template.substitute(x=x, y=i))
    return result

funcs = strange_func(4)

for f in funcs:
    print(f('A'))


```
 strange_func creates a list of lambda functions that all reference the same template object. When the lambdas are executed in the loop, they use the current value of i, which is 3 at the end of the loop, for the $y placeholder in the template. So, all of the lambdas in the list will return the same string where 3 is substituted for $y and A is substituted for $x.

To avoid this issue, you could use a closure to capture the current value of i for each lambda, like this:


```python
def strange_func(n):
    result = []

    for i in range(n):
        template = Template('$x is not the $y letter')
        result.append((lambda x, y: template.substitute(x=x, y=y))(i))

    return result

funcs = strange_func(4)

for f in funcs:
    print(f('A'))
```

This should output:

`0 is not the A letter`
`1 is not the A letter`
`2 is not the A letter`
`3 is not the A letter`
In this version of the code, each lambda creates its own template object and passes the current value of i as a parameter to the lambda. This way, the value of i is captured by the lambda at the time it is created and doesn't change later on.

---

### Question13.py
**Code:**
```python

i = lambda i: (i, print('x'))
j = lambda i: i

w = lambda n: (n(0), n(1))

result = f"{(j(1) in i(1))}, {(w(i) == w(j))}"
print(result)

```
`Code output`
`False, True`

The first part of the output, False, is because the value 1 is not in the tuple returned by i(1). The second part of the output, True, is because the functions i and j return the same value for all inputs.

Explanation of the code:

i = lambda i: (i, print('x')) defines a lambda function called i that takes an integer i as input and returns a tuple containing i and the string 'x'. The print() statement is executed immediately when the function is called.
j = lambda i: i defines a lambda function called j that takes an integer i as input and returns i.
w = lambda n: (n(0), n(1)) defines a lambda function called w that takes a function n as input and returns a tuple containing the values returned by calling n with the arguments 0 and 1.
result = f"{(j(1) in i(1))}, {(w(i) == w(j))}" defines a string result that contains the output of the expressions (j(1) in i(1)) and (w(i) == w(j)).
print(result) prints the value of result to the console.

---
### question14.py
**Code**
```python
import matplotlib.pyplot as plt

labels = ('python','katolin', 'C++', 'C', 'java')
index = (1,2,3,4,5)

sizes = [45,5,15,20,30]

plt.ylabel('Usage')
plt.xlabel('Programming Language')

plt.bar(index, sizes)
plt.xticks(index, labels)
plt.show()

```
This code will create a bar graph showing the usage of different programming languages. The x-axis will show the names of the programming languages, and the y-axis will show the usage of each language. The bars will be colored blue.
As you can see, Python is the most popular programming language, followed by Java, C++, C, and Kotlin.

---


### Question15.py


```python

import heapq

results = [65, 59, 89, 89.9999999, 89.899977, 90]

# Finding the 3 largest numbers
largest_numbers = heapq.nlargest(3, results)
print('N largest numbers:', largest_numbers)

# Finding the 3 smallest numbers
smallest_numbers = heapq.nsmallest(3, results)
print('N smallest numbers:', smallest_numbers)

Output:


N largest numbers: [90, 89.9999999, 89.899977]
N smallest numbers: [59, 65, 89]

```
This code, heapq.nlargest(n, iterable) returns a list containing the n largest elements from the iterable (in this case, the results list). Similarly, heapq.nsmallest(n, iterable) returns a list containing the n smallest elements from the iterable.

When you run the code, it will print the n largest numbers and the n smallest numbers from the results list. In this case, it will display the 3 largest and 3 smallest numbers.

Note that if there are multiple numbers with the same value as the n-th largest or smallest element, the function will include them in the result. For example, in this case, 89.9999999 and 89.899977 are both considered as the third largest numbers because they have the same value, so both are included in the result.

---

### Dervatives.ipynb
**Code**

```python
import matplotlib.pyplot as plt
import torch
x = torch.tensor(3.0, requires_grad = True)
print("creating tensor x: ", x)

y = 3 * x ** 2
print("Result of the equation is: ", y)
y.backward()
print("Dervative of the equation at x = 3 is: ", x.grad)    
print('data attribute of the tensor:',x.data)
print('grad attribute of the tensor::',x.grad)
print('grad_fn attribute of the tensor::',x.grad_fn)
print("is_leaf attribute of the tensor::",x.is_leaf)

print("requires_grad attribute of the tensor::",x.requires_grad)
u = torch.tensor(3., requires_grad=True)
v = torch.tensor(4., requires_grad=True)

f = u**3 + v**2 + 4*u*v

print(u)
print(v)
print(f)

f.backward()
print("Partial derivative with respect to u: ", u.grad)
print("Partial derivative with respect to v: ", v.grad)
# compute the derivative of the function with multiple values
x = torch.linspace(-20, 20, 20, requires_grad = True)
Y = x ** 2
y = torch.sum(Y)
y.backward()

# ploting the function and derivative
function_line, = plt.plot(x.detach().numpy(), Y.detach().numpy(), label = 'Function')
function_line.set_color("red")
derivative_line, = plt.plot(x.detach().numpy(), x.grad.detach().numpy(), label = 'Derivative')
derivative_line.set_color("green")
plt.xlabel('x')
plt.legend()
plt.show()

```
Import the required libraries:

`import matplotlib.pyplot as plt`
`import torch`
Here, we import the matplotlib.pyplot module to visualize the function and derivative, and the torch module for tensor operations and automatic differentiation.

Define a tensor x with the value 3.0 and requires_grad set to True:

`x = torch.tensor(3.0, requires_grad=True)`
This creates a scalar tensor x with the value 3.0. By setting requires_grad to True, we enable automatic differentiation to compute gradients with respect to x.

Print the value of x:


`print("creating tensor x:", x)`
This statement prints the value of x to the console.

Define a tensor y that represents an equation involving x:

`y = 3 * x ** 2`
Here, we define y as a tensor representing the equation 3 * x ** 2, which squares x and multiplies it by 3.

Print the result of the equation:

`print("Result of the equation is:", y)`
This statement prints the value of y to the console.

Perform backward propagation to compute the gradients:

`y.backward()`
This line triggers the backward propagation algorithm in PyTorch, which computes the gradients of y with respect to all the tensors that have requires_grad set to True. In this case, it computes the gradient of y with respect to x.

Print the derivative of the equation at x = 3:

`print("Derivative of the equation at x = 3 is:", x.grad)`
This statement prints the computed gradient (derivative) of y with respect to x. It gives you the derivative of the equation at x = 3.

Print various attributes of the tensor x:


`print('data attribute of the tensor:', x.data)`
`print('grad attribute of the tensor:', x.grad)`
`print('grad_fn attribute of the tensor:', x.grad_fn)`
`print("is_leaf attribute of the tensor:", x.is_leaf)`
`print("requires_grad attribute of the tensor:", x.requires_grad)`
These lines print various attributes of the tensor x to provide more information about its properties. data gives the underlying data of the tensor, grad contains the computed gradients, grad_fn refers to the function that generated the tensor (in this case, it's the multiplication operation), is_leaf indicates if the tensor is a leaf node in the computation graph, and requires_grad shows whether the tensor is set to compute gradients.

Define tensors u and v with requires_grad set to True:


`u = torch.tensor(3., requires_grad=True)`
`v = torch.tensor(4., requires_grad=True)`
Here, we create two tensors, u and v, with the values 3.0 and 4.0, respectively. Both tensors are set to compute gradients.

Define a function f involving u and v:


`f = u**3 + v**2 + 4*u*v`

---

### question20.py
**Code:**

```python
import pyfiglet
import random

font = random.choice(pyfiglet.FigletFont.getFonts())
ascii_art = pyfiglet.figlet_format("HAPPY BIRTHDAY TO YOU!", font=font)

greetings = f"\nHAPPY BIRTHDAY TO YOU!\n{ascii_art}"

print(greetings)


```
generate a random ASCII art representation of the phrase "HAPPY BIRTHDAY TO YOU!" using the pyfiglet library. The code looks correct, assuming you have the pyfiglet library installed.

Here's a breakdown of the code:

Importing the necessary modules:

`import pyfiglet`
`import random`
Randomly selecting a font from the available fonts in pyfiglet:

`font = random.choice(pyfiglet.FigletFont.getFonts())`
Generating ASCII art text using the selected font:

`ascii_art = pyfiglet.figlet_format("HAPPY BIRTHDAY TO YOU!", font=font)`
Creating the final birthday greetings message by combining the original phrase and the ASCII art:

`greetings = f"\nHAPPY BIRTHDAY TO YOU!\n{ascii_art}"`
Printing the birthday greetings message:

`print(greetings)`
When executed, this code will output a random ASCII art representation of "HAPPY BIRTHDAY TO YOU!" along with the text "HAPPY BIRTHDAY TO YOU!" on separate lines.


