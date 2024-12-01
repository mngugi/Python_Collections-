# Script Name: Area_Circle.py
# Author: Mwangi
# Purpose: This snippet creates a class called Car.
# Usage: For example the expected outcome is :
#
# 
# 
# 
#
# 
# a class called car.

class Car:
    def printSize(self):
        print("small")

class Hatch_Back(Car):
    def printSize(self):
        super().printSize()
        print("medium")

hatch = Hatch_Back()
hatch.printSize()
    
