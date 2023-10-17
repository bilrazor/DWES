from cell import Cell
from tkinter import Label
from PIL import Image,ImageTk
from io import BytesIO
import threading
import requests
from tkinter import Tk

class MainWindow:

  
    # Constructor de la clase MainWindow.
     def __init__(self, root, json_data):
        self.json_data = json_data
        self.root = root

        def load_image_from_url(url):
            try:
                response = requests.get(url)
                response.raise_for_status()
                img_data = Image.open(BytesIO(response.content))
                return ImageTk.PhotoImage(img_data)
            except requests.RequestException as e:
                print(f"Error al cargar imagen: {e}")
                return None 

        root.title("MainWindow")
        self.cells = []

        for item in self.json_data:
            image_url = item.get("url")
            title = item.get("name")
            description = item.get("description")

            image_tk = load_image_from_url(image_url)
            if image_tk:
                cell = Cell(root, title, image_tk, description, image_url)
                self.cells.append(cell)

 
     