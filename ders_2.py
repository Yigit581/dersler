import tkinter as tk
import random
from PIL import Image,ImageTk
import tkinter.font as Tf

root = tk.Tk()
root.title("tkinter resim projesi")

root.geometry("800x600")

image = Image.open("rose.png")
image = image.resize((200,300))
image = ImageTk.PhotoImage(image)
label = tk.Label(root, image = image)
label.pack()
resimler = ["adam.png", "rose.png"]
index = 1
font = Tf.Font(family = "Courier New", size = 12, weight = "bold")

def yer_degistir():
    label.pack_forget()
    label.place_forget()
    x = random.randint(0,800)
    y = random.randint(0,600)
    label.place(x = x,y = y)

def resim_degistir():
    image = Image.open(random.choice(["adam.png", "rose.png"]))
    image = image.resize((200,300))
    image = ImageTk.PhotoImage(image)
    label.config(image = image)
    label.image = image

def siradaki_resim():
    global index
    index += 1
    index = index % len(resimler)
    image = Image.open(resimler[index])
    image = image.resize((200,300))
    image = ImageTk.PhotoImage(image)
    label.config(image = image)
    label.image = image

def önceki_resim():
    global index
    index -= 1
    index = index % len(resimler)
    image = Image.open(resimler[index])
    image = image.resize((200,300))
    image = ImageTk.PhotoImage(image)
    label.config(image = image)
    label.image = image



frame = tk.Frame(root)
frame.pack(pady= 30)

buton_ileri = tk.Button(frame, text="-->",command=siradaki_resim, width= 5, font=font)
buton_ileri.pack(side="right")

buton= tk.Button(frame, text="🎲",command=resim_degistir, width= 3, font=font)
buton.pack(side="right")

buton_geri = tk.Button(frame, text="<--",command=önceki_resim, width= 5, font=font)
buton_geri.pack(side="left")

print()

root.mainloop()