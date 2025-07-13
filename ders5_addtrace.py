import tkinter as tk

def on_change(*args):
    value = entry_var.get()
    result_label.config(text = f"Girilen Metin: {value}")

root = tk.Tk()
root.title("trace_add Projesi")
root.geometry("300x600")

entry_var = tk.StringVar()
entry_var.trace_add("write", on_change)
entry = tk.Entry(root, textvariable= entry_var)
entry.pack(pady=10)

result_label = tk.Label(root, text= "Henüz Bir Şey Girilmedi")
result_label.pack(pady=10)

def psw_check(*args):
    psw = psw_var.get()
    if len(psw) <= 4:
        color = "red"
    elif len(psw) <= 6:
        color = "orange"
    else:
        color = "green"
    psw_label.config(text = f"{psw}", fg = color)

psw_var = tk.StringVar()
psw_var.trace_add("write", psw_check)
psw = tk.Entry(root, textvariable= psw_var)
psw.pack(pady=10)

psw_label = tk.Label(root, text= "Henüz Şifre Girilmedi")
psw_label.pack(pady=10)

def char_check(*args):
    char = char_var.get()
    tip = ""
    if char.isdigit():
        tip = "rakam"
    elif char.isalpha():
        tip = "alfabetik"
    else:
        tip = "özel karakter"
    char_label.config(text = f"{tip}")

char_var = tk.StringVar()
char_var.trace_add("write", char_check)
char = tk.Entry(root, textvariable= char_var)
char.pack(pady=10)

char_label = tk.Label(root, text= "Henüz Karakter Girilmedi")
char_label.pack(pady=10)

gecerli_renkler = ["red", "green", "blue", "yellow", "orange", "pink", "purple", "black", "white", "gray", "cyan", "magenta"]

def color_change(*args):
    color = color_var.get().lower()
    if color in gecerli_renkler:
        root.configure(bg=color)
        color_label.config(text="Arka plan rengi değiştirildi", fg=color)
    else:
        color_label.config(text="Geçersiz renk adı", fg="red")

color_var = tk.StringVar()
color_var.trace_add("write", color_change)
color_entry = tk.Entry(root, textvariable=color_var)
color_entry.pack(pady=10)
color_label = tk.Label(root, text="Henüz renk girilmedi")
color_label.pack(pady=10)

def vehicle_guess(*args):
    val = wheel_var.get()
    if val.isdigit():
        wheels = int(val)
        if wheels == 2:
            guess = "Motosiklet yada Bisiklet"
        elif wheels == 4:
            guess = "Araba yada Otobüs"
        elif wheels == 6:
            guess = "Kamyon"
        elif wheels == 10:
            guess = "Tır"
        else:
            guess = "Bilinmeyen Araç"
        vehicle_label.config(text=f"Araç Tahmini: {guess}")
    else:
        vehicle_label.config(text="Geçerli bir sayı giriniz")

wheel_var = tk.StringVar()
wheel_var.trace_add("write", vehicle_guess)
wheel_entry = tk.Entry(root, textvariable=wheel_var)
wheel_entry.pack(pady=10)
vehicle_label = tk.Label(root, text="Henüz tekerlek sayısı girilmedi")
vehicle_label.pack(pady=10)

def animal_guess(*args):
    val = leg_var.get()
    if val.isdigit():
        legs = int(val)
        if legs == 0:
            animal = "Yılan"
        elif legs == 2:
            animal = "Kuş"
        elif legs == 4:
            animal = "Kedi veya Köpek"
        elif legs == 8:
            animal = "Örümcek"
        else:
            animal = "Bilinmeyen Hayvan"
        animal_label.config(text=f"Hayvan Tahmini: {animal}")
    else:
        animal_label.config(text="Geçerli bir sayı giriniz")

leg_var = tk.StringVar()
leg_var.trace_add("write", animal_guess)
leg_entry = tk.Entry(root, textvariable=leg_var)
leg_entry.pack(pady=10)
animal_label = tk.Label(root, text="Henüz ayak sayısı girilmedi")
animal_label.pack(pady=10)

root.mainloop()


