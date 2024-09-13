
# Script Name: calculator.py
# Author: Mwangi
# Purpose: This script prompts the user to enter two numbers, then performs addition
#          using the add_TwoNumbers() function, and prints the result.
# Usage: The user is expected to input two space-separated integers when prompted.
#        The script will then display the sum of the two numbers.


def add(*numbers: float) -> float:
    return sum(numbers)

print(add(52,63,98))    