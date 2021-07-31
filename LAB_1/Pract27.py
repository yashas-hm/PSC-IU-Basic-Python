# Aim:
# A program to read a file and capitalize the first letter of every word in the file.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066

if __name__ == '__main__':
    file = open('test4.txt', 'wt')
    file.write('hello world\n')
    file.write('this is yashas h majmudar')
    file.close()

    file = open('test4.txt', 'rt')
    data = []
    for i in file:
        data.append(i.title())

    file.close()
    file = open('test4.txt', 'wt')
    file.writelines(data)
    file.close()

    file = open('test4.txt', 'rt')
    print(file.read())
    file.close()
