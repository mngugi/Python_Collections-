# this code deletes files from the directory folder

import os
from tkinter import *

# Create an instance of tkinter window
win = Tk()
win.geometry("700x250")

def Delete_File():
    if os.path.exists("remove3.txt"):
        os.remove("remove3.txt")
    else:
        print("The file does not exist") 
    
Delete_btn = Button(win, text="Delete", command=Delete_File)
Delete_btn.pack()

win.mainloop()
