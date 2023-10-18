from tkinter import Frame, Label
from PIL import Image, ImageTk
from detail_window import DetailWindow

class Cell:
    def __init__(self, root, title, image_tk, description, image_path):
        self.root = root
        self.title = title
        self.image_tk = image_tk 
        self.description = description
        self.image_path = image_path

        # Crea un frame para contener los elementos de esta celda.
        self.frame = Frame(root)
        self.frame.grid()  # Cambiado de pack a grid

        # Título de la celda
        title_label = Label(self.frame, text=title)
        title_label.grid(row=0, column=0)  # Usando grid aquí

        # Abre y redimensiona la imagen, luego la muestra en una etiqueta.
        label = Label(self.frame, image=self.image_tk)
        label.image = self.image_tk  # Mantén una referencia a la imagen
        label.grid(row=1, column=0)  # Usando grid aquí

        # Vincula un clic del botón izquierdo del ratón en la etiqueta al método show_detail.
        label.bind('<Button-1>', self.show_detail)

    def show_detail(self, event):
        DetailWindow(self.root, self.image_path, self.title, self.description)
