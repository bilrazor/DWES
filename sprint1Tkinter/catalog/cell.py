from tkinter import Frame, Label
from PIL import Image, ImageTk

class Cell:
    def __init__(self, root, title, path, description):
        self.root = root
        self.title = title
        self.path = path
        self.description = description
        
        self.frame = Frame(self.root)
        self.frame.pack()
        
        original_image = Image.open(self.path)
        resized_image = original_image.resize((100, 100), Image.Resampling.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(resized_image)

        self.label = Label(self.frame, image=self.image_tk)
        self.label.pack()
        self.label.bind('<Button-1>', self.show_detail)  # Vincula el clic del botón izquierdo del ratón al método show_detail

    def show_detail(self, event):
        from detail_window import DetailWindow  # Importación local para evitar importaciones circulares
        DetailWindow(self.root, self.path, self.title, self.description)
