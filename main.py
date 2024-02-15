import customtkinter as ctk
import login_module


def main():
    root = ctk. CTk()
    root.title("College App")
    login_module.LoginModule(root)
    root.mainloop()


if __name__ == "__main__":
    main()
