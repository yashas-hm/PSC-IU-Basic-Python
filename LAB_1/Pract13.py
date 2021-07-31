# Aim:
# Write a function to find out x^y. Function should find out the square of x in case of default argument passing.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


def raise_to(number, exponent=2):
    print("{} raise to {} is : {}".format(number, exponent, number ** exponent))


if __name__ == '__main__':
    a = int(input("Enter a number : "))
    b = int(input("Enter another number : "))
    raise_to(a, b)
    raise_to(a)
