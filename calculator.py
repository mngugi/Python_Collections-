
# Script Name: calculator.py
# Author: Mwangi
# Purpose: This script prompts the user to enter many numbers, then performs addition or sum
#          using the add() function, and prints the result.
# Usage: the program is also a module for the subsequent programm CalculateSum.py
#
#


def add(*numbers: float) -> float:
    return sum(numbers)
   
    if __name__ == ' __main__ ':

        print(add(52,63,98))    