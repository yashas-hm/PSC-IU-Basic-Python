# Write a regular expression to retrieve all words starting with a numeric digit.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import re


def search(data):
    return re.findall(r'\b[0-9]\w+', str(data))


if __name__ == '__main__':
    s = '1shoe s2ss 3fff '
    print(search(s))