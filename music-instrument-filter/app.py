import tkinter as tk
from tkinter import ttk

instruments_arr = [
    {"category": "woodwinds", "instrument": "Flute", "price": 500},
    {"category": "woodwinds", "instrument": "Clarinet", "price": 200},
    {"category": "woodwinds", "instrument": "Oboe", "price": 4000},
    {"category": "brass", "instrument": "Trumpet", "price": 200},
    {"category": "brass", "instrument": "Trombone", "price": 300},
    {"category": "brass", "instrument": "French Horn", "price": 4300},
    {"category": "percussion", "instrument": "Drum Set", "price": 500},
    {"category": "percussion", "instrument": "Xylophone", "price": 3000},
    {"category": "percussion", "instrument": "Cymbals", "price": 200},
    {"category": "percussion", "instrument": "Marimba", "price": 3000}
]

def instrument_cards(instrument_category):
    if instrument_category == "all":
        filtered = instruments_arr
    else:
        filtered = [item for item in instruments_arr if item["category"] == instrument_category]
    
    return filtered

root = tk.Tk()
root.title("Instrument Shop")
root.geometry("400x500")

products_container = tk.Frame(root)

def update_display(event=None):
    selected_category = select_container.get()
    
    for widget in products_container.winfo_children():
        widget.destroy()
    
    cards_data = instrument_cards(selected_category)
    for data in cards_data:
        card = tk.LabelFrame(products_container, text=data["instrument"], padx=10, pady=10)
        card.pack(fill="x", my=5, padx=10)
        price_label = tk.Label(card, text=f"${data['price']}", font=("Arial", 12, "bold"))
        price_label.pack()

select_container = ttk.Combobox(
    root, 
    values=["all", "woodwinds", "brass", "percussion"],
    state="readonly"
)
select_container.set("all")
select_container.bind("<<ComboboxSelected>>", update_display)
select_container.pack(pady=10)

products_container.pack(fill="both", expand=True)

# 初回表示
update_display()

root.mainloop()