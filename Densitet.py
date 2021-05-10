import tkinter as tk

window = tk.Tk()



#Finde densitet med masse og volumen

def findDensitet():

    masse = int()
    volumen = int()

    densitet = masse/volumen

#Finde massen med densiteten og volumen

def findMasse():
    volumen = int()
    densitet = int()

    masse = densitet*volumen

#find volumen

def findVolumen():
    masse = int()
    densitet = int()

    volumen = masse/densitet
