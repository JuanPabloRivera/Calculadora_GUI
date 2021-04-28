import tkinter as tk
from tkinter import font

class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=600, height=1000, padx=10, pady=10, background='#333333')

        self.ans = '0'
        self.currentNumber = ''
        self.op = ''
        self.hasAns = False

        self.numberDisplay = tk.Label(self, text='', font=('Courier', 30), width=13, height=1, anchor=tk.E)
        self.numberDisplay.grid(row=0, column=0, sticky='EW', padx=10, pady=10, columnspan=5)

        # Backspace and clear buttons
        buttonCE = tk.Button(self, text='CE', font=('Helvetica', 16), bg='#ecac4c', anchor=tk.CENTER, command=self.pressCE)
        buttonCE.grid(row=1, column=0, padx=10, pady=10, sticky='EW')
        buttonC = tk.Button(self, text='C', font=('Helvetica', 16), bg='#ecac4c', anchor=tk.CENTER, command=self.pressC)
        buttonC.grid(row=1, column=1, padx=10, pady=10, sticky='EW')
        backspace = tk.Button(self, text='←', font=('Helvetica', 16), bg='#ecac4c', anchor=tk.CENTER, command=self.pressBackSpace)
        backspace.grid(row=1, column=2, padx=10, pady=10, sticky='EW', columnspan=3)

        # Number buttons
        number1 = tk.Button(self, text='1', font=('Helvetica', 16), width=3, bg='#969fa6', anchor=tk.CENTER, command=self.press1)
        number1.grid(row=2, column=0, padx=10, pady=10, sticky='EW')
        number2 = tk.Button(self, text='2', font=('Helvetica', 16), width=3, bg='#969fa6', anchor=tk.CENTER, command=self.press2)
        number2.grid(row=2, column=1, padx=10, pady=10, sticky='EW')
        number3 = tk.Button(self, text='3', font=('Helvetica', 16), width=3, bg='#969fa6', anchor=tk.CENTER, command=self.press3)
        number3.grid(row=2, column=2, padx=10, pady=10, sticky='EW')
        number4 = tk.Button(self, text='4', font=('Helvetica', 16), width=3, bg='#969fa6', anchor=tk.CENTER, command=self.press4)
        number4.grid(row=3, column=0, padx=10, pady=10, sticky='EW')
        number5 = tk.Button(self, text='5', font=('Helvetica', 16), width=3, bg='#969fa6', anchor=tk.CENTER, command=self.press5)
        number5.grid(row=3, column=1, padx=10, pady=10, sticky='EW')
        number6 = tk.Button(self, text='6', font=('Helvetica', 16), width=3, bg='#969fa6', anchor=tk.CENTER, command=self.press6)
        number6.grid(row=3, column=2, padx=10, pady=10, sticky='EW')
        number7 = tk.Button(self, text='7', font=('Helvetica', 16), width=3, bg='#969fa6', anchor=tk.CENTER, command=self.press7)
        number7.grid(row=4, column=0, padx=10, pady=10, sticky='EW')
        number8 = tk.Button(self, text='8', font=('Helvetica', 16), width=3, bg='#969fa6', anchor=tk.CENTER, command=self.press8)
        number8.grid(row=4, column=1, padx=10, pady=10, sticky='EW')
        number9 = tk.Button(self, text='9', font=('Helvetica', 16), width=3, bg='#969fa6', anchor=tk.CENTER, command=self.press9)
        number9.grid(row=4, column=2, padx=10, pady=10, sticky='EW')
        number0 = tk.Button(self, text='0', font=('Helvetica', 16), width=3, bg='#969fa6', anchor=tk.CENTER, command=self.press0)
        number0.grid(row=5, column=1, padx=10, pady=10, sticky='EW')
        number00 = tk.Button(self, text='00', font=('Helvetica', 16), width=3, bg='#969fa6', anchor=tk.CENTER, command=self.press00)
        number00.grid(row=5, column=0, padx=10, pady=10, sticky='EW')
        decimalPoint = tk.Button(self, text='.', font=('Helvetica', 16), width=3, bg='#969fa6', anchor=tk.CENTER, command=self.pressDPoint)
        decimalPoint.grid(row=5, column=2, padx=10, pady=10, sticky='EW')

        # Operators buttons
        add = tk.Button(self, text='+', font=('Helvetica', 16), width=3, bg='#c1412e', anchor=tk.CENTER, command=self.pressAdd)
        add.grid(row=2, column=3, padx=10, pady=10, sticky='EW')
        substract = tk.Button(self, text='-', font=('Helvetica', 16), width=3, bg='#c1412e', anchor=tk.CENTER, command=self.pressSubstract)
        substract.grid(row=2, column=4, padx=10, pady=10, sticky='EW')
        multiply = tk.Button(self, text='x', font=('Helvetica', 16), width=3, bg='#c1412e', anchor=tk.CENTER, command=self.pressMultiply)
        multiply.grid(row=3, column=3, padx=10, pady=10, sticky='EW')
        divide = tk.Button(self, text='÷', font=('Helvetica', 16), width=3, bg='#c1412e', anchor=tk.CENTER, command=self.pressDivide)
        divide.grid(row=3, column=4, padx=10, pady=10, sticky='EW')
        modulus = tk.Button(self, text='%', font=('Helvetica', 16), width=3, bg='#c1412e', anchor=tk.CENTER, command=self.pressModulus)
        modulus.grid(row=4, column=3, padx=10, pady=10, sticky='EW')
        power = tk.Button(self, text='x\u207F', font=('Helvetica', 16), width=3, bg='#c1412e', anchor=tk.CENTER, command=self.pressPower)
        power.grid(row=4, column=4, padx=10, pady=10, sticky='EW')
        sqrt = tk.Button(self, text='\u221Ax', font=('Helvetica', 16), width=3, bg='#c1412e', anchor=tk.CENTER, command=self.pressSqrt)
        sqrt.grid(row=5, column=4, padx=10, pady=10, sticky='EW')
        equal = tk.Button(self, text='=', font=('Helvetica', 16), width=3, bg='#603632', anchor=tk.CENTER, command=self.pressEqual)
        equal.grid(row=5, column=3, padx=10, pady=10, sticky='EW')

        # Column and row spaces
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)

    def press1(self):
        if len(self.currentNumber) < 13:
            self.currentNumber += '1'
            self.numberDisplay['text'] = self.currentNumber

    def press2(self):
        if len(self.currentNumber) < 13:
            self.currentNumber += '2'
            self.numberDisplay['text'] = self.currentNumber

    def press3(self):
        if len(self.currentNumber) < 13:
            self.currentNumber += '3'
            self.numberDisplay['text'] = self.currentNumber

    def press4(self):
        if len(self.currentNumber) < 13:
            self.currentNumber += '4'
            self.numberDisplay['text'] = self.currentNumber

    def press5(self):
        if len(self.currentNumber) < 13:
            self.currentNumber += '5'
            self.numberDisplay['text'] = self.currentNumber

    def press6(self):
        if len(self.currentNumber) < 13:
            self.currentNumber += '6'
            self.numberDisplay['text'] = self.currentNumber
    
    def press7(self):
        if len(self.currentNumber) < 13:
            self.currentNumber += '7'
            self.numberDisplay['text'] = self.currentNumber

    def press8(self):
        if len(self.currentNumber) < 13:
            self.currentNumber += '8'
            self.numberDisplay['text'] = self.currentNumber
        
    def press9(self):
        if len(self.currentNumber) < 13:
            self.currentNumber += '9'
            self.numberDisplay['text'] = self.currentNumber

    def press0(self):
        if len(self.currentNumber) < 13:
            self.currentNumber += '0'
            self.numberDisplay['text'] = self.currentNumber

    def press00(self):
        if len(self.currentNumber) < 12:
            self.currentNumber += '00'
            self.numberDisplay['text'] = self.currentNumber

    def pressDPoint(self):
        if '.' not in self.currentNumber and len(self.currentNumber) < 12:
            self.currentNumber += '.'
            self.numberDisplay['text'] = self.currentNumber

    def pressC(self):
        self.ans = '0'
        self.currentNumber = ''
        self.op = ''
        self.hasAns = False
        self.numberDisplay['text'] = self.currentNumber

    def pressCE(self):
        self.currentNumber = ''
        self.numberDisplay['text'] = self.currentNumber

    def pressBackSpace(self):
        if len(self.currentNumber) > 0:
            self.currentNumber = self.currentNumber[:-1]
            self.numberDisplay['text'] = self.currentNumber

    def pressAdd(self):
        self.makeOperations()
        self.op = '+'

    def pressSubstract(self):
        self.makeOperations()
        self.op = '-'

    def pressMultiply(self):
        self.makeOperations()
        self.op = '*'

    def pressDivide(self):
        self.makeOperations()
        self.op = '/'

    def pressModulus(self):
        self.makeOperations()
        self.op = '%'

    def pressPower(self):
        self.makeOperations()
        self.op = '**'

    def pressSqrt(self):
        if self.hasAns:
            self.ans = "{:.2f}".format(float(self.ans) ** (0.5))
        else: 
            self.ans = "{:.2f}".format(float(self.currentNumber) ** (0.5))
        self.hasAns = True
        self.currentNumber = ''
        self.numberDisplay['text'] = self.ans

    def pressEqual(self):
        self.makeOperations()
        self.op = ''

    def makeOperations(self):
        if self.op == '+':
            self.ans = "{:.2f}".format(float(self.ans) + float(self.currentNumber))
        elif self.op == '-':
            self.ans = "{:.2f}".format(float(self.ans) - float(self.currentNumber))
        elif self.op == '*':
            self.ans = "{:.2f}".format(float(self.ans) * float(self.currentNumber))
        elif self.op == '/':
            self.ans = "{:.2f}".format(float(self.ans) / float(self.currentNumber))
        elif self.op == '%':
            self.ans = "{:.2f}".format(float(self.ans) % float(self.currentNumber))
        elif self.op == '**':
            self.ans = "{:.2f}".format(float(self.ans) ** float(self.currentNumber))
        else:
            if not self.hasAns:
                self.ans = self.currentNumber

        self.hasAns = True
        self.currentNumber = ''
        self.numberDisplay['text'] = self.ans