import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkinter import colorchooser
from PIL import Image,ImageTk


def renk_sec():
    secilen_renk = colorchooser.askcolor(title= "Renk Seçiniz")
    if secilen_renk [1]:
        metin_kutusu.config(bg= secilen_renk[1])

def metin_renk_sec():
    secilen_renk = colorchooser.askcolor(title= "Renk Seçiniz")
    if secilen_renk [1]:
        metin_kutusu.config(fg= secilen_renk[1])

def kaydet():
    metin = metin_kutusu.get("1.0", "end-1c")
    if not metin.strip():
        messagebox.showwarning("Uyarı", "Günlük boş olamaz")
        return
    zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    kayit = f"{zaman}\n{metin}\n{'-'*40}\n"

    with open("Günlük.txt", "a", encoding= "utf-8") as dosya:
        dosya.write(kayit)
    messagebox.showinfo("kayit başarılı", "kaydiniz başarlıyla kayıt edildi")
    metin_kutusu.delete("1.0", "end")

#arayüz

root = tk.Tk()
root.title("Günlük projesi")
root.geometry("400x400")

label = tk.Label(root, text= "Bu gün ne hissediyorsun", )
label.pack(pady=10)

metin_kutusu = tk.Text(root, height=10, width=40)
metin_kutusu.pack(pady=10)

button = tk.Button(root, text= "Kaydet", command= kaydet)
button.pack(pady=10)

image = Image.open(f"assets\color-pallete.png")
image = image.resize((30,30))
image = ImageTk.PhotoImage(image)

renk_button = tk.Button(root, text= "Renk Seç", command= renk_sec, image=image)
renk_button.pack(pady=10, padx=10, side="left")

text_image = Image.open(r"assets\font.png")
text_image = text_image.resize((30,30))
text_image = ImageTk.PhotoImage(text_image)

metin_renk_button = tk.Button(root, command= metin_renk_sec, image=text_image)
metin_renk_button.pack(pady=10, padx=10, side="left")

root.mainloop()