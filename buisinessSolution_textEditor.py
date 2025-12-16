from tkinter import *
#need to install on all machines
from tkmacosx import Button
import tkinter as tk 

# Create the main window
root = Tk()
root.title("Enter Title Here")

#Set size of window


# Create buttons
red_button = Button(root, text="Red", background='red')
yellow_button = Button(root,text="Yellow", background='yellow')
green_button= Button(root,text='Green',background='green')
#Add a label
label = Label(root, text = "What color is the light?!")
textarea = tk.Text(root, width = 50, height = 10, wrap="word")


# Place widgets in window (with pack function!)
l = Label(root, text = "text box")
T = Text(root, height = 5, width = 52)
red_button.grid(row=0, column=0)	


yellow_button.grid(row=0, column=1 )
green_button.grid(row=0, column=2)
label.grid(row= 1, column= 1)
T.grid(row = 1, column =1, columnspan=2)

# Start the GUI event loop
root.mainloop()
tk.mainloop()