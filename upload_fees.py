import sqlite3
import customtkinter as ctk


def update_fees():
    usn = usn_entry.get()
    fees = fees_entry.get()

    if not usn or not fees:
        status_label.configure(text="Please enter both USN and Fees.")
        return

    try:
        fees = float(fees)
    except ValueError:
        status_label.configure(text="Fees must be a valid number.")
        return

    conn = sqlite3.connect('College App.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE usn=?", (usn,))
    student = cursor.fetchone()

    if not student:
        status_label.configure(text="Student with the given USN not found.")
        conn.close()
        return

    cursor.execute("UPDATE users SET fees=? WHERE usn=?", (fees, usn))
    conn.commit()

    conn.close()
    status_label.configure(text="Fees updated successfully.")


root = ctk.CTk()
root.title("Update Fees")
root.geometry("400x300")
usn_label = ctk.CTkLabel(root, text="USN:")
usn_label.pack(pady=5)
usn_entry = ctk.CTkEntry(root)
usn_entry.pack(pady=5)

fees_label = ctk.CTkLabel(root, text="Fees:")
fees_label.pack(pady=5)
fees_entry = ctk.CTkEntry(root)
fees_entry.pack(pady=5)

update_button = ctk.CTkButton(root, text="Update Fees", command=update_fees)
update_button.pack(pady=10)

status_label = ctk.CTkLabel(root, text="")
status_label.pack(pady=5)

root.mainloop()
