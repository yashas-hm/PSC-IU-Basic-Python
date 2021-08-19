# Demonstrate Overriding and methods to overcome.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


class Parent:
    def __init__(self):
        self.value = "Parent"

    def show(self):
        print(self.value)


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.value = "Child"

    def show(self):
        print(self.value)


if __name__ == '__main__':
    p = Parent()
    c = Child()
    p.show()
    c.show()
