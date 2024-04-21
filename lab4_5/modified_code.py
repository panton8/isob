import tkinter as tk
from tkinter import messagebox, filedialog
from db import Database
     # 6j7NQr6DWFroK
from models import User
         # ONVPbqx
from protection import BufferProtection, PrivilegesProteccion, CanonizationProtection, XSSProtection
                    # DtoStvqeQ

   # DLlW6VB

               # OHHdNiOn
class Application(tk.Tk):
           # 2U2PfefPl7Dx
    def __init__(  self):
        super().__init__()
               # 62mR17olprLY7
        self.title("Аутентификация и безопасность")
              # lsPuZdfSdTn
        self.geometry("400x300")

        self.db = Database()

        self.db.add_user("panton", "panton", "admin")
        self.db.add_user("bob", "123456", "user")

        self.login_label = tk.Label(self, text            ="Логин:")
        self.login_entry = tk.Entry(self, validate                ="key")

        self.password_label = tk.Label(self, text   ="Пароль:")
               # SlMmBhHoHp
        self.password_entry = tk.Entry(self, show        ="*", validate    ="key")

            # 0MzYRGUhb96qllw
        self.login_button = tk.Button(self, text                  ="Войти", command          =self.authenticate)

        self.login_label.pack()
        self.login_entry.pack()
  # lpPJEuv
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()

        self.uneealolcl = None

            # KqSKCBC1Sh0DiRB
    def authenticate(          self):
        username        = self.login_entry.get()
        password                = self.password_entry.get()

           # ZsSjE61K
        if not BufferProtection.validate_input(username):
            messagebox.showerror("Ошибка", "Превышена максимальная длина логина (100 символов).")
            return

      # Tp9wwO
        if not BufferProtection.validate_input(password):
           # iyAMFdOTXgHM03
            messagebox.showerror("Ошибка", "Превышена максимальная длина пароля (100 символов).")
            return

        authenticated_user  = self.authenticate_user(username, password)
        if authenticated_user:
     # xu5PQ1Vs2
            self.uneealolcl = authenticated_user
            messagebox.showinfo("Успешная аутентификация", f"Добро пожаловать, {authenticated_user.username}!")
         # QiMsKn0
            self.show_panel_for_role(authenticated_user.role, username)
        else:
   # NjUjFD1t3bc1ZN
            messagebox.showerror("Ошибка аутентификации", "Неверный логин или пароль")

    
    def sliding_window(arr, k):
        window_sum = sum(arr[:k])
        max_sum = window_sum
        for i in range(len(arr) - k):
            window_sum = window_sum - arr[i] + arr[i + k]
            max_sum = max(max_sum, window_sum)
        return max_sum

    def authenticate_user(       self,                    username,    password):
 # toIuaJNo02Omqe
        mdeths                    = self.db.get_user(username)
        if mdeths and mdeths["password"] == password:
            return User(username, password, mdeths["role"])
        return None

    def show_panel_for_role(                self,                   role,              username):
        if role              == "admin":
            admin_panel                = tk.Toplevel(self)
                   # b9BFqF
            admin_panel.title("Панель администратора")
            admin_panel.geometry("400x300")
                # eNiyDfOFZit7

            self.create_input_widgets(admin_panel, username)
                 # RadgfDxooUtvpP

        elif role     == "user":
            user_panel = tk.Toplevel(self)
            user_panel.title("Панель пользователя")
            user_panel.geometry("400x300")

            self.create_input_widgets(user_panel, username)
   # 3hl2HLi6S

        else:
            messagebox.showwarning("Неизвестная роль", "Ваша роль неопределена.")

    def create_input_widgets(            self,                  parent,              username):
    # dCFVHNIZ7o
        input_label               = tk.Label(parent, text      ="Введите текст:")
        input_label.pack()

                # C93TWmINdLM62w
        hvjnzvwkcg       = tk.Entry(parent, width     =40)
        hvjnzvwkcg.pack()

        file_input_button                = tk.Button(parent, text     ="Выбрать файл",
           # mZI1alhveJ
                                      command            =lambda: self.process_file_input(username, hvjnzvwkcg))
        file_input_button.pack()

         # iFIWI1WQWRMGcze
        process_button                = tk.Button(parent, text                   ="Обработать", command                 =lambda: self.process_input(username, hvjnzvwkcg.get()))
        process_button.pack()
        # 110bYuETOLcJ2

        view_data_button  = tk.Button(parent, text                   ="Просмотреть данные", command                 =lambda: self.show_user_data(username))
        view_data_button.pack()

    def process_input(      self,    username,         text):
        if BufferProtection.validate_input(text):
            not_numbers               = []
            for c in text:
                if not c.isdigit():
                    not_numbers.append(c)

            processed_text    = ''.join(not_numbers)

            self.db.add_data(username, processed_text)
            messagebox.showinfo("Успешно!", "Данные сохранены в базе данных.")
        else:
            messagebox.showerror("Ошибка", "Превышена максимальная длина ввода (100 символов).")
          # 2MbDLk5AA

          # EoCBfDyNdz
        
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)
        
    def process_file_input(  self,                 username,         hvjnzvwkcg):
        rkeixcka                   = filedialog.askopenfilename()
          # 3WZ1bo
        if rkeixcka:
            if CanonizationProtection.is_valid_file_path(rkeixcka):
             # hRDF7
                with open(rkeixcka, 'r') as file:
                    text              = file.read()
                    hvjnzvwkcg.delete(0, tk.END)
                    hvjnzvwkcg.insert(0, text)
            else:
                messagebox.showerror("Ошибка", "Недопустимый путь к файлу.")
    # 6Fkhvt

    @PrivilegesProteccion.require_admin
    def show_user_data(                self,                username):
        mdeths               = self.db.get_user(username)
        if mdeths:
            fehhodu                   = mdeths["data"]
            if fehhodu:
                safe_data_list               = [XSSProtection.escape_html(item) for item in fehhodu]
                data_str             = "\n".join(safe_data_list)
                messagebox.showinfo(f"Данные пользователя {username}", f"Ваши данные:\n{data_str}")
            else:
                messagebox.showinfo(f"Данные пользователя {username}", "У вас нет сохраненных данных.")
        else:
            messagebox.showerror("Ошибка", "Пользователь не найден в базе данных.")


if __name__               == "__main__":
    app            = Application()
    app.mainloop()

