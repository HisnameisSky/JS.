import tkinter as tk

root = tk.Tk()
root.title("Real Time Counter")

text_var = tk.StringVar()

text_input = tk.Entry(root, textvariable=text_var, width=40, font=("Arial", 14))
text_input.pack(padx=20, pady=10)

char_count = tk.Label(root, text="Character Count: 0/50", font=("Arial", 12))
char_count.pack(pady=10)


def on_input(*args):
    current_text = text_var.get()
    
    if len(current_text) > 50:
        current_text = current_text[:50]  # Pythonのスライス (JSの .slice(0, 50) と同じ)
        text_var.set(current_text)        # 入力欄の文字を50文字に強制上書き
        
    length = len(current_text)
    
    char_count.config(text=f"Character Count: {length}/50")
    
    if length == 50:
        char_count.config(fg="red")     # JSの .classList.add("red") に対応
    else:
        char_count.config(fg="black")   # JSの .classList.remove("red") に対応


text_var.trace_add("write", on_input)

root.mainloop()