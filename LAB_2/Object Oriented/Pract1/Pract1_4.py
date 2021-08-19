# Hybrid Inheritance


class Base(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Child(Base):
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    def get_age(self):
        return self.age


class ChildDOB:
    def __init__(self, dob):
        self.dob = dob

    def get_dob(self):
        return self.dob


class GrandChild(Child, ChildDOB):
    def __init__(self, name, age, address, dob):
        Child.__init__(self, name, age)
        ChildDOB.__init__(self, dob)
        self.address = address

    def get_address(self):
        return self.address
