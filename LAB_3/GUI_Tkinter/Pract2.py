# Create a dropdown list to select a city from the given list of cities.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066

import tkinter as tk


def gui(root):
    root.geometry('280x280+500+100')
    root.title('Dropdown')
    root['padx'] = 8
    root['pady'] = 8

    def show():
        label.config(text=selected.get())

    options = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    selected = tk.StringVar()

    selected.set("Monday")

    drop = tk.OptionMenu(root, selected, *options)
    drop.pack()

    tk.Button(root, text="show selection", command=show).pack()

    label = tk.Label(root, text=" ")
    label.pack()


if __name__ == '__main__':
    window = tk.Tk()
    gui(window)
    window.mainloop()
