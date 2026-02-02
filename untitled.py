from tkinter import *
#need to install on all machines
from tkmacosx import Button
import tkinter as tk py
def openFile():
	with open('Meeting Notes', 'r+') as file:
		content = file.read()
		file.write('\nThis is a new line.')
# Create the main window
root = Tk()
root.title("Meeting Notes")

#Set size of window

# Create buttons
underscore = Button(root, background='white',text = "underscore")
bold = Button(root, background='white', text = "Bold")
italics= Button(root,background='white',text = "Italics")
#Add a label
label = Label(root, text = "What color is the light?!")
textarea = tk.Text(root, width = 50, height = 10, wrap="word")
File = Button(root, text = "Save & Open File", command = openFile)
# Place widgets in window (with pack function!)
l = Label(root, text = "text box")
T = Text(root, height = 5, width = 52)
underscore.grid(row=0, column=0)	


File.grid(row=2, column=2)
bold.grid(row=0, column=1 )
italics.grid(row=0, column=2)
label.grid(row= 1, column= 1)
T.grid(row = 1, column =1, columnspan=2)

# Start the GUI event loop
root.mainloop()
tk.mainloop()

