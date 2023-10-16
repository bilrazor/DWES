from tkinter import Toplevel, Label, messagebox
from PIL import Image, ImageTk

class DetailWindow:
    # Constructor de la clase DetailWindow.
    def __init__(self, root, image_path, title, description):
        
        # Crea una nueva ventana (Toplevel) para mostrar los detalles.
        self.root = Toplevel(root)  
        self.root.title("Detalle")
        
        # Crea y muestra una etiqueta con el título.
        Label(self.root, text=title).pack()
        
        # Abre la imagen desde la ruta proporcionada y la muestra en una etiqueta.
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        image_label = Label(self.root, image=photo)
        image_label.photo = photo  # Mantiene una referencia a la imagen para evitar que se recoja como basura.
        image_label.pack()
        
        # Verifica la longitud de la descripción y muestra un mensaje de error si es necesario.
        # También ajusta la descripción a la longitud requerida si es necesario.
        if len(description) < 100:
            messagebox.showerror("Error", "La descripción es demasiado corta. Debe tener al menos 100 caracteres.")
            description = description.ljust(100) 
        elif len(description) > 200:
            messagebox.showerror("Error", "La descripción es demasiado larga. Debe tener como máximo 200 caracteres.")
            description = description[:200]  

        # Crea y muestra una etiqueta con la descripción.
        Label(self.root, text=description, wraplength=200).pack()