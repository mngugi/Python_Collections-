# Your updated Python code here
# Python Acronyms Dictionary
import pyfiglet # type: ignore
from rich.console import Console
from rich.text import Text 

def display_title(title):
    ascii_art = pyfiglet.figlet_format(title)
    print(ascii_art)

if __name__ == "__main__":
    display_title("Python Acronyms")

'''
# Script Name: add_two_numbers.py
# Author: Mwangi
# Purpose: This program print pythons acronyms 
# Example:
#PEP: Python Enhancement Proposal
GIL: Global Interpreter Lock
CPython: C implementation of Python
IDLE: Integrated Development and Learning Environment
PyPI: Python Package Index
Pandas: Panel Data
SciPy: Scientific Python
Django: Named after Django Reinhardt, jazz guitarist
Flask: A lightweight web framework in Python
JSON: JavaScript Object Notation

'''

acronyms = {
    "PEP": "Python Enhancement Proposal",
    "GIL": "Global Interpreter Lock",
    "CPython": "C implementation of Python",
    "IDLE": "Integrated Development and Learning Environment",
    "PyPI": "Python Package Index",
    "Pandas": "Panel Data",
    "SciPy": "Scientific Python",
    "Django": "Named after Django Reinhardt, jazz guitarist",
    "Flask": "A lightweight web framework in Python",
    "JSON": "JavaScript Object Notation",
    
}

# Print Acronyms
# creat a console 
console = console()
print("Python Acronyms and Their Meanings:\n")
for acronym, meaning in acronyms.items():
    text = Text(f"{acronym}: {meaning}", style="bold green")
    print(f"{acronym}: {meaning}")
    console.print(text)
