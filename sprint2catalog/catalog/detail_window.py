from tkinter import Toplevel, Label, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

class DetailWindow:
    def __init__(self, root, image_url, title, description):
        if not (100 <= len(description) <= 200):
            messagebox.showerror("Error", "La descripción debe tener entre 100 y 200 caracteres.")
            return  # Retorna desde el método __init__, por lo que no se creará la ventana.

        self.root = Toplevel(root)  
        self.root.title("Detalle")

        Label(self.root, text=title).pack()

        # Descarga la imagen desde la URL
        try:
            response = requests.get(image_url)
            response.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa
            image_bytes = BytesIO(response.content)  # BytesIO crea un objeto tipo archivo en memoria
            image = Image.open(image_bytes)
            photo = ImageTk.PhotoImage(image)
            image_label = Label(self.root, image=photo)
            image_label.image = photo 
            image_label.pack()
        except requests.RequestException as e:
            print(f"Error al recuperar la imagen: {e}")
            messagebox.showerror("Error", f"Error al cargar la imagen: {e}")
         

        # Crea y muestra una etiqueta con la descripción.
        Label(self.root, text=description, wraplength=200).pack()
        self.root.update_idletasks()
        x = ( self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = ( self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")
  
        