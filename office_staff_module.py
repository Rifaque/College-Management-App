import subprocess
import customtkinter as ctk


class OfficeStaffModule:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Office Staff")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.greeting_label = ctk.CTkLabel(self.root, text="Hello, Office User")
        self.greeting_label.pack(pady=5)

        self.register_student_button = ctk.CTkButton(self.root, text="Register New Student",
                                                     command=self.register_student)
        self.register_student_button.pack(pady=10)

        self.register_teacher_button = ctk.CTkButton(self.root, text="Register New Teacher",
                                                     command=self.register_teacher)
        self.register_teacher_button.pack(pady=10)

        self.update_fees_button = ctk.CTkButton(self.root, text="Update Student Fees", command=self.update_fees)
        self.update_fees_button.pack(pady=10)

        self.new_button = ctk.CTkButton(self.root, text="Log out", command=self.exit)
        self.new_button.pack(side="left", anchor="sw", padx=10, pady=10)

        self.root.mainloop()

    def register_student(self):
        subprocess.run(["python", "newstudent.py"])

    def register_teacher(self):
        subprocess.run(["python", "newteacher.py"])

    def update_fees(self):
        subprocess.run(["python", "upload_fees.py"])

    def exit(self):
        self.root.destroy()
        subprocess.run(["python", "login_module.py"])
