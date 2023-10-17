from cell import Cell
from tkinter import Label
from PIL import Image,ImageTk
from io import BytesIO
import threading
import requests
from tkinter import Tk
import tkinter as tk
from tkinter import messagebox

class MainWindow:
    def __init__(self, root, json_data):
        self.root = root
        self.json_data = json_data

        self.setup_ui()
        self.setup_menu()

    def setup_ui(self):
        self.root.title("MainWindow")

        for item in self.json_data:
            image_url = item.get("url")
            title = item.get("name")
            description = item.get("description")

            image_tk = self.load_image_from_url(image_url)
            if image_tk:
                cell = Cell(self.root, title, image_tk, description, image_url)

        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry("+{}+{}".format(int(x), int(y)))

    def setup_menu(self):
        def show_about_dialog():
            messagebox.showinfo("Acerca de", "Información acerca del desarrollador.")

        menubar = tk.Menu(self.root)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Acerca de", command=show_about_dialog)
        menubar.add_cascade(label="Ayuda", menu=helpmenu)

        self.root.config(menu=menubar)

    @staticmethod
    def load_image_from_url(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            img_data = Image.open(BytesIO(response.content))
            return ImageTk.PhotoImage(img_data)
        except requests.RequestException as e:
            print(f"Error al cargar imagen: {e}")
            return None