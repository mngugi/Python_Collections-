
# In this code a function echoPhrase() is created and
# it is called by the press of a button in other words 
# a button can be used for argument parsing.
# This code also demonstrates customization of functions in python.


from tkinter import *
import tkinter as tk

r = tk.Tk()
def echoPhrase():
    print("Echoed message is, Button Pressed")

def echo_phrase1():
    print("Second button works okay")    

def  echo_phrase_2():
    print("This is the third button ")  

r.title('Buttons')
button  = tk.Button(r, text='Print', width=25, command=echoPhrase)
button2 = tk.Button(r, text='Print', width=25, command=echo_phrase1)
button3 = tk.Button(r, text= 'Print', width=25, command=echo_phrase_2)

button.pack()
button2.pack()
button3.pack()

r.mainloop()

