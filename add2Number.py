
'''
Spyder Editor
Author : Mwangi
Purpose : Enter two numbers and per addition using a
add_TwoNumbers() function.
'''
user_input = input("Enter Two Numbers: ") # input method.

def add_TwoNumbers(i,j): # creating a add_TwoNumbers() function
    return i + j

# split the numbers into 2 parts
numbers = user_input.split()
num1 = int(numbers[0]) # numbers at the first position
num2 = int(numbers[1]) # numbers at the second position


print(add_TwoNumbers(i = num1, j=num2)) # print tht results
