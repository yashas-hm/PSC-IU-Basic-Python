class A:
    def __init__(self, cal):
        self.calc = cal

    def get_number(self):
        data = int(input("Please enter a number : "))
        self.calc.arithmetic_calc(data)
