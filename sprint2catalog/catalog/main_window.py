from cell import Cell
from tkinter import Label
from PIL import Image,ImageTk
from io import BytesIO
import threading
import requests
from tkinter import Tk
import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas , Scrollbar , Frame 
from detail_window import DetailWindow

class MainWindow:
    def __init__(self, root, json_data):
        self.root = root
        self.json_data = json_data
        
        
        self.canvas = Canvas(self.root)
        # Creación de una barra de desplazamiento que estará sincronizada con el canvas
        self.scrollbar = Scrollbar(self.root , orient="vertical",command = self.canvas.yview)
        # Creación de un frame que será colocado dentro del canvas.
        self.scrollable_frame = Frame(self.canvas)
        # Método que se activa cuando el widget cambia 
        # Ajusta el área de desplazamiento del canvas según el tamaño del frame.
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion = self.canvas.bbox("all")
                )
        )
        # Crea una ventana en el canvas que contiene el frame desplazable.
        self.canvas.create_window((0,0) , window=self.scrollable_frame, anchor="nw")
        # Configura el canvas para que utilice la barra de desplazamiento.
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        # Coloca el canvas y la barra de desplazamiento en la ventana principal usando el administrador de geometría grid.
        self.canvas.grid(row=0 , column=0, sticky="nsew")
        self.scrollbar.grid(row=0,column=1,sticky="ns")
        # Configura el redimensionamiento de las filas y columnas.
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        # Configura la interfaz de usuario y el menú.
        self.setup_ui()
        self.setup_menu()
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry("{}x{}+{}+{}".format(120, 120, int(x), int(y)))  # Centra una ventana de 120x120 en la pantalla


    def setup_ui(self):
        # Configura el título de la ventana principal y crea celdas para cada elemento en json_data.
        self.root.title("MainWindow")

        for item in self.json_data:
            image_url = item.get("url")
            title = item.get("name")
            description = item.get("description")

            image_tk = self.load_image_from_url(image_url)
            if image_tk:
                cell = Cell(self.scrollable_frame, title, image_tk, description, image_url)

        
       

    def setup_menu(self):
        # Configura un menú en la ventana principal con una opción para mostrar información sobre el desarrollador.
        def show_about_dialog():
            messagebox.showinfo("Acerca de", "Información acerca del desarrollador.")

        menubar = tk.Menu(self.root)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Acerca de", command=show_about_dialog)
        menubar.add_cascade(label="Ayuda", menu=helpmenu)

        self.root.config(menu=menubar)

    @staticmethod
    def load_image_from_url(url):
        # Método estático para cargar una imagen desde una URL y convertirla en un objeto PhotoImage de Tkinter.
        try:
            response = requests.get(url)
            response.raise_for_status()
            img_data = Image.open(BytesIO(response.content))
            return ImageTk.PhotoImage(img_data)
        except requests.RequestException as e:
            print(f"Error al cargar imagen: {e}")
            return None