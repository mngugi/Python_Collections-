# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:47:20 2019

Author:Mwangi
Purpose: Lists ,Sets and Dictionaries in Python
- A list is a container which we used to store multiple data
- Set is also another python collection data type. Set’s can’t have duplicates.
- Dictionary is also a python collection data type. These are unordered, changeable 
- and indexed. In python dictionaries are written using curly brackets. “{}”. Dictionaries have keys and values.
"""
print("---------Lists----------\n")

Lists_Participants = [10,21,23,36,25,14,78,96,85,74,41,52,63,30,20,]
print (Lists_Participants)
print(Lists_Participants[2])
print(Lists_Participants[7])
print(Lists_Participants[5])
print(Lists_Participants[9])

print("---------Sets----------\n")

names = {'Ben','Penalty', 'Curtis', 'Yidah','Curtis', 'Everton', 'Yidah'}
for i in names:
    print(i)
    

print("---------Dictionaries----------\n")

names = {'Ben - ':'Male ','Penalty - ':'Sports', 'Curtis - ':'Male', 'Yidah - ':'Player','Curtis - ':'Boy','Everton - ':'Club', 'Yidah - ':'Man'}
for i, j  in names.items():
    print(i+j)


