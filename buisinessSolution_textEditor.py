from tkinter import *
#need to install on all machines
from tkmacosx import Button
import tkinter as tk 

# Create the main window
root = Tk()
root.title("Meeting Notes")

#Set size of window


# Create buttons
underscore = Button(root, text="Red", background='red')
bold = Button(root,text="Yellow", background='yellow')
italics= Button(root,text='Green',background='green')
#Add a label
label = Label(root, text = "What color is the light?!")
textarea = tk.Text(root, width = 50, height = 10, wrap="word")


# Place widgets in window (with pack function!)
l = Label(root, text = "text box")
T = Text(root, height = 5, width = 52)
underscore.grid(row=0, column=0)	


bold.grid(row=0, column=1 )
italics.grid(row=0, column=2)
label.grid(row= 1, column= 1)
T.grid(row = 1, column =1, columnspan=2)

# Start the GUI event loop
root.mainloop()
tk.mainloop()