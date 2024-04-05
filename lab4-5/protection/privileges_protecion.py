from functools import wraps
from tkinter import messagebox


class PrivilegesProteccion:

    @staticmethod
    def require_admin(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if self.current_user and self.current_user.role == "admin":
                return func(self, *args, **kwargs)
            else:
                messagebox.showerror("Ошибка", "Доступ запрещен. Требуется роль администратора.")
            return None

        return wrapper
