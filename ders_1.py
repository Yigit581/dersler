import tkinter as tk
import random

root = tk.Tk()
root.title("ilk projem")

root.geometry("800x600")
root.config(bg="blue")

label = tk.Label(root, text="Bu bir Label'dır", bg="red", fg="white")
label.pack(pady=10)

def degistir():
    label.config(text="Değişti", bg="yellow", fg="black")

def arkaplan():
    renkler=["red", "yellow", "blue"]
    root.config(bg=random.choice(renkler))

def girdi():
    metin=entry.get()
    label.config(text=metin)

def ters_çevir():
    metin=entry.get()
    ters_metin = metin[::-1]
    label.config(text=ters_metin)

def buyuk_yaz():
    metin=entry.get()
    metin=metin.upper()
    label.config(text=metin)

def sakaci_buton():
    button4.pack_forget()
    button4.place_forget()
    x=random.randint(50,750)
    y=random.randint(50,550)
    button4.place(x=x, y=y)


button4 = tk.Button(root, text="Şakacı", command=sakaci_buton)
button4.pack(pady=20)

button3 = tk.Button(root, text="ters çevir", command=buyuk_yaz)
button3.pack(pady=40)

button2 = tk.Button(root, text="Arkaplan Değişir", command=arkaplan)
button2.pack(pady=30)

button = tk.Button(root, text="Tıkla", command=degistir)
button.pack(pady=20)

entry = tk.Entry(root)
entry.pack(pady=10)


root.mainloop()
