import tkinter as tk
import random
from tkinter import messagebox

root = tk.Tk()
root.title("list box")

root.geometry("300x400")


ürünler = ["süt","ekmek","zeytin","peynir","çay"]

ürün_verisi = {}

def urun_ekle():
    girdi = entry.get()
    if girdi:
        ürün = girdi
    else:
        ürün = random.choice(ürünler)
    if ürün in ürün_verisi:
        ürün_verisi[ürün] += 1
    else:
        ürün_verisi[ürün] = 1
    listeyi_güncelle()

def listeyi_güncelle():
    listbox.delete(0,tk.END)
    for ürün,adet in ürün_verisi.items():
        listbox.insert(tk.END,f"{ürün} x {adet}")

def ürün_sil():
    #messagebox.showwarning("uyarı", "ürün silinecek, emin misiniz")
    dönüt = messagebox.askokcancel("UYARI", "ürün silinecek, emin misiniz")
    if dönüt:
        ürün = listbox.curselection()
        listbox.delete(ürün)

def listeyi_sil():
    dönüt = messagebox.askokcancel("UYARI", "Liste silinecek, emin misiniz")
    if dönüt:
        listbox.delete(0,tk.END)
    

entry = tk.Entry(root)
entry.pack()

listbox = tk.Listbox(root,width=30, height=15)
listbox.pack(pady=10)

buton = tk.Button(root, text="ürün ekle", command=urun_ekle)
buton.pack(pady=10)

silme_buton = tk.Button(root, text="ürün sil", command=ürün_sil)
silme_buton.pack(pady=10)

silme_buton2 = tk.Button(root, text="listeyi sil", command=listeyi_sil)
silme_buton2.pack(pady=10)

root.mainloop()
