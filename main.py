import tkinter as tk
from PIL import Image, ImageTk

# Create window
root = tk.Tk()
root.title("Popup Window")
root.geometry("400x400")
root.resizable(False, False)

# Text label
label = tk.Label(
    root,
    text="Hello! This is a popup window.",
    font=("Arial", 14)
)
label.pack(pady=10)

# Load image
image = Image.open("image.png")
image = image.resize((250, 250))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.pack()

# Run app
root.mainloop()
