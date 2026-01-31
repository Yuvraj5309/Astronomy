import tkinter as tk
from PIL import Image, ImageTk

# Create window
root = tk.Tk()
root.title("Popup Window")
root.geometry("600x400")
root.resizable(True, True)

# Left-justified title
title_label = tk.Label(
    root,
    text="T Tauri Star",
    font=("Helvetica Neue", 18, "bold"),
    anchor="w",
    justify="left"
)
title_label.pack(fill="x", padx=20, pady=(10, 5))

# Thin horizontal line
separator = tk.Frame(root, height=1, bg="grey")
separator.pack(fill="x", padx=20, pady=(0, 10))

# Scrollable content frame
content_frame = tk.Frame(root)
content_frame.pack(fill="both", expand=True, padx=20, pady=(0, 10))

canvas = tk.Canvas(content_frame)
scrollbar = tk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Paragraph text (left)
paragraph_text = (
    "T Tauri stars are young, variable stars that are still in the process of forming. "
)

text_label = tk.Label(
    scrollable_frame,
    text=paragraph_text,
    font=("Helvetica Neue", 13, "normal"),  # thinner font
    justify="left",
    anchor="nw",
    wraplength=300
)
text_label.grid(row=0, column=0, sticky="nw", padx=(0, 10), pady=5)

# Load and resize image
image = Image.open("image.png")
image = image.resize((180, 180))  # image size
photo = ImageTk.PhotoImage(image)

# Grey box slightly bigger than image, with thin border
padding = 10
image_box = tk.Frame(
    scrollable_frame,
    bg="#e6e6e6",
    width=image.width + padding*2,
    height=image.height + 60 + padding*2,  # extra space for top/bottom text
    highlightbackground="grey",  # thin border color
    highlightthickness=1
)
image_box.grid(row=0, column=1, sticky="ne", padx=(10, 0), pady=5)
image_box.pack_propagate(False)  # keep the frame size fixed

# Title above image (inside grey box)
image_title = tk.Label(
    image_box,
    text="Star Formation",
    font=("Helvetica Neue", 12, "bold"),
    bg="#e6e6e6"
)
image_title.pack(pady=(5, 2))

# Image inside grey box
image_label = tk.Label(
    image_box,
    image=photo,
    bg="#e6e6e6"
)
image_label.pack(pady=2)
image_label.image = photo

# Small text below image
image_desc = tk.Label(
    image_box,
    text="Visible spectrum of T Tauri Star",
    font=("Helvetica Neue", 10, "normal"),
    bg="#e6e6e6",
    wraplength=image.width
)
image_desc.pack(pady=(2, 5))

# Run app
root.mainloop()
