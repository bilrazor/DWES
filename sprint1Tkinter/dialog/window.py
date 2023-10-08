from tkinter import ttk, Tk
from no_window import NoWindow
from yes_window import YesWindow

class MainWindow:
    
    # Método para manejar el clic en el botón "SI".
    def on_button_clickL(self):
        root = Tk()
        YesWindow(root)
        root.mainloop()
        
    # Método para manejar el clic en el botón "NO".
    def on_button_clickR(self):
        root = Tk()
        NoWindow(root)
        root.mainloop()
        
    # Constructor que toma la ventana raíz como argumento.
    def __init__(self, root):
        self.root = root
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label(self.frame, text="Realizar acción")
        self.label.pack()
        
        # Creación de un botón con el texto "SI" que llama a on_button_clickL cuando se hace clic en él.
        self.button = ttk.Button(self.frame, text="SI", command=self.on_button_clickL)
        self.button.pack(side="left")
        
        # Creación de un botón con el texto "NO" que llama a on_button_clickR cuando se hace clic en él.
        self.button = ttk.Button(self.frame, text="NO", command=self.on_button_clickR)
        self.button.pack(side="right")
