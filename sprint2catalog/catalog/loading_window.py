from tkinter import Label,TOP,Canvas,ARC
import threading ,requests
import time
from PIL import Image,ImageTk
from io import BytesIO
import threading
import requests
from tkinter import Tk
from main_window import MainWindow

class LoadingWindow:
    def __init__(self,root):
        self.json_data = None
        self.data_ready = threading.Event()
        self.root = root
        self.root.title("Cargando...")
        self.root.geometry("170x120")
        self.root.resizable(False,False)

        self.label = Label(self.root, text="Cargando datos..." , font= ("Arial",14))
        self.label.pack(side=TOP, pady=10)
        
        label_bg_color = self.label.cget("bg")

        self.canvas = Canvas(self.root,width=60 , height=60 , bg = label_bg_color)
        self.canvas.pack()

        self.progress = 0

        self.draw_progress_circle(self.progress)

        self.update_progress_circle()

        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()
        self.check_data_ready()

        self.root.update_idletasks()
        x = ( self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = ( self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")
        
    def fetch_json_data(self):
        try:
            response = requests.get("https://raw.githubusercontent.com/bilrazor/DWES/main/resources/catalog.json")
            response.raise_for_status()  
            self.json_data = response.json()
            print(self.json_data)  # Imprime los datos para verificar
            self.data_ready.set()
        except requests.RequestException as e:
            print(f"Error al recuperar datos: {e}")
            self.root.after(0, self.root.destroy) 

    def check_data_ready(self):
        if not self.data_ready.is_set():
            self.root.after(100, self.check_data_ready)  # Vuelve a verificar después de un corto período
        else:
            self.root.destroy() 

 

    def draw_progress_circle(self,progress):
        self.canvas.delete("progress")
        angle = int(360 * (progress / 100))

        self.canvas.create_arc(10,10,35,35 ,
                               start=0 ,extent=angle, tags="progress", outline="green" , width=4 , style = ARC)
                    
    def update_progress_circle(self):
        if self.progress < 100:
            self.progress += 10
        else:
            self.progress = 0

        
        self.draw_progress_circle(self.progress)
        self.root.after(100,self.update_progress_circle)
