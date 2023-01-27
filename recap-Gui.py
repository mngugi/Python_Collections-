import tkinter as tk
# create the main window
root = tk.Tk()
root.title("Graphical User Interface")

# create label and set of options and variables for the optionMenu
label = tk.Label(root,text= " Niaje Buda!")
options = ("option 1","option 2","option 3")
selected_option = tk.StringVar()
selected_option.set(options[0])
#Lay out label
label.pack()
# create a variable to store options for the Radiobuttons
radio_option = tk.IntVar()
#run forever
root.mainloop()
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
#the Button
 #the Button
import tkinter as tk
root = tk.Tk()
root.title("Graphical User Interface the Button")
def callback():
	print (" Click!")
b = Button(root, text="OK", command=callback)
b.pack()

root.mainloop()
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#the canvas 
import tkinter as tk
root = tk.Tk()
root.title("Graphical User Interface the canvas")
w = Canvas(root, width=200, height=100)
w.pack()
w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")

root.mainloop()
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
#the Checkbutton
import tkinter as tk
root = tk.Tk()
root.title("Graphical User Interface the canvas")
var = IntVar()
#v = IntVar()
chk = Canvas(root,width=200, height=100)
#chk = Canvas(root,text="Don't ask me again")
#chk.var = v
chk.pack()
root.mainloop()
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#the Checkbutton
import tkinter as tk
from tkinter import*
master = tk.Tk()
master.title("Graphical User Interface the canvas")
#Entry = master()
e = Entry()
e.pack()

e.focus_set()

def callback():
    print ( e.get())

b = Button(master, text="get", width=10, command=callback)
b.pack()

master.mainloop()
e = Entry(master, width=50)
e.pack()

text = e.get()
def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

user = makeentry(parent, "User name:", 10)
password = makeentry(parent, "Password:", 10, show="*")
content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
 #Frame Widget
 import tkinter as tk
 from tkinter import *

master = tk.Tk()

Label(text="one").pack()

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

Label(text="two").pack()
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

master.mainloop()
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#LabelFrame Widget
from tkinter import *

master = tk.Tk()

group = LabelFrame(master, text="Group", padx=5, pady=5)
group.pack(padx=10, pady=10)

w = Entry(group)
w.pack()

master.mainloop()
  ==================================================
  #LabelFrame Widget
from tkinter import *

master = tk.Tk()

group = LabelFrame(master, text="Group", padx=5, pady=5)
group.pack(padx=10, pady=10)
w = Entry(group)
w.pack()
group = LabelFrame(master, text="Users", padx=5, pady=5)
group.pack(padx=10, pady=10)
w = Entry(group)
w.pack()

master.mainloop()
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Listbox Widget
from tkinter import *

master = tk.Tk()

listbox = Listbox(master)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

master.mainloop()
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#The Tkinter Listbox Widget
from tkinter import *

master = tk.Tk()

listbox = Listbox(master)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)
  
lb = Listbox(master)
b = Button(master, text="Delete",
           command=lambda lb=lb: lb.delete(ANCHOR))

master.mainloop()

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
# The Tkinter Menu Widget
import tkinter as tk
root = tk.Tk()

def hello():
    print ("hello!")

menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)
root.mainloop()
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#the message box
import tkinter as tk
from tkinter import *
master = tk.Tk()
w = Message(master , text = "this is a message box", width=80 )
w.pack()
master.mainloop()
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# The Tkinter OptionMenu Widget
import tkinter as tk
from tkinter import *
master = tk.Tk()
variable = StringVar(master)
variable.set("one") # default value
w = Message(master,width=80, height=80 )
w.pack()
w = OptionMenu(master, variable, "one", "two", "three")
w.pack()
master.mainloop()
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#The Tkinter PanedWindow Widget
import tkinter as tk
from tkinter import *
master = tk.Tk()
m = PanedWindow(orient=VERTICAL)
m.pack(fill=BOTH, expand=1)

top = Label(m, text="top pane")
m.add(top)

bottom = Label(m, text="bottom pane")
m.add(bottom)
master.mainloop()
----------------------------------------------------
#The Tkinter PanedWindow Widget
import tkinter as tk
from tkinter import *
master = tk.Tk()
m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left pane")
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top = Label(m2, text="top pane")
m2.add(top)
m4= PanedWindow(m1,orient=HORIZONTAL)
m1.add(m4)
right = Label(m4, text="right pane")
m4.add(right)

bottom = Label(m2, text="bottom pane")
m2.add(bottom)
master.mainloop()
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#The Tkinter Radiobutton Widget
import tkinter as tk
from tkinter import *
master = tk.Tk()
v = IntVar()

Radiobutton(master, text="One", variable=v, value=1).pack(anchor=W)
Radiobutton(master, text="Two", variable=v, value=2).pack(anchor=W)
MODES = [
        ("Monochrome", "1"),
        ("Grayscale", "L"),
        ("True color", "RGB"),
        ("Color separation", "CMYK"),
    ]

v = StringVar()
v.set("L") # initialize

for text, mode in MODES:
    b = Radiobutton(master, text=text,
                        variable=v, value=mode)
    b.pack(anchor=W)
master.mainloop()
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#The Tkinter Scale Widget
import tkinter as tk
from tkinter import *
master = tk.Tk()
w = Scale(master, from_=0, to=100)
w.pack()

w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
print (w.get())
master.mainloop()
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#The Tkinter Toplevel Widget
import tkinter as tk
from tkinter import *
master = tk.Tk()
top = Toplevel()
top.title("About this application...")

msg = Message(top, text="about_message")
msg.pack()

