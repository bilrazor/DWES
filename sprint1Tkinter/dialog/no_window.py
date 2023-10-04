from tkinter import Tk , ttk

class NoWindow:
    def __init__(self,root):

        self.root = root
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label (self.frame, text="NO PORQUE")
        self.label.pack()