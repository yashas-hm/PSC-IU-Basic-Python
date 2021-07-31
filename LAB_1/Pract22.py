# Aim:
# A program to count the number of words, number of lines, occurrence of particular word, occurrence of
# particular character, number of blank spaces in a text file.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


if __name__ == '__main__':
    file = open('test1.txt', 'rt')
    data = file.read()
    chars = len(data)
    words = data.split(' ')

    print("Total characters in file : {}".format(chars))
    print("Total words in file : {}".format(len(words)))
    print("Total lines in file : {}".format(len(data.split('\n'))))

    for i in file:
        ctr = 0
        for j in file:
            if i == j:
                ctr = ctr + 1
        if ctr > 1:
            print('{} occurred {} times in the file'.format(i, ctr))

    for i in words:
        ctr = 0
        for j in words:
            if i == j:
                ctr = ctr + 1
        if ctr > 1:
            print('{} occurred {} times in the file'.format(i, ctr))

    ctr = 0
    for i in file:
        if i == ' ':
            ctr = ctr + 1

    print('Space occurred {} times in the file.'.format(ctr))
