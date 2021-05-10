import tkinter as tk
from PIL import ImageTk,Image

vindue = tk.Tk()

talliste = [1, 1200, 4184, 12000000, 31536000, 1000000000, 10000000000]

#1 joule = 1 newton kraft over 1 meter afstand
def joule_1():
    billede1 = ImageTk.PhotoImage(Image.open("1_joule.png"))
    label1 = tk.Label(image = billede1)
    label1.pack()


#1200 joule = den mængde  energi det tager at varme 1 kg vand med 1 grad celsious. 


#4184 joules = 1 Calorie

#1 gram kul = 29308 joule


#12000000 j = cirka daglige menneskelige behov. 


#liter of gasoline = 31,536,000 joules


#1,000,000,000 joules = lynnedslag


mængde = tk.Entry()


def find(mængde, vindue):
    joule =int( mængde.get())

    joule = talliste[min(range(len(talliste)), key = lambda i: abs(talliste[i]-joule))]

    print(joule)



    if int(joule) == 1:
        vindue.destroy()

        vindue = tk.Tk()
        
        billede = ImageTk.PhotoImage(Image.open("1_joule.jpg"))
        label = tk.Label(image = billede)
        label.pack()

        vindue.geometry("600x400")
        vindue.mainloop()

    
        

vis_joule = tk.Button(text = "Tryk her, for at finde ud af hvad du kan bruge den mængde energi du har indtastet til", command = lambda: find(mængde, vindue))



mængde.pack()
vis_joule.pack()

vindue.geometry("600x400")
vindue.mainloop()
