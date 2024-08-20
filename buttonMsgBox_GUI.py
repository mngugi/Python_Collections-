# this code displays a message in a message box


from tkinter import *
import tkinter as tk
from tkinter import messagebox

r = tk.Tk()

def echoPhraseInMsgBox():
    return messagebox.showinfo("Button Pressed")
   

def echoText():
    return messagebox.showwarning("Type the correct command!")

button = tk.Button(r, text='Print',background='blue',foreground='yellow', width=25, command=echoPhraseInMsgBox)

label_1 = tk.Label(r, text="print", fg='white', bg='red', width=25, height=20, command=echoText )

button.pack()
label_1()
r.mainloop()

