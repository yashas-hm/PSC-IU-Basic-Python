# Write a regular expression to retrieve all words starting with “a”.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import re


def search(data):
    return re.findall(r'\ba\w+', str(data))


if __name__ == '__main__':
    s = 'all am ban adolf audacity christ'
    print(search(s))