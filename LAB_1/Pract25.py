# Aim:
# A program to read a text file and print all the numbers present in the text file.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


if __name__ == '__main__':
    file = open('test2.txt', 'rt')
    while 1:
        char = file.read(1)
        if char.isdigit():
            print(char, end=" ")

        if not char:
            break
