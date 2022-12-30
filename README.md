# Python-Level-One-O-One
Active Pythoner , exploring python functions def() : 


The following snippets are basic level of python programming,these excercises use functions.
A function is a block of code designed to perform specific tasks.
A Function has three component that is . Header(def), Body(e.g name_func()) and Call (print) function.


tryExcept.py
Code:

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
The code you have provided is a basic implementation of a try-except block in Python. The try block contains the code that might throw an exception, and the except block contains the code that will handle the exception if it is raised.

In this case, the try block is attempting to cast the user's input to an integer using the int() function. If the input cannot be cast to an integer (for example, if the user enters a string or a float), a ValueError will be raised. The except block will catch this error and print a message to the user, telling them to try again.

This is a useful way to handle errors and ensure that your code continues to run smoothly even if something goes wrong. You can use try-except blocks to handle a wide variety of errors, including syntax errors, type errors, and other exceptions that might occur while your code is running.tryExcept.py
Code:

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
The code you have provided is a basic implementation of a try-except block in Python. The try block contains the code that might throw an exception, and the except block contains the code that will handle the exception if it is raised.

In this case, the try block is attempting to cast the user's input to an integer using the int() function. If the input cannot be cast to an integer (for example, if the user enters a string or a float), a ValueError will be raised. The except block will catch this error and print a message to the user, telling them to try again.

This is a useful way to handle errors and ensure that your code continues to run smoothly even if something goes wrong. You can use try-except blocks to handle a wide variety of errors, including syntax errors, type errors, and other exceptions that might occur while your code is running.
