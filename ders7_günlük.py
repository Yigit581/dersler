import tkinter as tk
from tkinter import messagebox
from datetime import datetime

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
root.geometry("400x300")

label = tk.Label(root, text= "Bu gün ne hissediyorsun")
label.pack(pady=10)

metin_kutusu = tk.Text(root, height=10, width=40)
metin_kutusu.pack(pady=10)



root.mainloop()