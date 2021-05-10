from tkinter import *

def tungde(mainHub):
    mainHub.destroy()
    import tyngde.py
 
def dens(mainHub):
    mainHub.destroy()
    import Densitet.py

def energi(mainhub):
    mainHub.destroy()
    import Energi_Visualisering.py


#laver vinduet
mainHub = Tk()



mainHub.geometry('600x400')

space = Label(mainHub, text="                     ")
space2 = Label(mainHub, text="                     ")

mennavn = Label(mainHub, text="Hoved Menu")

space.grid(row=0, column=0)
mennavn.grid(row=0, column=1)
space2.grid(row=0, column=2)

tungButton = Button(mainHub, text="Tyngdekraft", command=lambda: tungde(mainHub))

space.grid(row=1, column=0)
tungButton.grid(row=1, column=1)
space2.grid(row=1, column=2)

densButton = Button(mainHub, text="Densitet", command=lambda: dens(mainHub))

space.grid(row=2, column=0)
densButton.grid(row=2, column=1)
space2.grid(row=2, column=2)

energiButton = Button(mainHub, text="Energi", command=lambda: energi(mainHub))

space.grid(row=3, column=0)
energiButton.grid(row=3, column=1)
space2.grid(row=3, column=2)


mainHub.mainloop()
