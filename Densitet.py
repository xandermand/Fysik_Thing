import tkinter as tk
from subprocess import Popen




#Vindue
vindue = tk.Tk()

forklaring = tk.Label(text="Tryk på den tekstboks der indeholder den information du har")

#densitet/volumen
def mulighed1(vindue):
    vindue.destroy()
    import Densitet_og_volumen.py
    
    
d_og_v = tk.Button(text = "Densitet og volumen", command = lambda: mulighed1 (vindue))


#masse/densitet

def mulighed2(vindue):
    vindue.destroy()
    import masse_og_densitet.py
    

m_og_d = tk.Button(text = "Masse og densitet", command = lambda: mulighed2 (vindue))


#masse/Volumen

def mulighed3(vindue):
    vindue.destroy()
    import Masse_og_volumen.py

m_og_v = tk.Button(text = "Masse og volumen", command = lambda: mulighed3(vindue))


#Packs

forklaring.pack()
d_og_v.pack()
m_og_d.pack()
m_og_v.pack()

vindue.geometry("600x400")
vindue.mainloop()


