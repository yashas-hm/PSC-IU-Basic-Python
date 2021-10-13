# Create a tkinter GUI to implement a calculator.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import tkinter as tk

operator = ''
operand = ''
operand_str = ''
data = 0


def gui(root):
    root.title("Calculator")
    root.geometry('480x640+500+100')
    root['padx'] = 8
    root['pady'] = 8

    global operator
    global operand
    global operand_str

    root.rowconfigure(0, weight=30)
    root.rowconfigure(1, weight=10)
    root.rowconfigure(2, weight=10)
    root.rowconfigure(3, weight=10)
    root.rowconfigure(4, weight=10)
    root.columnconfigure(0, weight=10)
    root.columnconfigure(1, weight=10)
    root.columnconfigure(2, weight=10)
    root.columnconfigure(3, weight=10)

    entry = tk.Entry(root, font=('Calibri', 40), justify='right')
    entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

    btn1 = tk.Button(root, text='1', command=add_to_operand_str(entry, 1))
    btn1.grid(row=1, column=0, sticky='nsew')
    btn2 = tk.Button(root, text='2', command=add_to_operand_str(entry, 2))
    btn2.grid(row=1, column=1, sticky='nsew')
    btn3 = tk.Button(root, text='3', command=add_to_operand_str(entry, 3))
    btn3.grid(row=1, column=2, sticky='nsew')
    div = tk.Button(root, text='/', command=operator_btn(entry, '/'))
    div.grid(row=1, column=3, sticky='nsew')

    btn4 = tk.Button(root, text='4', command=add_to_operand_str(entry, 4))
    btn4.grid(row=2, column=0, sticky='nsew')
    btn5 = tk.Button(root, text='5', command=add_to_operand_str(entry, 5))
    btn5.grid(row=2, column=1, sticky='nsew')
    btn6 = tk.Button(root, text='6', command=add_to_operand_str(entry, 6))
    btn6.grid(row=2, column=2, sticky='nsew')
    mul = tk.Button(root, text='*', command=operator_btn(entry, '*'))
    mul.grid(row=2, column=3, sticky='nsew')

    btn7 = tk.Button(root, text='7', command=add_to_operand_str(entry, 7))
    btn7.grid(row=3, column=0, sticky='nsew')
    btn8 = tk.Button(root, text='8', command=add_to_operand_str(entry, 8))
    btn8.grid(row=3, column=1, sticky='nsew')
    btn9 = tk.Button(root, text='9', command=add_to_operand_str(entry, 9))
    btn9.grid(row=3, column=2, sticky='nsew')
    sub = tk.Button(root, text='-', command=operator_btn(entry, '-'))
    sub.grid(row=3, column=3, sticky='nsew')

    clear = tk.Button(root, text='clear')
    clear.grid(row=4, column=0, sticky='nsew')
    btn0 = tk.Button(root, text='0', command=add_to_operand_str(entry, 0))
    btn0.grid(row=4, column=1, sticky='nsew')
    eq = tk.Button(root, text='=', command=equal(entry))
    eq.grid(row=4, column=2, sticky='nsew')
    add = tk.Button(root, text='+')
    add.grid(row=4, column=3, sticky='nsew', command=operator_btn(entry, '+'))


def clear(entry):
    global operator
    global operand
    global operand_str
    operator = ''
    operand = ''
    operand_str = ''
    entry.delete(0, tk.END)


def add_to_operand_str(entry, data):
    global operand_str
    operand_str += str(data)
    set_text(entry, data)


def operator_btn(entry, data):
    global operator
    global operand
    global operand_str
    operator = data
    operand = operand_str
    operand_str = ''
    set_text(entry, data)


def equal(entry):
    global operator
    global operand
    global operand_str
    global data
    if operator == '+':
        data = int(operand) + int(operand_str)
    elif operator == '-':
        data = int(operand) - int(operand_str)
    elif operator == '/':
        data = int(operand) / int(operand_str)
    elif operator == '*':
        data = int(operand) * int(operand_str)
    entry.delete(0, tk.END)
    entry.insert(0, str(data))


def set_text(entry, text):
    entry.insert(tk.END, str(text))


if __name__ == '__main__':
    window = tk.Tk()
    gui(window)
    window.mainloop()
