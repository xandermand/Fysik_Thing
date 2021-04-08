from tkinter import *
from tkinter.ttk import *
#import matplotlib.pyplot as plt
from subprocess import Popen

#laver vores vindue
tungHub = Tk()
#sætter vores valgbox op
comb = Combobox(tungHub)
comb['values']=("Vælg en værdi", "Jorden", "Månen", "Jupiter", "Mekur", "Venus", "Angiv selv en tyngdeacceleration")
comb.current(0)

space = Label(tungHub, text="                     ")
space2 = Label(tungHub, text="                     ")


comb.grid(column=0, row=0)

tungHub.mainloop()
