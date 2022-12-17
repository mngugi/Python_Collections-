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


    
    
    
     
     
