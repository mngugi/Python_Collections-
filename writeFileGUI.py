# this code opens,read, write , saves and overwrites/deletes a text file
from tkinter import *

# Create an instance of tkinter window
win = Tk()
win.geometry("880x450")

def open_text():
   text_file = open("File_Open.txt", "r")
   content = text_file.read()
   my_text_box.insert(END, content)
   text_file.close()

def save_text():
   text_file = open("File_Open.txt", "w")
   text_file.write(my_text_box.get(1.0, END))
   text_file.close()

def write_text():
    text_file = open("File_Open.txt", "a")
    text_file.write("Add a new line of content")
    text_file.close()
    
def overwrite_text():
    text_file = open("File_Open.txt", "w")
    text_file.write("Delete content in the text file")
    text_file.close()

# Creating a text box widget
my_text_box = Text(win, height=10, width=50)
my_text_box.pack()

open_btn = Button(win, text="Open Text File", command=open_text)
open_btn.pack()

# Create a button to save the text
save = Button(win, text="Save File", command=save_text)
save.pack()


write_btn = Button(win, text="write file", command=write_text)
write_btn.pack()

# after this button is pressed the content inside File_Open.txt is overwritten.
overwrite_btn = Button(win, text="overwrite file", command=overwrite_text)
overwrite_btn.pack()

win.mainloop()
