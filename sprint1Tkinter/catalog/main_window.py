from cell import Cell
from tkinter import Label

class MainWindow:
    # Constructor de la clase MainWindow.
    def __init__(self, root):

    
        root.title("MainWindow")
        
        # Crea una lista de objetos Cell, cada uno representando una celda en la ventana principal.
        # Cada celda tiene un título, una ruta a una imagen y una descripción.
        self.cells = [
            Cell(root, "Robot 1", "catalog\\unedited\\imagen1.png", "Descripción del Robot 1"*5),
            Cell(root, "Robot 2", "catalog\\unedited\\imagen2.png", "Descripción del Robot 2"*5),
            Cell(root, "Robot 3", "catalog\\unedited\\imagen3.png", "Descripción del Robot 3"*5),
            Cell(root, "Robot 4", "catalog\\unedited\\imagen4.jpg", "Descripción del Robot 4"*5),
            Cell(root, "Robot 5", "catalog\\unedited\\imagen5.png", "Descripción del Robot 5"*5)
        ]
 