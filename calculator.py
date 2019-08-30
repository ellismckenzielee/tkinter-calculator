import tkinter as tk
from tkinter import messagebox

def click(symbol):
    root.expression += (symbol)
    root.entry.set(root.expression)
    print(root.expression)

def quit():
    root.destroy() 

def reset():
    root.expression = ''
    root.entry.set('Enter expression')

def solve():
    if (root.entry.get() != root.expression):
        root.expression = root.entry.get()
    print(eval(root.expression))
    root.entry.set(str(eval(root.expression)))


if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title('Simple Calculator')
    root.expression = ''
    root.configure(background = 'white')
    root.entry = tk.StringVar()
    root.entry.set('Enter the expression')


    zero = tk.Button(root, text='0', command= lambda: click('0')).grid(row=5, column=0, ipadx=15, ipady=10, sticky='nsew')
    one = tk.Button(root, text='1', command= lambda: click('1')).grid(row=4, column=0, ipadx=15, ipady=10)
    two = tk.Button(root, text='2', command= lambda: click('2')).grid(row=4, column=1, ipadx=15, ipady=10)
    three = tk.Button(root, text='3', command= lambda: click('3')).grid(row=4, column=2, ipadx=15, ipady=10)
    four = tk.Button(root, text='4', command= lambda: click('4')).grid(row=3, column=0, ipadx=15, ipady=10)
    five = tk.Button(root, text='5', command= lambda: click('5')).grid(row=3, column=1, ipadx=15, ipady=10)
    six = tk.Button(root, text='6', command= lambda: click('6')).grid(row=3, column=2, ipadx=15, ipady=10)
    seven = tk.Button(root, text='7', command= lambda: click('7')).grid(row=2, column=0, ipadx=15, ipady=10)
    eight = tk.Button(root, text='8', command= lambda: click('8')).grid(row=2, column=1, ipadx=15, ipady=10)
    nine = tk.Button(root, text='9', command= lambda: click('9')).grid(row=2, column=2, ipadx=15, ipady=10)

    decimal = tk.Button(root, text='.', command= lambda: click('.')).grid(row=5, column=1, ipadx=15, ipady=10)
    equals = tk.Button(root, text='=', command= lambda: solve()).grid(row=5, column=2, ipadx=15, ipady=10)
    plus = tk.Button(root, text='+', command= lambda: click('+')).grid(row=5, column=3, ipadx=15, ipady=10)
    minus = tk.Button(root, text='-', command= lambda: click('-')).grid(row=4, column=3, ipadx=15, ipady=10)
    multiply = tk.Button(root, text='x', command= lambda: click('*')).grid(row=3, column=3, ipadx=15, ipady=10)
    divide = tk.Button(root, text='÷', command= lambda: click('/')).grid(row=2, column=3, ipadx=15, ipady=10)
    opening_bracket = tk.Button(root, text='(', command= lambda: click('(')).grid(row=1, column=0, ipadx=15, ipady=10)
    closing_bracket = tk.Button(root, text=')', command= lambda: click(')')).grid(row=1, column=1, ipadx=15, ipady=10)
    QUIT = tk.Button(root, text='Quit', command= lambda: quit()).grid(row=1, column=3, ipadx=10, ipady=15)
    RESET = tk.Button(root, text='Reset', command= lambda: reset()).grid(row=1, column=2, ipadx=10, ipady=15)

    entry_box = tk.Entry(root, textvariable=root.entry).grid(row=0, columnspan=4, ipadx=70, ipady=10)

    expression = ''
    root.mainloop()


