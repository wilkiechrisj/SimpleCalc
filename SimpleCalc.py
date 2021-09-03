from tkinter import *
from tkinter import messagebox

def num(char):
    current = entry.get()
    entry.configure(state='normal')
    entry.delete(0, END)
    new = current + char
    if float(new) == 0:
        entry.configure(state='disabled')
        pass
    entry.insert(0, new)
    entry.configure(state='disabled')

def clear():
    entry.configure(state='normal')
    storage.clear()
    entry.delete(0, END)
    entry.configure(state='disabled')

def operation(symbol):
    num = entry.get()

    if not num:
        num = 0

    entry.configure(state='normal')
    entry.delete(0, END)
    storage.append(num)
    storage.append(symbol)
    entry.configure(state='disabled')

def calculate():
    num = entry.get()
    entry.configure(state='normal')

    if not num:
        num = '0'

    storage.append(num)

    calc = ''
    for element in storage:
        calc = calc + element

    entry.delete(0, END)
    try:
        entry.insert(0, eval(calc))
    except:
        messagebox.showerror(title='ZeroDivisionError', message='ZeroDivisionError')
    storage.clear()
    entry.configure(state='disabled')

window = Tk()
window.title('SimpleCalc')
window.geometry('400x400')

storage = []

entry = Entry(window, width=50, borderwidth=5)
entry.grid(row=0,column=0, columnspan=3, padx=20, pady=20)
entry.configure(state='disabled')

nine = Button(window, text='9', padx=10, pady=10, command=lambda: num('9'))
nine.grid(row=1, column=2)
eight = Button(window, text='8', padx=10, pady=10, command=lambda: num('8'))
eight.grid(row=1, column=1)
seven = Button(window, text='7', padx=10, pady=10, command=lambda: num('7'))
seven.grid(row=1, column=0)
six = Button(window, text='6', padx=10, pady=10, command=lambda: num('6'))
six.grid(row=2, column=2)
five = Button(window, text='5', padx=10, pady=10, command=lambda: num('5'))
five.grid(row=2, column=1)
four = Button(window, text='4', padx=10, pady=10, command=lambda: num('4'))
four.grid(row=2, column=0)
three = Button(window, text='3', padx=10, pady=10, command=lambda: num('3'))
three.grid(row=3, column=2)
two = Button(window, text='2', padx=10, pady=10, command=lambda: num('2'))
two.grid(row=3, column=1)
one = Button(window, text='1', padx=10, pady=10, command=lambda: num('1'))
one.grid(row=3, column=0)
zero = Button(window, text='0', padx=10, pady=10, command=lambda: num('0'))
zero.grid(row=4, column=2)

equals = Button(window, text='=', padx=10, pady=10, command=calculate)
equals.grid(row=4, column=1)

clear = Button(window, text='C', padx=10, pady=10, command=clear)
clear.grid(row=4, column=0)

plus = Button(window, text='+', padx=10, pady=10, command=lambda: operation('+'))
plus.grid(row=5, column=0)

minus = Button(window, text='-', padx=10, pady=10, command=lambda: operation('-'))
minus.grid(row=5, column=1)

multiply = Button(window, text='*', padx=10, pady=10, command=lambda: operation('*'))
multiply.grid(row=6, column=0)

divide = Button(window, text='/', padx=10, pady=10, command=lambda: operation('/'))
divide.grid(row=6, column=1)

window.mainloop()
