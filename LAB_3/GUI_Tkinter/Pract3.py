# Write a tkinter code to place an image/picture in the window.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import tkinter as tk
from PIL import ImageTk, Image


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Baby Yoda')
    img = ImageTk.PhotoImage(Image.open('download.jpg'))
    image = tk.Label(root, image=img)
    image.pack(side='bottom', fill='both', expand='yes')
    root.mainloop()