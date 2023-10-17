from tkinter import Tk
from main_window import MainWindow
from loading_window import LoadingWindow

def launch_main_window(json_data):
    root = Tk()
    app = MainWindow(root, json_data)
    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = LoadingWindow(root)
    root.mainloop()
    if app.data_ready.is_set():  # Verifica si los datos están listos
        launch_main_window(app.json_data)