from tkinter import Tk
from main_window import MainWindow
from loading_window import LoadingWindow

# Código principal que se ejecuta cuando se ejecuta este script.
def start_main_window():
    # Inicia la ventana principal después de que la carga se haya completado
    app = MainWindow(root)
    # Nota: No necesitas llamar a root.mainloop() aquí, ya que ya se está ejecutando

if __name__ == "__main__":
    root = Tk()
    # Crea la ventana de carga y pasa el callback start_main_window
    loading_app = LoadingWindow(root, start_main_window)
    root.mainloop()