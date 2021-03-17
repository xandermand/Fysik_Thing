from tkinter import *
from subprocess import Popen

def tyngde():
    Popen('python tyngde.py')

#laver vinduet
mainHub = Tk()

hub = Label(mainHub, text="hello world")

hub.grid(row=0, column=0)

densButton = Button(mainHub, text="rør ved mig", command=tyngde)

densButton.grid(row=1, column=0)

mainHub.mainloop()
