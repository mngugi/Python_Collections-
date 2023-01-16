# In this code a function echoPhrase() is created and
# it is called by the press of a button in other words 
# a button can be used for argument parsing.
# This code also demonstrates customization of functions in python.


from tkinter import *
import tkinter as tk

r = tk.Tk()
def echoPhrase():
    print("Echoed message is, Button Pressed")

r.title('Buttons')
button = tk.Button(r, text='Print', width=25, command=echoPhrase)

button.pack()
r.mainloop()

