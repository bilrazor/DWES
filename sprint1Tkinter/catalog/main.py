from tkinter import Tk
from main_window import MainWindow
from detail_window import DetailWindow

if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root)
    root.mainloop()