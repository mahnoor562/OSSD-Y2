import tkinter as tk
from tkinter import ttk
from scrapper import get_cars_data


# Show data in textarea
def set_textarea(data):
    textarea.config(state=tk.NORMAL)
    textarea.delete(1.0, tk.END)

    if not data:
        textarea.insert(tk.END, "No data found!")
    else:
        for car in data:
            textarea.insert(tk.END, f"Name: {car['name']}\nPrice: {car['price']}\n\n")

    textarea.config(state=tk.DISABLED)
    status_label.config(text="Data loaded ✔")


# Search button action
def search():
    status_label.config(text="Loading...")
    root.update()
    data = get_cars_data(dropdown.get())
    set_textarea(data)


# Clear button
def clear_text():
    textarea.config(state=tk.NORMAL)
    textarea.delete(1.0, tk.END)
    textarea.config(state=tk.DISABLED)
    status_label.config(text="Cleared")


# Main window
root = tk.Tk()
root.title("🚗 Car Price Scraper")
root.geometry("700x550")
root.config(bg="#f2f2f2")


# Title
title = tk.Label(root, text="Car Price Scraper", font=("Arial", 18, "bold"), bg="#f2f2f2")
title.pack(pady=10)


# Dropdown
car_manufact = ['toyota', 'honda', 'suzuki']
dropdown = ttk.Combobox(root, values=car_manufact, font=("Arial", 12))
dropdown.current(0)
dropdown.pack(pady=10)


# Buttons
btn_frame = tk.Frame(root, bg="#f2f2f2")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Search 🔍", command=search, bg="green", fg="white", width=12).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Clear 🧹", command=clear_text, bg="red", fg="white", width=12).grid(row=0, column=1, padx=10)


# Text area + scrollbar
text_frame = tk.Frame(root)
text_frame.pack(pady=10)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

textarea = tk.Text(text_frame, height=18, width=75, yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)
textarea.config(state=tk.DISABLED)


# Status label
status_label = tk.Label(root, text="Ready", bg="#f2f2f2", fg="blue")
status_label.pack(pady=10)


root.mainloop()