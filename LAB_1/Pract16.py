# Aim:
# Demonstrate Function Scoping.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


def function():
    print("This is function")

    def inner_function():
        print("This is inner function")

    inner_function()

    i = 1
    for i in range(1):
        print(i+1)

    print(i)


if __name__ == '__main__':
    function()
