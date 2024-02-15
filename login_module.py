import sqlite3 as sql
import student_module
import teacher_module
import office_staff_module
import customtkinter as ctk
from tkinter import messagebox


class LoginModule:
    def __init__(self, master):
        self.master = master
        self.master.geometry("250x250")
        self.frame = ctk.CTkFrame(self.master)
        self.frame.pack(padx=20, pady=20)

        self.label_username = ctk.CTkLabel(self.frame, text="Username:")
        # username will be [firstname(space)lastname]
        self.label_username.pack(pady=5)
        self.entry_username = ctk.CTkEntry(self.frame)
        self.entry_username.pack(pady=5)

        self.label_password = ctk.CTkLabel(self.frame, text="Password:")
        # password will be the usn/ID of the user
        self.label_password.pack(pady=5)
        self.entry_password = ctk.CTkEntry(self.frame, show="*")
        self.entry_password.pack(pady=5)

        self.button_login = ctk.CTkButton(self.frame, text="Login", command=self.login)
        self.button_login.pack(pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        con = sql.connect("College App.db")
        cur = con.cursor()
        statement = f"SELECT username from users WHERE username='{username}' AND Password = '{password}';"
        cur.execute(statement)
        if not cur.fetchone():
            messagebox.showerror("Login", "Invalid username or password")
            exit()
        else:
            messagebox.showinfo("Login", "Login Successful")
        cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cur.fetchone()
        usn = row[0]
        usertype = row[3]
        if usertype == "student":
            self.master.destroy()
            student_module.StudentModule(usn, username)
        elif usertype == "teacher":
            self.master.destroy()
            teacher_module.TeacherModule(usn, username)
        elif usertype == "office":
            self.master.destroy()
            office_staff_module.OfficeStaffModule()


if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Login App")
    login_app = LoginModule(root)
    root.mainloop()
