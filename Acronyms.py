# Your updated Python code here
# Python Acronyms Dictionary

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
print("Python Acronyms and Their Meanings:\n")
for acronym, meaning in acronyms.items():
    print(f"{acronym}: {meaning}")
