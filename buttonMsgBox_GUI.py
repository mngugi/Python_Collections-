# this code displays a message in a message box


from tkinter import *
import tkinter as tk
from tkinter import messagebox

r = tk.Tk()

def echoPhraseInMsgBox():
    return messagebox.showinfo("Button Pressed")
   


button = tk.Button(r, text='Print', width=25, command=echoPhraseInMsgBox)

button.pack()
r.mainloop()

