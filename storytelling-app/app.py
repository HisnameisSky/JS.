import tkinter as tk

root = tk.Tk()
root.title("Story Display")

story_container = tk.Frame(root, highlightthickness=3, highlightbackground="#ccc", padding=10)
story_container.pack(padx=20, pady=20)

result_label = tk.Label(story_container, text="", wraplength=400, justify="left")
result_label.pack()

story_dict = {
    "scary": {
        "story": "In the dark woods, a group of friends stumbled upon an old, abandoned cabin. They enter the cabin and awaken something malevolent that had been dormant for centuries.",
        "borderColor": "#ee4b2b"
    },
    "funny": {
        "story": "During a camping trip, Mark decided to show off his culinary skills by cooking dinner over an open fire. However, his attempt caused him to burn the dinner as well as his eyebrows off.",
        "borderColor": "#f1be32"
    },
    "adventure": {
        "story": "Lost in the heart of the Amazon rain forest, Sarah and Jake stumbled upon an ancient temple. They braved deadly traps and encountered strange wildlife, all while deciphering cryptic clues left behind by a mysterious civilization.",
        "borderColor": "#acd157"
    }
}

def display_story(genre):
    if genre in story_dict:
        result_label.config(text=story_dict[genre]["story"])
        story_container.config(highlightbackground=story_dict[genre]["borderColor"])

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

scary_btn = tk.Button(button_frame, text="Scary", command=lambda: display_story("scary"))
funny_btn = tk.Button(button_frame, text="Funny", command=lambda: display_story("funny"))
adventure_btn = tk.Button(button_frame, text="Adventure", command=lambda: display_story("adventure"))

scary_btn.pack(side="left", padx=5)
funny_btn.pack(side="left", padx=5)
adventure_btn.pack(side="left", padx=5)

root.mainloop()