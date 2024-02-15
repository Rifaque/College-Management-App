import sqlite3
import customtkinter as ctk


def fetch_current_gpa():
    usn = usn_entry.get()

    if not usn:
        status_label.configure(text="Please enter the USN to fetch GPA.")
        return

    conn = sqlite3.connect('College App.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE usn=?", (usn,))
    student = cursor.fetchone()

    if not student:
        status_label.configure(text="Student with the given USN not found.")
    else:
        try:
            status_label.configure(text=f"Current GPA of {student[0]} is: {student[4]}")
        except TypeError :
            status_label.config(text="GPA has not been entered yet.")
    conn.close()

def update_gpa():
    usn = usn_entry.get()
    gpa = gpa_entry.get()

    if not usn or not gpa:
        status_label.configure(text="Please enter both USN and GPA.")
        return

    try:
        gpa = float(gpa)
    except ValueError:
        status_label.configure(text="GPA must be a valid number.")
        return

    conn = sqlite3.connect('College App.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE usn=?", (usn,))
    student = cursor.fetchone()

    if not student:
        status_label.configure(text="Student with the given USN not found.")
        conn.close()
        return

    cursor.execute("UPDATE users SET gpa=? WHERE usn=?", (gpa, usn))
    conn.commit()

    conn.close()
    status_label.configure(text="GPA updated successfully.")

root = ctk.CTk()
root.title("Update GPA")
root.geometry("400x300")
usn_label = ctk.CTkLabel(root, text="USN:")
usn_label.pack(pady=5)
usn_entry = ctk.CTkEntry(root)
usn_entry.pack(pady=5)

fetch_button = ctk.CTkButton(root, text="Fetch GPA", command=fetch_current_gpa)
fetch_button.pack(pady=10)

gpa_label = ctk.CTkLabel(root, text="GPA:")
gpa_label.pack(pady=5)
gpa_entry = ctk.CTkEntry(root)
gpa_entry.pack(pady=5)

update_button = ctk.CTkButton(root, text="Update GPA", command=update_gpa)
update_button.pack(pady=10)

status_label = ctk.CTkLabel(root, text="")
status_label.pack(pady=5)

root.mainloop()