from tkinter import Frame, Label
from PIL import Image, ImageTk
from detail_window import DetailWindow

class Cell:
    
    # Constructor de la clase Cell.
    def __init__(self, root, title, path, description):
        self.root = root
        self.title = title
        self.path = path
        self.description = description
        #titulo de la celda
        Label(self.root, text=title).pack()

        # Crea un frame para contener los elementos de esta celda.
        self.frame = Frame(self.root)
        self.frame.pack()
        
        # Abre y redimensiona la imagen, luego la muestra en una etiqueta.
        image = Image.open(self.path).resize((100, 100), Image.Resampling.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(image)
        label = Label(self.frame, image=self.image_tk)
        label.pack()
        
   
        # Vincula un clic del botón izquierdo del ratón en la etiqueta al método show_detail.
        label.bind('<Button-1>', self.show_detail)


    # Método para mostrar la ventana de detalles cuando se hace clic en esta celda.
    def show_detail(self, event):
        DetailWindow(self.root, self.path, self.title, self.description)

