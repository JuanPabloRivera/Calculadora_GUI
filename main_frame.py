import tkinter as tk
from tkinter import ttk

class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=600, height=1000, padx=10, pady=10, background='#333333')

        self.ans = 0

        self.numberDisplay = ttk.Label(self, text='0', font=('Helvetica', 30), wraplength=15, anchor=tk.E)
        self.numberDisplay.grid(row=0, column=0, sticky='EW', padx=10, pady=10, columnspan=5)

        # Backspace and clear buttons
        buttonCE = tk.Button(self, text='CE', font=('Helvetica', 16), bg='#6f90a8', anchor=tk.CENTER)
        buttonCE.grid(row=1, column=0, padx=10, pady=10, sticky='EW')
        buttonC = tk.Button(self, text='C', font=('Helvetica', 16), bg='#6f90a8', anchor=tk.CENTER)
        buttonC.grid(row=1, column=1, padx=10, pady=10, sticky='EW')
        backspace = tk.Button(self, text='←', font=('Helvetica', 16), bg='#6f90a8', anchor=tk.CENTER)
        backspace.grid(row=1, column=2, padx=10, pady=10, sticky='EW', columnspan=3)

        # Number buttons
        number1 = tk.Button(self, text='1', font=('Helvetica', 16), bg='#969fa6', anchor=tk.CENTER)
        number1.grid(row=2, column=0, padx=10, pady=10, sticky='EW')
        number2 = tk.Button(self, text='2', font=('Helvetica', 16), bg='#969fa6', anchor=tk.CENTER)
        number2.grid(row=2, column=1, padx=10, pady=10, sticky='EW')
        number3 = tk.Button(self, text='3', font=('Helvetica', 16), bg='#969fa6', anchor=tk.CENTER)
        number3.grid(row=2, column=2, padx=10, pady=10, sticky='EW')
        number4 = tk.Button(self, text='4', font=('Helvetica', 16), bg='#969fa6', anchor=tk.CENTER)
        number4.grid(row=3, column=0, padx=10, pady=10, sticky='EW')
        number5 = tk.Button(self, text='5', font=('Helvetica', 16), bg='#969fa6', anchor=tk.CENTER)
        number5.grid(row=3, column=1, padx=10, pady=10, sticky='EW')
        number6 = tk.Button(self, text='6', font=('Helvetica', 16), bg='#969fa6', anchor=tk.CENTER)
        number6.grid(row=3, column=2, padx=10, pady=10, sticky='EW')
        number7 = tk.Button(self, text='7', font=('Helvetica', 16), bg='#969fa6', anchor=tk.CENTER)
        number7.grid(row=4, column=0, padx=10, pady=10, sticky='EW')
        number8 = tk.Button(self, text='8', font=('Helvetica', 16), bg='#969fa6', anchor=tk.CENTER)
        number8.grid(row=4, column=1, padx=10, pady=10, sticky='EW')
        number9 = tk.Button(self, text='9', font=('Helvetica', 16), bg='#969fa6', anchor=tk.CENTER)
        number9.grid(row=4, column=2, padx=10, pady=10, sticky='EW')
        number0 = tk.Button(self, text='0', font=('Helvetica', 16), bg='#969fa6', anchor=tk.CENTER)
        number0.grid(row=5, column=1, padx=10, pady=10, sticky='EW')
        number00 = tk.Button(self, text='00', font=('Helvetica', 16), bg='#969fa6', anchor=tk.CENTER)
        number00.grid(row=5, column=0, padx=10, pady=10, sticky='EW')
        decimalPoint = tk.Button(self, text='.', font=('Helvetica', 16), bg='#969fa6', anchor=tk.CENTER)
        decimalPoint.grid(row=5, column=2, padx=10, pady=10, sticky='EW')

        # Operators buttons
        add = tk.Button(self, text='+', font=('Helvetica', 16), bg='#2c5778', anchor=tk.CENTER)
        add.grid(row=2, column=3, padx=10, pady=10, sticky='EW')
        substract = tk.Button(self, text='-', font=('Helvetica', 16), bg='#2c5778', anchor=tk.CENTER)
        substract.grid(row=2, column=4, padx=10, pady=10, sticky='EW')
        multiply = tk.Button(self, text='x', font=('Helvetica', 16), bg='#2c5778', anchor=tk.CENTER)
        multiply.grid(row=3, column=3, padx=10, pady=10, sticky='EW')
        divide = tk.Button(self, text='÷', font=('Helvetica', 16), bg='#2c5778', anchor=tk.CENTER)
        divide.grid(row=3, column=4, padx=10, pady=10, sticky='EW')
        modulus = tk.Button(self, text='%', font=('Helvetica', 16), bg='#2c5778', anchor=tk.CENTER)
        modulus.grid(row=4, column=3, padx=10, pady=10, sticky='EW')
        power = tk.Button(self, text='x\u207F', font=('Helvetica', 16), bg='#2c5778', anchor=tk.CENTER)
        power.grid(row=4, column=4, padx=10, pady=10, sticky='EW')
        sqrt = tk.Button(self, text='\u221Ax', font=('Helvetica', 16), bg='#2c5778', anchor=tk.CENTER)
        sqrt.grid(row=5, column=4, padx=10, pady=10, sticky='EW')
        equal = tk.Button(self, text='=', font=('Helvetica', 16), bg='#018cab', anchor=tk.CENTER)
        equal.grid(row=5, column=3, padx=10, pady=10, sticky='EW')

        # Column and row spaces
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)