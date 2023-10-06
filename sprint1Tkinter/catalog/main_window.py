from tkinter import Tk, ttk, messagebox
from cell import Cell
from detail_window import DetailWindow

class MainWindow:
    def on_button_clicked(self, cell):
        detail_window_root = Tk()
        DetailWindow(detail_window_root, cell.path, cell.title, cell.description)
        detail_window_root.mainloop()

    def __init__(self, root):

        """self.cells = [
            Cell("Robot 1", "C:\\Users\\Alumno\\Documents\\GitHub\\DWES\\sprint1Tkinter\\catalog\\edited\\imagen1Edited.png"),
            Cell("Robot 2", "C:\\Users\\Alumno\\Documents\\GitHub\\DWES\\sprint1Tkinter\\catalog\\edited\\imagen2Edited.jpg"),
            Cell("Robot 3", "C:\\Users\\Alumno\\Documents\\ GitHub\\DWES\\sprint1Tkinter\\catalog\\edited\\imagen3Edited.png"),
            Cell("Robot 4", "C:\\Users\\Alumno\\Documents\\GitHub\\DWES\\sprint1Tkinter\\catalog\\edited\\imagen4Edited.png"),
            Cell("Robot 5", "C:\\Users\\Alumno\\Documents\\GitHub\\DWES\\sprint1Tkinter\\catalog\\edited\\imagen5Edited.png")
        ]"""
        """self.cells = [
            Cell("Robot 1", "catalog\\edited\\imagen1Edited.png"),
            Cell("Robot 2", "catalog\\edited\\imagen2Edited.jpg"),
            Cell("Robot 3", "catalog\\edited\\imagen3Edited.png"),
            Cell("Robot 4", "catalog\\edited\\imagen4Edited.png"),
            Cell("Robot 5", "catalog\\edited\\imagen5Edited.png")
        ]""" 

        root.title("MainWindow")

        self.cells = [
            Cell(root, "Robot 1", "catalog\\unedited\\imagen1.png", "Descripción del Robot 1"),
            Cell(root, "Robot 2", "catalog\\unedited\\imagen2.png", "Descripción del Robot 2"),
            Cell(root, "Robot 3", "catalog\\unedited\\imagen3.png", "Descripción del Robot 3"),
            Cell(root, "Robot 4", "catalog\\unedited\\imagen4.jpg", "Descripción del Robot 4"),
            Cell(root, "Robot 5", "catalog\\unedited\\imagen5.png", "Descripción del Robot 5")
        ]