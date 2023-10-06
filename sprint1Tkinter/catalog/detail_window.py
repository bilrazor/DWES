from tkinter import Toplevel, Label
from PIL import Image, ImageTk

class DetailWindow:
    def __init__(self, root, image_path, title, description):
        self.root = Toplevel(root)  # Cambiado a Toplevel para no crear una nueva instancia de Tk
        self.root.title("Detalle")
        
        self.title_label = Label(self.root, text=title)
        self.title_label.pack()

        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.root, image=self.photo)
        self.image_label.pack()

        self.description_label = Label(self.root, text=description, wraplength=300)
        self.description_label.pack()
