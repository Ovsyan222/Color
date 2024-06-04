import tkinter as tk
import time

# Функция для изменения цвета фона на зеленый
def change_colorG():
    button1.config(bg="green")  # Устанавливаем цвет фона кнопки 1 на зеленый
    root.after(1500, lambda: root.config(bg="gray")) # Запускаем таймер для изменения цвета фона окна на серый через 1,5 секунды

# Создаем главное окно приложения
root = tk.Tk()
root.title("Смена цвета")  # Устанавливаем заголовок окна
root.geometry("300x200")  # Устанавливаем размеры окна

# Создаем кнопку для смены цвета на зеленый
button1 = tk.Button(root, text="Поменять на зелёный", command=change_colorG)
button1.pack(pady=20)  # Размещаем кнопку на форме

# Запускаем главный цикл обработки событий для отображения окна
root.mainloop()
