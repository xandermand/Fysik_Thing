import tkinter as tk
from PIL import ImageTk,Image

vindue = tk.Tk()

talliste = [1, 1200, 4184, 12000000, 31536000, 1000000000, 10000000000]

#1 joule = 1 newton kraft over 1 meter afstand
def joule_1():
    tekst1 = tk.Label(text = "1 joule er defineret som den mængde arbejde det kræver at bevæge 1 newton med 1 meters afstand.")
    billede1 = ImageTk.PhotoImage(Image.open("løft.jpg"))
    label1 = tk.Label(image = billede1)
    tekst1.pack()
    label1.pack()
    vindue.geometry("600x400")
    vindue.mainloop()


#1200 joule = den mængdeenergi det tager at varme 1 kg vand med 1 grad celsious. 

def joule_2():
    tekst2 = tk.Label(text = "1200 joule er den mængde arbejde det kræver at varme 1 kg vand med 1 grad celsious")
    billede2 = ImageTk.PhotoImage(Image.open("vand_koge.jpeg"))
    label2 = tk.Label(image = billede2)
    tekst2.pack()
    label2.pack()
    vindue.geometry("600x400")
    vindue.mainloop()
    

#4184 joules = 1 Calorie

def joule_3():
    tekst3 = tk.Label (text = "4181 joule er den mængde energi der er i en Kalorie, også kaldet en kcal")
    billede3 = ImageTk.PhotoImage(Image.open("kcal.png"))
    label3 = tk.Label(image = billede3)
    tekst3.pack()
    label3.pack()
    vindue.geometry("600x400")
    vindue.mainloop()

#1 gram kul = 29308 joule

def joule_4():
    tekst4 = tk.Label (text = "29308 joule er den mængde energi der er i 1 gram kul")
    billede4 = ImageTk.PhotoImage(Image.open("kul.jpeg"))
    label4 = tk.Label(image = billede4)
    tekst4.pack
    label4.pack()
    vindue.geometry("600x400")
    vindue.mainloop()

#12000000 j = cirka daglige menneskelige behov. 

def joule_5():
    tekst5 = tk.Label (text = "12000000 joules er crika den mængde energi, en menneskekrop har brug for dagligt")
    billede5 = ImageTk.PhotoImage(Image.open("menneskekrop.jpeg"))
    label5 = tk.Label(image = billede5)
    tekst5.pack()
    label5.pack()
    vindue.geometry("600x400")
    vindue.mainloop()


#liter of gasoline = 31,536,000 joules

def joule_6():
    tekst6 = tk.Label (text = "31,536,000 joules er cirka den mængde energi der er i en liter benzin")
    billede6 = ImageTk.PhotoImage(Image.open("benzin.jpeg"))
    label6 = tk.Label(image = billede6)
    tekst6.pack()
    label6.pack()
    vindue.geometry("600x400")
    vindue.mainloop()

#1,000,000,000 joules = lynnedslag

def joule_7():
    tekst7 = tk.Label (text = "1,000,000,000 joules er cirka den mængde energi der er i et lynnedslag")
    billede7 = ImageTk.PhotoImage(Image.open("lyn.jpeg"))
    label7 = tk.Label(image = billede7)
    tekst7.pack()
    label7.pack()
    vindue.geometry("600x400")
    vindue.mainloop()

mængde = tk.Entry()


def find(mængde, vindue):
    joule = int(mængde.get())

    joule = talliste[min(range(len(talliste)), key = lambda i: abs(talliste[i]-joule))]

    print(joule)

    vindue.destroy()

    vindue = tk.Tk()
    #vindue.pack_propagate(0)

    if int(joule) == 1:
        
        joule_1()

    elif int(joule) == 1200:

        joule_2()

    elif int(joule) == 4184:

        joule_3()

    elif int(joule) == 29308:

        joule_4()
        
    elif int(joule) == 12000000:

        joule_5()
        
    elif int(joule) == 31536000:

        joule_6()
        
    elif int(joule) == 1000000000:

        joule_7()
        

vis_joule = tk.Button(text = "Tryk her, for at finde ud af hvad du kan bruge den mængde energi du har indtastet til", command = lambda: find(mængde, vindue))

intro = tk.Label(text = "Indtast en mængde energi i joules.")

intro.pack()
mængde.pack()
vis_joule.pack()

vindue.geometry("600x400")
vindue.mainloop()
