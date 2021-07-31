# Aim:
# A program to read the contents of a file in reverse order.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


if __name__ == '__main__':
    for line in reversed(list(open('test1.txt'))):
        print(line, end='')
