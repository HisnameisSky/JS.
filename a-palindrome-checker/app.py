import re
import tkinter as tk
from tkinter import messagebox


def check_palindrome():
    raw_input = text_input.get()

    if raw_input == "":
        messagebox.showinfo("Alert", "Please input a value")
        return

    clean_input = re.sub(r"[^a-zA-Z0-9]", "", raw_input).lower()

    reversed_input = clean_input[::-1]

    if clean_input == reversed_input:
        result_label.config(text=f"{raw_input} is a palindrome")
    else:
        result_label.config(text=f"{raw_input} is not a palindrome")

root=tk.Tk()
root.title("Palidrom Checker")
root.geometry("400X200")

text_input=tk.Entry(root,width=30)
text_input.pack(pady=5)

result_label=tk.Label(root,text="")
result_label.pack(pady=10)

root.mainloop()