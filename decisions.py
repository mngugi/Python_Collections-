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

'''
this part referenced from 
https://www.geeksforgeeks.org/decision-making-python-else-nested-elif/
if (condition1):
   # Executes when condition1 is true
   if (condition2): 
      # Executes when condition2 is true
   # if Block is end here
# if Block is end here
'''

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