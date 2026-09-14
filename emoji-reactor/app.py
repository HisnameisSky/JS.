import tkinter as tk

def update_count(btn):
    current_text = btn.cget("text")
    
    emoji, count_part = current_text.rsplit(" ", 1)
    
    curr_count = int(count_part.split("/")[0])
    
    if curr_count == 10:
        return
    
    curr_count += 1
    
    btn.config(text=f"{emoji} {curr_count}/10")


root = tk.Tk()
root.title("Emoji Counter")

button_labels = ["👍 8/10", "❤️ 10/10", "🔥 0/10"]
buttons = []

for label in button_labels:
    btn = tk.Button(root, text=label, font=("Arial", 14), padding=10)
    btn.config(command=lambda b=btn: update_count(b))
    btn.pack(side="left", padx=10, pady=20)
    buttons.append(btn)

root.mainloop()