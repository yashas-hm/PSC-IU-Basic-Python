# Write a Python Program that returns a match where the string contains a white
# space character.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import re


def search(data):
    return re.search('.*\s', str(data)).group()


if __name__ == '__main__':
    s = 'the university indus'
    print(search(s))