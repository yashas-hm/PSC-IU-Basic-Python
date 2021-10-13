# Using the Turtle module in python, Draw Square, Rectangle, Star and explore various
# attributes with it (ex: background color, line fill, border color, etc...)
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import turtle as t


def square():
    screen = t.Screen()
    screen.bgcolor('light green')
    screen.title('square')

    pen = t.Turtle()
    for i in range(4):
        pen.forward(200)
        pen.right(90)

    screen.mainloop()


def rectangle():
    screen = t.Screen()
    screen.bgcolor('light green')
    screen.title('rectangle')

    pen = t.Turtle()
    pen.color('blue')
    d = [200, 100, 200, 100]
    for i in range(4):
        pen.forward(d[i])
        pen.right(90)

    screen.mainloop()


def star():
    screen = t.Screen()
    screen.bgcolor('light green')
    screen.title('star')

    pen = t.Turtle()
    pen.color('blue')
    pen.right(75)
    pen.forward(200)

    for i in range(4):
        pen.right(144)
        pen.forward(200)

    screen.mainloop()


if __name__ == '__main__':
    star()
