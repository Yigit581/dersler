import tkinter as tk
import random

def tema_degistir(*args):
    secilen_tema = tema_var.get()
    tema = temalar[secilen_tema]

    root.config(bg=tema["bg"])
    oda_turu_label.config(bg=tema["label_bg"])
    cocuk_label.config(bg=tema["label_bg"])
    ebeveyn_label.config(bg=tema["label_bg"])
    ucret_label.config(bg=tema["label_bg"])

    oda_turu_menu.config(bg=tema["menu_bg"], fg=tema["menu_fg"])
    cocuk_menu.config(bg=tema["menu_bg"], fg=tema["menu_fg"])
    ebeveyn_menu.config(bg=tema["menu_bg"], fg=tema["menu_fg"])
    tema_menu.config(bg=tema["menu_bg"], fg=tema["menu_fg"])
    hesaplama.config(bg=tema["button_bg"], fg=tema["button_fg"])

def hesapla():
    oda_turu = oda_turu_var.get()
    ebeveyn = int(ebeveyn_var.get())
    cocuk = int(cocuk_var.get())

    ucret = 0
    if oda_turu == "Standart Oda":
        ucret = 100
    elif oda_turu == "Lüks Oda":
        ucret = 200
    elif oda_turu == "Aile Odası":
        ucret = 300

    cocuk_indirimi = cocuk * 30
    toplam_ucret = ucret * (ebeveyn + cocuk) - cocuk_indirimi

    ucret_label.config(text= f"Toplam Ücret = {toplam_ucret}")

temalar = {
    "Turuncu-Pembe": {
        "bg": "#EB5B00",
        "label_bg": "#FFB200",
        "menu_bg": "#D91656",
        "menu_fg": "white",
        "button_bg": "#640D5F",
        "button_fg": "white"
    },
    "Mavi-Beyaz": {
        "bg": "#0077B6",
        "label_bg": "#90E0EF",
        "menu_bg": "#00B4D8",
        "menu_fg": "black",
        "button_bg": "#03045E",
        "button_fg": "white"
    },
    "Yeşil-Krem": {
        "bg": "#A4DE02",
        "label_bg": "#E9F5DB",
        "menu_bg": "#76BA1B",
        "menu_fg": "black",
        "button_bg": "#254441",
        "button_fg": "white"
    }
}

root = tk.Tk()
root.title("Otel Rezervasyonu")

root.geometry("500x400")

renk1 = "#EB5B00"
renk2 = "#FFB200"
renk3 = "#D91656"
renk4 = "#640D5F"

root.config(bg = renk1)

tema_var = tk.StringVar(value="Turuncu-Pembe")
tema_buton = tk.Button(root, text="Temayı Uygula", command=tema_degistir)
tema_buton.pack(pady=10, padx= 10)

tema_label = tk.Label(root, text="Tema Seçiniz")
tema_label.pack(pady=10)
tema_menu = tk.OptionMenu(root, tema_var, *temalar.keys())
tema_menu.pack()

oda_turu_label = tk.Label(root, text="Oda Türü Seçiniz", bg = renk2)
oda_turu_label.pack(pady=10)

oda_turu_var = tk.StringVar(value= "Standart Oda")
oda_turu_menu = tk.OptionMenu(root, oda_turu_var, "Standart Oda", "Lüks Oda", "Aile Odası")
oda_turu_menu.config(background = renk3)
oda_turu_menu.pack(pady=5)

cocuk_label = tk.Label(root, text="Çocuk Sayasını Seçin", bg = renk2)
cocuk_label.pack(pady=10)

cocuk_var = tk.StringVar(value= "0")
cocuk_menu = tk.OptionMenu(root, cocuk_var, "0", "1", "2", "3", "4", "5")
cocuk_menu.config(background = renk3)
cocuk_menu.pack(pady=5)

ebeveyn_label = tk.Label(root, text="Ebeveyn Seçin", bg = renk2)
ebeveyn_label.pack(pady=10)

ebeveyn_var = tk.StringVar(value= "1")
ebeveyn_menu = tk.OptionMenu(root, ebeveyn_var, "1", "2", "3", "4", "5")
ebeveyn_menu.config(background = renk3)
ebeveyn_menu.pack(pady=5)

ucret_label = tk.Label(root, text="Toplam Ücret = 0", bg = renk2)
ucret_label.pack(pady=15)

hesaplama = tk.Button(root, text="Tamamla", command=hesapla, bg = renk4, fg = "white")
hesaplama.pack(pady=10) 

tema_degistir()

root.mainloop()



