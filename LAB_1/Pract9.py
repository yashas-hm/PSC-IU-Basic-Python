# Aim:
# Write a Python program which accepts the user's first and last name and print them in reverse order with a
# space between them.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


if __name__ == '__main__':
    first = input("Enter first name : ")
    last = input("Enter last name : ")
    print("{} {}".format(first[::-1], last[::-1]))

