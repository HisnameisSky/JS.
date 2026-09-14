import tkinter as tk
from PIL import Image, ImageTk  # 画像描画用の定番ライブラリ (Pillow)

root = tk.Tk()
root.title("Lightbox Viewer")

thumbnail_urls = [
    "https://cdn.freecodecamp.org/curriculum/labs/stonehenge-thumbnail.jpg",
    "https://cdn.freecodecamp.org/curriculum/labs/storm-thumbnail.jpg",
    "https://cdn.freecodecamp.org/curriculum/labs/trees-thumbnail.jpg"
]

lightbox = tk.Frame(root, bg="black")
lightbox_image_label = tk.Label(lightbox, bg="black")
lightbox_image_label.pack(expand=True)

close_btn = tk.Button(lightbox, text="×", font=("Arial", 20), fg="white", bg="black", bd=0, command=lambda: hide_lightbox())
close_btn.place(x=10, y=10)


def show_lightbox(thumb_src):
    full_size_src = thumb_src.replace("-thumbnail", "")
    
    print(f"Loading Fullsize Image: {full_size_src}")
    
    lightbox.place(x=0, y=0, relwidth=1, relheight=1)

def hide_lightbox():
    lightbox.place_forget()


gallery_frame = tk.Frame(root)
gallery_frame.pack(padding=20)

for url in thumbnail_urls:
    btn = tk.Button(gallery_frame, text=f"Thumb: {url.split('/')[-1]}", command=lambda u=url: show_lightbox(u))
    btn.pack(side="left", padx=5)

lightbox.bind("<Button-1>", lambda e: hide_lightbox())

root.mainloop()