from tkinter import *
from tkinter.ttk import *
import matplotlib.pyplot as plt
from subprocess import Popen
import math

#laver vores vindue
tungHub = Tk()
#sætter vores valgbox op
tungHub.geometry('600x700')
comb = Combobox(tungHub, state='readonly')
comb['values']=("Vælg en værdi",
                "Jorden",
                "Månen",
                "Jupiter",
                "Mekur",
                "Venus",
                "Angiv selv en tyngdeacceleration")
comb.current(1)

selvvalg = Entry(tungHub)
selvtekst = Label(tungHub, text="Skriv her hvis du skal bruge en selvvalgt acceleration i m/s^2")
længde = Entry(tungHub)
fald = Label(tungHub, text="Skriv hvor langt objektet falder i meter")
def bpress():
    currval = comb.get()
    leng = længde.get()
    if currval == "Jorden":
        tacc = 9.78/2
    elif currval == "Månen":
        tacc = 1.62
    elif currval == "Jupiter":
        tacc = 24.79
    elif currval == "Mekur":
        tacc = 3.7
    elif currval == "Venus":
        tacc = 8.87
    elif currval == "Angiv selv en tyngdeacceleration":
        tacc = float(selvvalg.get())
    res = float(leng)/tacc
    time = math.sqrt(res)
    reslab = Label(tungHub, text="Det tager " + str(time) + " sekunder for objektet at falde fra " + str(leng) + " meters højde med en tyngdeacceleration på " + str(tacc))
    reslab.grid(column=0, row=7)
    plt.plot(leng, time, 'go--')

    

space = Label(tungHub, text="                     ")
space2 = Label(tungHub, text="                     ")

tungvalg = Label(tungHub, text="Vælg en tyngeacceleration")

funkt = Button(tungHub, text="Click her", command=bpress)




tungvalg.grid(column=0, row=0)
comb.grid(column=0, row=1)
fald.grid(column=0, row=2)
længde.grid(column=0, row=3)
selvtekst.grid(column=0, row=4)
selvvalg.grid(column=0, row=5)
funkt.grid(column=0, row=6)
tungHub.mainloop()
