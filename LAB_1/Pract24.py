# Aim:
# A program to copy the contents of one file into another.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


if __name__ == '__main__':
    file = open('test1.txt', 'wt')
    file.write('Hello\n')
    file.write('World\n')
    file.write('This is Yashas\n')
    file.write('Programming on Python\n')
    file.write('Bye\n')
    file.close()

    file = open('test1.txt', 'rt')
    print(file.read())
    file.close()

    with open('test1.txt', 'rt') as file, open('result.txt', 'wt') as file1:
        for line in file:
            file1.write(line)
        file.close()
        file1.close()

    file = open('result.txt', 'rt')
    print(file.read())
    file.close()