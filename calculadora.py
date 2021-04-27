import tkinter as tk
from tkinter import ttk
from main_frame import MainFrame

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()

        self.winfo_toplevel().title("Calculadora")
        self.resizable(0,0)
        self.mainFrame = MainFrame(self)
        self.mainFrame.grid(row=0, column=0, padx=10, pady=10, sticky='NSEW')

app = Calculadora()
app.mainloop()