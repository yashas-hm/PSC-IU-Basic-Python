# Aim: Practical based on Strings (Length finding,change specific character,palindrome,concatenation)
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066

string = 'hello'


def length():
    print(len(string))


def change():
    print(string.replace('h', 'y', 1))


def palindrome():
    str2 = string[::-1]
    if string == str2:
        print('Palindrome')
    else:
        print('Not Palindrome')


def concatenation():
    str2 = ' world'
    print(string + str2)


if __name__ == '__main__':
    length()
    change()
    palindrome()
    concatenation()