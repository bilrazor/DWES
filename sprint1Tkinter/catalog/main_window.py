from tkinter import Tk, ttk, messagebox
from cell import Cell

class MainWindow:
    def on_button_clicked(self, cell):
        message = " has hecho click en la celda " + cell.title
        messagebox.showinfo("Información", message)

    def __init__(self, root):
        root.title("MainWindow")

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

        self.cells = [
            Cell("Robot 1", "catalog\\unedited\\imagen1.png"),
            Cell("Robot 2", "catalog\\unedited\\imagen2.png"),
            Cell("Robot 3", "catalog\\unedited\\imagen3.png"),
            Cell("Robot 4", "catalog\\unedited\\imagen4.jpg"),
            Cell("Robot 5", "catalog\\unedited\\imagen5.png")
        ]


        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound="center")
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))
