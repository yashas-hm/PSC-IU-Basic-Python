# Write a Python Program that searches a string to see if it starts with "The '' and
# ends with "Indus".
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import re


def search(data):
    return re.findall(r'^\bthe.*indus\b$', str(data))


if __name__ == '__main__':
    s = 'the university indus'
    print(search(s))

