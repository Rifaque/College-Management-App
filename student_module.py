from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
from PIL import Image
import customtkinter as ctk
import subprocess


class StudentModule:
    def __init__(self, usnin, username):
        global usn
        usn = usnin
        self.root = ctk.CTk()
        self.root.title("Student (" + username + ")")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        con = sql.connect("College App.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cur.fetchone()
        sem = str(row[6])
        branch = str(row[7])

        self.greeting_label = ctk.CTkLabel(self.root, text="")
        self.greeting_label.pack(pady=0)

        self.greeting_label = ctk.CTkLabel(self.root,
                                           text="Hello, " + username + "\nStudent of Sem " + sem + " " + branch)
        self.greeting_label.pack(pady=5)

        # self.greeting_label = ctk.CTkLabel(self.root, text="Student of Sem " + sem + " " + branch)
        # self.greeting_label.pack(pady=5)

        self.timetable_button = ctk.CTkButton(self.root, text="View Timetable", command=self.view_timetable)
        self.timetable_button.pack(pady=10)

        self.fees_button = ctk.CTkButton(self.root, text="See Fees", command=self.see_fees)
        self.fees_button.pack(pady=10)

        self.gpa_button = ctk.CTkButton(self.root, text="See GPA", command=self.calculate_gpa)
        self.gpa_button.pack(pady=10)

        self.new_button = ctk.CTkButton(self.root, text="Log out", command=self.exit)
        self.new_button.pack(side="left", anchor="sw", padx=10, pady=10)

        self.root.mainloop()

    def view_timetable(self):

        img = Image.open('Timetable.jpg')
        img.show()

    def see_fees(self):
        con = sql.connect("College App.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE usn = ?", (usn,))
        row = cur.fetchone()
        fees = row[5]
        try:
            messagebox.showinfo("Fees", "You have a pending fee of Rs." + str(fees) + ".")
        except TypeError:
            messagebox.showinfo("Fees", f"Your Fees hasn't been updated yet, Please contact the Administration")

    def calculate_gpa(self):
        con = sql.connect("College App.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE usn = ?", (usn,))
        row = cur.fetchone()
        gpa = row[4]
        try:
            messagebox.showinfo("GPA", f"Your GPA is " + gpa)
        except TypeError:
            messagebox.showinfo("GPA", f"Your GPA hasn't been updated yet, Please contact your teacher")

    def exit(self):
        self.root.destroy()
        subprocess.run(["python", "login_module.py"])
