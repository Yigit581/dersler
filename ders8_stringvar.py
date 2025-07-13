import tkinter as tk
import random
import string
from tkinter import messagebox

root = tk.Tk()
root.title("StringVar, IntVar Projesi")
root.geometry("300x400")

sayi_var = tk.IntVar()
sayi_var.set(1)

entry = tk.Entry(root, textvariable= sayi_var).pack(pady=10)
label = tk.Label(root, textvariable= sayi_var).pack(pady=10)

root.mainloop()