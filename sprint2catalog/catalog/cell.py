from tkinter import Frame, Label
from PIL import Image, ImageTk
from detail_window import DetailWindow

class Cell:
    
    # Constructor de la clase Cell.
    def __init__(self, root, title,image_tk, description,image_path):
        self.root = root
        self.title = title
        self.image_tk = image_tk 
        self.description = description
        self.image_path = image_path
        #titulo de la celda
        Label(self.root, text=title).pack()

        # Crea un frame para contener los elementos de esta celda.
        self.frame = Frame(self.root)
        self.frame.pack()
        
        # Abre y redimensiona la imagen, luego la muestra en una etiqueta.
        label = Label(self.frame, image=self.image_tk)
        label.image = self.image_tk  # Mantén una referencia a la imagen
        label.pack()
        
   
        # Vincula un clic del botón izquierdo del ratón en la etiqueta al método show_detail.
        label.bind('<Button-1>', self.show_detail)


    # Método para mostrar la ventana de detalles cuando se hace clic en esta celda.
    def show_detail(self, event):
        DetailWindow(self.root, self.image_path, self.title, self.description)

