import os
import tkinter as tk
from tkinter import messagebox


def compile_project():
    os.system("pyinstaller --onefile main.py")


def check_license():
    license_key = entry_license.get()
    if license_key == "p1A2n3t4O5n6":
        compile_project()
        messagebox.showinfo("Успех", "Проект успешно скомпилирован в exe файл.")
        window.quit()
    else:
        messagebox.showerror("Ошибка", "Неверный лицензионный ключ.")


window = tk.Tk()
window.title("Инсталлятор")

label_license = tk.Label(window, text="Введите лицензионный ключ:")
label_license.pack()

entry_license = tk.Entry(window)
entry_license.pack()

btn_compile = tk.Button(window, text="Скомпилировать", command=check_license)
btn_compile.pack()

window.mainloop()
#