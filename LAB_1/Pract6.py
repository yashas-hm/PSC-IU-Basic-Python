# Aim: Write a python program to find out if a given number is even or odd using a user
# defined function.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


def odd_eve(n):
    return n % 2 == 0


if __name__ == '__main__':
    a = int(input("Enter a number "))
    if odd_eve(a):
        print("Number is even")
    else:
        print("Number is odd")
