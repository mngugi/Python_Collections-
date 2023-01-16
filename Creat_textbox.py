# code creates a textbox
import tkinter as tk
from tkinter import *

win = Tk()
win.resizable(False, False)
win.title("Text Box Widget")

text = Text(win, height=10)
text.pack()

win.mainloop()
