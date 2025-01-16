import nltk
from rich.console import Console
from rich.text import Text

import pyfiglet # type: ignore

def display_title(title):
    ascii_art = pyfiglet.figlet_format(title)
    print(ascii_art)

if __name__ == "__main__":
    display_title("Add Two Numbers")
'''
# Script Name: add_two_numbers.py
# Author: Mwangi
# Purpose: This script prompts the user to enter two numbers, then performs addition
#          using the add_TwoNumbers() function, and prints the result.
# Usage: The user is expected to input two space-separated integers when prompted.
#        The script will then display the sum of the two numbers.
#
# Function: add_TwoNumbers(i, j)
#   - Description: Takes two integers and returns their sum.
#   - Parameters:
#       - i (int): The first integer.
#       - j (int): The second integer.
#   - Returns:
#       - int: The sum of the two integers.
#
# Example:
#   Input: 5 10
#   Output: 15

'''
user_input = input("Enter Two Numbers: ") # input method.
console = Console()

def add_TwoNumbers(i,j): # creating a add_TwoNumbers() function

    """
       Function to add two numbers.
       Args:
           i (int): First number
           j (int): Second number
       Returns:
           int: Sum of the two numbers
       """
    return i + j

# split the numbers into 2 parts
numbers = user_input.split()
num1 = int(numbers[0]) # numbers at the first position
num2 = int(numbers[1]) # numbers at the second position

text = Text(style="bold orange")
print(add_TwoNumbers(i = num1, j=num2)) # print tht results
