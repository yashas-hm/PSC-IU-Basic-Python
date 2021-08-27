# Write a regular expression to retrieve the last word from the string
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import re


def search(data):
    return re.search(r'\b(\w+)$', str(data)).group()


if __name__ == '__main__':
    s = 'hello world this is yashas'
    print(search(s))