button = Button(top, text="Dismiss", command=top.destroy)
button.pack()
master.mainloop()
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#The Tkinter Scrollbar Widget
import tkinter as tk
from tkinter import *
master = tk.Tk()
scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(master, yscrollcommand=scrollbar.set)
for i in range(1000):
    listbox.insert(END, str(i))
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)
master.mainloop()
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#The Tkinter Spinbox Widget
import tkinter as tk
from tkinter import *
master = tk.Tk()
w = Spinbox(master, from_=0, to=10)
w.pack()
master.mainloop()
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 #The Tkinter Grid Geometry Manager
import tkinter as tk
from tkinter import *
master = tk.Tk()
Label(master, text="First").grid(row=0, sticky=W)
Label(master, text="Second").grid(row=1, sticky=W)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
master.mainloop()
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#The Tkinter Grid Geometry Manager
import tkinter as tk
from tkinter import *
master = tk.Tk()
label1.grid(sticky=E)
label2.grid(sticky=E)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

checkbutton.grid(columnspan=2, sticky=W)

image.grid(row=0, column=2, columnspan=2, rowspan=2,
sticky=W+E+N+S, padx=5, pady=5)

button1.grid(row=2, column=2)
button2.grid(row=2, column=3)
master.mainloop()
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#All together in one 
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My GUI")

# Create a set of options and variable for the OptionMenu
options = ["Option 1", "Option 2", "Option 3"]
selected_option = tk.StringVar()
selected_option.set(options[0])

# Create a variable to store options for the Radiobuttons
radio_option = tk.IntVar()

###############################################################################
# Create widgets

# Create widgets
button = tk.Button(root, text="Button")
canvas = tk.Canvas(root, bg='white', width=50, height=50)
checkbutton = tk.Checkbutton(root, text="Checkbutton")
entry = tk.Entry(root, text="Entry", width=10)
frame = tk.Frame(root)
label = tk.Label(root, text="Label")
labelframe = tk.LabelFrame(root, text="LabelFrame", padx=5, pady=5)
listbox = tk.Listbox(root, height=3)
menu = tk.Menu(root)
# Menubutton: deprecated, use Menu instead
message = tk.Message(root, text="Message", width=50)
optionmenu = tk.OptionMenu(root, selected_option, *options)
panedwindow = tk.PanedWindow(root, sashrelief=tk.SUNKEN)
radiobutton_1 = tk.Radiobutton( root, 
                                text="Option 1", 
                                variable=radio_option,
                                value=1)
radiobutton_2 = tk.Radiobutton( root, 
                                text="Option 2", 
                                variable=radio_option, 
                                value=2)
scale = tk.Scale(root, orient=tk.HORIZONTAL)
scrollbar = tk.Scrollbar(root)
spinbox = tk.Spinbox(root, values=(0, 2, 4, 10))
text = tk.Text(root, width=15, height=3)
toplevel = tk.Toplevel()

# Lay out widgets
button.pack(padx=5, pady=5)
canvas.pack(padx=5, pady=5)
checkbutton.pack(padx=5, pady=5)
entry.pack(padx=5, pady=5)
frame.pack(padx=5, pady=10)
label.pack(padx=5, pady=5)
labelframe.pack(padx=5, pady=5)
listbox.pack(padx=5, pady=5)
# Menu: See below for adding the menu bar at the top of the window
# Menubutton: deprecated, use Menu instead
message.pack(padx=5, pady=5)
optionmenu.pack(padx=5, pady=5)
panedwindow.pack(padx=5, pady=5)
radiobutton_1.pack(padx=5)
radiobutton_2.pack(padx=5)
scale.pack(padx=5, pady=5)
scrollbar.pack(padx=5, pady=5)
spinbox.pack(padx=5, pady=5)
text.pack(padx=5, pady=5)
# Toplevel: does not have a parent or geometry manager, as it is its own window

###############################################################################
# Add stuff to the widgets (if necessary)

# Draw something in the canvas
canvas.create_oval(5, 15, 35, 45, outline='blue')
canvas.create_line(10, 10, 40, 30, fill='red')

# Add a default value to the Entry widgets
entry.insert(0, "Entry")

# Create some useless buttons in the LabelFrame
button_yes = tk.Button(labelframe, text="YES")
button_no = tk.Button(labelframe, text="NO")

# Lay out buttons in the LabelFrame
button_yes.pack(side=tk.LEFT)
button_no.pack(side=tk.LEFT)

# Put some options in the Listbox
for item in ["Option 1", "Option 2", "Option 3"]:
    listbox.insert(tk.END, item)

# Add some options to the menu
menu.add_command(label="File")
menu.add_command(label="Edit")
menu.add_command(label="Help")

# Add the menu bar to the top of the window
root.config(menu=menu)

# Create some labels to add to the PanedWindow
label_left = tk.Label(panedwindow, text="LEFT")
label_right = tk.Label(panedwindow, text="RIGHT")

# Add the labels to the PanedWindow
panedwindow.add(label_left)
panedwindow.add(label_right)

# Put some default text into the Text widgets
text.insert(tk.END, "I am a\nText widget")

# Create some widgets to put in the Toplevel widget (window)
top_label = tk.Label(toplevel, text="A Toplevel window")
top_button = tk.Button(toplevel, text="OK", command=toplevel.destroy)

# Lay out widgets in the Toplevel pop-up window
top_label.pack()
top_button.pack()

###############################################################################
# Run!

root.mainloop()
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 from tkinter import *

canvas_width = 500
canvas_height = 150

def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   w.create_oval( x1, y1, x2, y2, fill = python_green )

master = Tk()
master.title( "Painting using Ovals" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )

message = Label( master, text = "Press and Drag the mouse to draw", font= ("Arial", 14 , "bold") )
message.pack( side = BOTTOM )

mainloop()
