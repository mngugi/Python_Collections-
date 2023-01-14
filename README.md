# Python_Programming
Active Pythoner , exploring python functions def() : 


The following snippets are basic level of python programming,these excercises use functions.
A function is a block of code designed to perform specific tasks.
A Function has three component that is . Header(def), Body(e.g name_func()) and Call (print) function.

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

This code you have provided is a simple script that takes user input and assigns it to the variable `x`. The variable `x` is then converted to an integer and assigned to the variable `z`, and is also converted to a float and assigned to the variable `w`. The variable `y` is assigned the string value '`x is ineger`' (note the typo in the string).

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
The code you have provided is a basic implementation of a `try-except` block in Python. The try block contains the code that might throw an exception, and the except block contains the code that will handle the exception if it is raised.

In this case, the try block is attempting to cast the user's input to an integer using the `int()` function. If the input cannot be cast to an integer (for example, if the user enters a string or a float), a `ValueError` will be raised. The except block will catch this error and print a message to the user, telling them to try again.

This is a useful way to handle errors and ensure that your code continues to run smoothly even if something goes wrong. You can use try-except blocks to handle a wide variety of errors, including syntax errors, type errors, and other exceptions that might occur while your code is running.

