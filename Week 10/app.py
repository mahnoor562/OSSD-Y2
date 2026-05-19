import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Application")
root.geometry("300x250")


# -------- FUNCTIONS --------
def clear():
    for widget in root.winfo_children():
        widget.destroy()


def main_menu(user):
    clear()

    tk.Label(root, text=f"Welcome {user}!", font=("Arial", 16)).pack(pady=15)

    tk.Button(root, text="Option 1",
              command=lambda: messagebox.showinfo("Option 1", "Clicked")).pack(pady=5)

    tk.Button(root, text="Option 2",
              command=lambda: messagebox.showinfo("Option 2", "Clicked")).pack(pady=5)

    tk.Button(root, text="Logout",
              command=sign_in_window).pack(pady=10)


def sign_in():
    user = username.get()
    pas = password.get()

    try:
        with open("users.txt", "r") as f:
            for line in f:
                u, p = line.strip().split(",")

                if user == u and pas == p:
                    messagebox.showinfo("Success", "Login Successful")
                    main_menu(user)
                    return

        messagebox.showerror("Error", "Wrong Username or Password")

    except:
        messagebox.showerror("Error", "No Account Found")


def sign_up():
    user = username.get()
    pas = password.get()

    with open("users.txt", "a") as f:
        f.write(f"{user},{pas}\n")

    messagebox.showinfo("Success", "Account Created")
    main_menu(user)


# -------- WINDOWS --------
def sign_in_window():
    clear()

    global username, password

    tk.Label(root, text="Sign In", font=("Arial", 16)).pack(pady=10)

    username = tk.Entry(root)
    username.pack(pady=5)
    username.insert(0, "Username")

    password = tk.Entry(root, show="*")
    password.pack(pady=5)
    password.insert(0, "Password")

    tk.Button(root, text="Sign In", command=sign_in).pack(pady=5)

    tk.Button(root, text="Sign Up Page",
              command=sign_up_window).pack()


def sign_up_window():
    clear()

    global username, password

    tk.Label(root, text="Sign Up", font=("Arial", 16)).pack(pady=10)

    username = tk.Entry(root)
    username.pack(pady=5)
    username.insert(0, "Username")

    password = tk.Entry(root, show="*")
    password.pack(pady=5)
    password.insert(0, "Password")

    tk.Button(root, text="Sign Up", command=sign_up).pack(pady=5)

    tk.Button(root, text="Sign In Page",
              command=sign_in_window).pack()


# -------- START --------
sign_in_window()
root.mainloop()