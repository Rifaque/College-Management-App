import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3


def enter_data():
    confirmed = confirm_var.get()

    if confirmed == "Confirmed":
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            usn = id_entry.get()
            username = firstname+' '+lastname[0]
            passkey = usn
            user_type = 'teacher'
            conn = sqlite3.connect('College App.db')

            data_insert_query = '''INSERT INTO users (usn, username, password,user_type) VALUES
            (?, ?, ?, ?)'''
            data = (usn, username, passkey, user_type)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data)
            conn.commit()
            conn.close()
            messagebox.showinfo("Entry", "Entry Successful")




        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not confirmed the details")


window = tkinter.Tk()
window.title("Teacher Registration Form")

frame = tkinter.Frame(window)
frame.pack()

user_info_frame = tkinter.LabelFrame(frame, text="Teacher Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

id_label = tkinter.Label(user_info_frame, text="ID")
id_entry = tkinter.Entry(user_info_frame)
id_label.grid(row=2, column=1)
id_entry.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

confirm_frame = tkinter.LabelFrame(frame, text="Confirmatoion")
confirm_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

confirm_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(confirm_frame, text="I confirm the above details are correct to my knowledge.",
                                  variable=confirm_var, onvalue="Confirmed", offvalue="Not Confirmed")
terms_check.grid(row=0, column=0)

button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
