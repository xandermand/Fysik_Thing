import tkinter as tk


#Vindue
vindue = tk.Tk()

Introduktion = tk.Label(text="Indtast din information herunder. Husk at bruge komma, og ikke punktum.")



masse = tk.Entry(text = "Skriv massen her")
masse.insert(0,"Masse")


volumen = tk.Entry(text = "Skriv volumen her")
volumen.insert(0,"Volumen")


#Knap
def udregn(masse, volumen):
    m = masse.get()
    v = volumen.get()

    try:
        svar_før_afrunding = float(m)/float(v)
    except:
        fejl = tk.Label(text = "Der er opstået en fejl. Sørg for at du har skrevet tal med punktum, og ikke med komma")
        fejl.pack()
      
    svar = round(svar_før_afrunding, 3)
    resultat = tk.Label(text ="Densiteten er på " + str(svar))
    resultat.pack()

find_masse = tk.Button(text = ("Klik her for at udregne massen ud fra den givne densitet og volumen"),
    command = lambda: udregn (masse, volumen)
)

#Packs
Introduktion.pack()
masse.pack()
volumen.pack()
find_masse.pack()


vindue.geometry("600x400")
vindue.mainloop()


