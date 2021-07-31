# Aim:
# A program to read a string from the user and append it into a file.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


if __name__ == '__main__':
    file = open('test.txt', 'wt')
    file.write(input("Enter a sentence\n"))
    file.close()
    file = open('test.txt', 'rt')
    print(file.read())
    file.close()
