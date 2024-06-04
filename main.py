import tkinter as tk
import time

def change_colorG():
    button1.config(bg="green")
    root.after(1500, lambda: root.config(bg="gray"))

def change_colorY():
    button2.config(bg="yellow")
    root.after(1500, lambda: root.config(bg="gray"))

def change_colorR():
    button3.config(bg="red")
    root.after(1500, lambda: root.config(bg="gray"))

root = tk.Tk()
root.title("Смена цвета")
root.geometry("300x200")

button1 = tk.Button(root, text="Поменять на зелёный", command=change_colorG)
button1.pack(pady=20)

button2 = tk.Button(root, text="Поменять на жёлтый", command=change_colorY)
button2.pack(pady=20)

button3 = tk.Button(root, text="Поменять на красный", command=change_colorR)
button3.pack(pady=20)

root.mainloop()