from tkinter import Label,TOP,Canvas,ARC
import threading ,requests
import time
from PIL import Image,ImageTk
from io import BytesIO

class LoadingWindow:
    def __init__(self,root,on_complete):

        self.on_complete = on_complete
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
    def fetch_json_data(self):
        # Simulación de una tarea de carga
        response = requests.get("https://github.com/bilrazor/DWES/blob/main/resources/catalog.json")
        
        if response.status_code== 200:
            json_data = response.json()
            for item in json_data:
                guardado = item
            self.root.quit()
            self.on_complete()        

    def load_image_from_url(self,url):
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content))  
        img = ImageTk.PhotoImage(img_data)