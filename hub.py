from tkinter import *
from subprocess import Popen
#åbner et andet program
def tungde():
    Popen('python tyngde.py')

#laver vinduet
mainHub = Tk()

space = Label(mainHub, text="           ")
space2 = Label(mainHub, text="           ")

mennavn = Label(mainHub, text="Hoved Menu")

space.grid(row=0, column=0)
mennavn.grid(row=0, column=1)
space2.grid(row=0, column=2)

densButton = Button(mainHub, text="Tyngdekraft", command=tungde)

space.grid(row=1, column=0)
densButton.grid(row=1, column=1)
space2.grid(row=1, column=2)

mainHub.mainloop()
