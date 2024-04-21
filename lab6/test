import tkinter as tk
from tkinter import messagebox, filedialog
from db import Database
from models import User
from protection import BufferProtection, PrivilegesProteccion, CanonizationProtection, XSSProtection


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Аутентификация и безопасность")
        self.geometry("400x300")

        self.db = Database()

        self.db.add_user("panton", "panton", "admin")
        self.db.add_user("bob", "123456", "user")

        self.login_label = tk.Label(self, text="Логин:")
        self.login_entry = tk.Entry(self, validate="key")

        self.password_label = tk.Label(self, text="Пароль:")
        self.password_entry = tk.Entry(self, show="*", validate="key")

        self.login_button = tk.Button(self, text="Войти", command=self.authenticate)

        self.login_label.pack()
        self.login_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()

        self.current_user = None

    def authenticate(self):
        username = self.login_entry.get()
        password = self.password_entry.get()

        if not BufferProtection.validate_input(username):
            messagebox.showerror("Ошибка", "Превышена максимальная длина логина (100 символов).")
            return

        if not BufferProtection.validate_input(password):
            messagebox.showerror("Ошибка", "Превышена максимальная длина пароля (100 символов).")
            return

        authenticated_user = self.authenticate_user(username, password)
        if authenticated_user:
            self.current_user = authenticated_user
            messagebox.showinfo("Успешная аутентификация", f"Добро пожаловать, {authenticated_user.username}!")
            self.show_panel_for_role(authenticated_user.role, username)
        else:
            messagebox.showerror("Ошибка аутентификации", "Неверный логин или пароль")

    def authenticate_user(self, username, password):
        user_data = self.db.get_user(username)
        if user_data and user_data["password"] == password:
            return User(username, password, user_data["role"])
        return None

    def show_panel_for_role(self, role, username):
        if role == "admin":
            admin_panel = tk.Toplevel(self)
            admin_panel.title("Панель администратора")
            admin_panel.geometry("400x300")

            self.create_input_widgets(admin_panel, username)

        elif role == "user":
            user_panel = tk.Toplevel(self)
            user_panel.title("Панель пользователя")
            user_panel.geometry("400x300")

            self.create_input_widgets(user_panel, username)

        else:
            messagebox.showwarning("Неизвестная роль", "Ваша роль неопределена.")

    def create_input_widgets(self, parent, username):
        input_label = tk.Label(parent, text="Введите текст:")
        input_label.pack()

        input_entry = tk.Entry(parent, width=40)
        input_entry.pack()

        file_input_button = tk.Button(parent, text="Выбрать файл",
                                      command=lambda: self.process_file_input(username, input_entry))
        file_input_button.pack()

        process_button = tk.Button(parent, text="Обработать", command=lambda: self.process_input(username, input_entry.get()))
        process_button.pack()

        view_data_button = tk.Button(parent, text="Просмотреть данные", command=lambda: self.show_user_data(username))
        view_data_button.pack()

    def process_input(self, username, text):
        if BufferProtection.validate_input(text):
            not_numbers = []
            for c in text:
                if not c.isdigit():
                    not_numbers.append(c)

            processed_text = ''.join(not_numbers)

            self.db.add_data(username, processed_text)
            messagebox.showinfo("Успешно!", "Данные сохранены в базе данных.")
        else:
            messagebox.showerror("Ошибка", "Превышена максимальная длина ввода (100 символов).")

    def process_file_input(self, username, input_entry):
        file_path = filedialog.askopenfilename()
        if file_path:
            if CanonizationProtection.is_valid_file_path(file_path):
                with open(file_path, 'r') as file:
                    text = file.read()
                    input_entry.delete(0, tk.END)
                    input_entry.insert(0, text)
            else:
                messagebox.showerror("Ошибка", "Недопустимый путь к файлу.")

    @PrivilegesProteccion.require_admin
    def show_user_data(self, username):
        user_data = self.db.get_user(username)
        if user_data:
            data_list = user_data["data"]
            if data_list:
                safe_data_list = [XSSProtection.escape_html(item) for item in data_list]
                data_str = "\n".join(safe_data_list)
                messagebox.showinfo(f"Данные пользователя {username}", f"Ваши данные:\n{data_str}")
            else:
                messagebox.showinfo(f"Данные пользователя {username}", "У вас нет сохраненных данных.")
        else:
            messagebox.showerror("Ошибка", "Пользователь не найден в базе данных.")


if __name__ == "__main__":
    app = Application()
    app.mainloop()

