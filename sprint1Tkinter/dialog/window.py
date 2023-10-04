from tkinter import ttk, Tk
from no_window import NoWindow
from yes_window import YesWindow

class MainWindow:
    def on_button_clickL(self):
        root = Tk()
        YesWindow(root)
        root.mainloop()

    def on_button_clickR(self):
        root = Tk()
        NoWindow(root)
        root.mainloop()

    def __init__(self, root):
        self.root = root
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label(self.frame, text="Realizar acción")
        self.label.pack()

        self.button = ttk.Button(self.frame, text="SI", command=self.on_button_clickL)
        self.button.pack(side="left")
        self.button = ttk.Button(self.frame, text="NO", command=self.on_button_clickR)
        self.button.pack(side="right")
