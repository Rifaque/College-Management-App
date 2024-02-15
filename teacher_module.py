from tkinter import *
import subprocess
from PIL import Image
import customtkinter as ctk


class TeacherModule:
    def __init__(self, usn, username):
        self.root = ctk.CTk()
        self.root.title("Teacher (" + username + ")")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.greeting_label = ctk.CTkLabel(self.root, text="Hello, " + username)
        self.greeting_label.pack(pady=5)

        self.timetable_button = ctk.CTkButton(self.root, text="View Timetable", command=self.view_timetable)
        self.timetable_button.pack(pady=10)

        self.marks_button = ctk.CTkButton(self.root, text="Upload GPA", command=self.upload_gpa)
        self.marks_button.pack(pady=10)

        self.new_button = ctk.CTkButton(self.root, text="Log out", command=self.exit)
        self.new_button.pack(side="left", anchor="sw", padx=10, pady=10)

        self.root.mainloop()

    def view_timetable(self):
        img = Image.open('Timetable.jpg')
        img.show()

    def upload_gpa(self):
        subprocess.run(["python", "upload_gpa.py"])
        self.root.mainloop()

    def exit(self):
        self.root.destroy()
        subprocess.run(["python", "login_module.py"])