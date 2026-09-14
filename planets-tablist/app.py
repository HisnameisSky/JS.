import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.title("Tab Navigation")
root.geometry("400x250")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

panel1 = ttk.Frame(notebook)
panel2 = ttk.Frame(notebook)
panel3 = ttk.Frame(notebook)

ttk.Label(panel1, text="This is the content of Panel 1").pack(
    padx=20, pady=20
)
ttk.Label(panel2, text="This is the content of Panel 2").pack(
    padx=20, pady=20
)
ttk.Label(panel3, text="This is the content of Panel 3").pack(
    padx=20, pady=20
)

notebook.add(panel1, text="Tab 1")
notebook.add(panel2, text="Tab 2")
notebook.add(panel3, text="Tab 3")

def on_tab_change(event):
    selected_index = notebook.index(notebook.select())
    selected_panel = notebook.tabs()[selected_index]
    print(f"Selected Tab Index: {selected_index}")

notebook.bind("<<NotebookTabChanged>>", on_tab_change)
root.mainloop()