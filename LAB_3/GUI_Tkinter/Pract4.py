# Create Registration window.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import tkinter as tk


def gui(root):
    root.geometry('480x280+400+100')
    root['padx'] = 8
    root['pady'] = 8
    root.title('Registration Window')

    root.rowconfigure(0, weight=10)
    root.rowconfigure(1, weight=10)
    root.rowconfigure(2, weight=10)
    root.rowconfigure(3, weight=10)
    root.rowconfigure(4, weight=10)
    root.rowconfigure(5, weight=10)
    root.rowconfigure(6, weight=10)
    root.rowconfigure(7, weight=10)
    root.columnconfigure(0, weight=10)
    root.columnconfigure(1, weight=10)
    root.columnconfigure(2, weight=10)

    name_lab = tk.Label(root, text='Name :')
    name_lab.grid(row=0, column=0, sticky='nsw')
    name = tk.Entry(root)
    name.grid(row=1, column=0, columnspan=3, sticky='nsew')
    email_lab = tk.Label(root, text='E-Mail :')
    email_lab.grid(row=2, column=0, sticky='nsw')
    email = tk.Entry(root)
    email.grid(row=3, column=0, columnspan=3, sticky='nsew')
    pass_lab = tk.Label(root, text='Password :')
    pass_lab.grid(row=4, column=0, sticky='nsw')
    password = tk.Entry(root, show='*')
    password.grid(row=5, column=0, columnspan=3, sticky='nsew')
    submit = tk.Button(root, text='Submit')
    submit.grid(row=7, column=1, sticky='nsew')


if __name__ == '__main__':
    window = tk.Tk()
    gui(window)
    window.mainloop()
