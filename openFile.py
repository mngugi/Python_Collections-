# this code demonstrates opening of files in python 
# the code only allows the user to open and read txt files.

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile

r = Tk()
# this function will open a text file only after button is pressed
def open_file():
    f = askopenfile(mode ='r', filetypes =[('text file', '*.txt')]) #only txt files will be opened
     if f is not None:
        content = f.read()
        print(content)
#Below code is reuseable in the event of opening a file is required
#with open("File_Open.txt", "r") as f:
#    Label(r, text=f.read()).pack()

bt= Button(r, text='Read', command= open_file)
bt.pack(side = TOP, pady = 50)    
    
    

r.mainloop()
