import tkinter as tk
import random
import string
from tkinter import messagebox

def ekle():
    metin = entry.get()
    if metin.strip():
        text_alani.insert(tk.END, metin + "\n")
    else:
        messagebox.showwarning("Uyarı", "Boş Metin Ekelnemez")
        
def temizle():
    sonuc = messagebox.askyesno("Temizle", "Tüm Metin Silinsin mi?")
    if sonuc:
        text_alani.delete("1.0", tk.END)

def buyuk_harf_yap():
    metin = entry.get()
    if metin.strip():
        text_alani.insert(tk.END, metin.upper() + "\n")
    else:
        messagebox.showwarning("Uyarı", "Boş Metin Ekelnemez")

def rastgele_ekle():
    metin_listesi = [
        "merhaba",
        "günaydın",
        "tünaydın",
        "iyi akşamlar"
    ]
    metin = random.choice(metin_listesi)
    if metin.strip():
        text_alani.insert(tk.END, metin + "\n")
    else:
        messagebox.showwarning("Uyarı", "Boş Metin Ekelnemez")

def sifre_ekle():
    harfler = random.choices(string.ascii_letters, k= 4)
    rakamlar = random.choices(string.digits, k= 4)
    karakterler = random.choices(string.punctuation, k=4)
    liste = []
    liste.extend(harfler)
    liste.extend(rakamlar)
    liste.extend(karakterler)
    random.shuffle(liste)
    print(liste)
    sifre = "".join(liste)
    print(sifre)
    text_alani.config(state="normal")
    text_alani.delete("1.0", tk.END)
    text_alani.insert(tk.END, sifre)
    text_alani.config(state="disabled")

def kopyala():
    print("kopyala")
    metin = text_alani.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(metin)

    # Pop-up göster
    popup = tk.Toplevel(root)
    popup.title("Bilgi")
    popup.geometry("200x80")
    popup.resizable(False, False)

    mesaj = tk.Label(popup, text="Metin panoya kopyalandı!", padx=10, pady=10)
    mesaj.pack()

    # tamam = tk.Button(popup, text="Tamam", command=popup.destroy)
    # tamam.pack(pady=5)

    root.after(1000, popup.destroy)

def edit():
    if text_alani.cget("state") == "normal":
        text_alani.config(state="disabled")
        edit_buton.config(text="🖋️", fg= "black")
    else:
        text_alani.config(state="normal")
        edit_buton.config(text="🖋️", fg= "green")

def yazinin_boyutunu_bul():
    metin = text_alani.get("1.0", tk.END)
    boyut = len(metin.strip())
    print(f"{metin}")
    messagebox.showinfo("boyut", str(boyut))

root = tk.Tk()
root.title("Text box projesi")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 12), width=40)
entry.pack(pady= 10)

frame = tk.Frame(root)
frame.pack(pady= 30)

rastgele_ekle_button = tk.Button(frame, text="Rastgele Ekle", command= rastgele_ekle)
rastgele_ekle_button.pack(pady = 10, side="left")

ekle_button = tk.Button(frame, text="Ekle", command= ekle)
ekle_button.pack(pady = 10, side="left")

buyuk_harf_ekle_button = tk.Button(frame, text="Büyük Harf", command= buyuk_harf_yap)
buyuk_harf_ekle_button.pack(pady = 10, side="left")

sifre_buton = tk.Button(frame, text= "Şifre Ekle", command=sifre_ekle)
sifre_buton.pack(pady= 10, side= "right")

text_alani = tk.Text(root, font=("Arial", 12), height=10, wrap="word")
text_alani.pack(padx= 10, pady= 10, fill="both", expand=True)

kopyala_buton= tk.Button(root, text="⏹️",fg= "blue" , command=kopyala)
kopyala_buton.place(x=250, y=160)

edit_buton= tk.Button(root, text="🖋️",fg= "green" , command=edit)
edit_buton.place(x=270, y=160)

temizle_button = tk.Button(root, text="Temizle", command= temizle)
temizle_button.pack(pady=10)

buton = tk.Button(frame, text="Boyutu", command=yazinin_boyutunu_bul)
buton.pack(side="right")

root.mainloop()