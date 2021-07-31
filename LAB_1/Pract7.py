# Aim:
# 1) Addition of first 15 numbers using loop.
# 2) Addition of any 15 numbers using loop.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import random


def first_15():
    add = 0
    for i in range(1, 16):
        add += i
    print("Sum is {}".format(add))


def rand_15():
    add = 0
    for i in range(1, 16):
        add += random.randint(1,200)
    print("Sum is {}".format(add))


if __name__ == '__main__':
    first_15()
    rand_15()
