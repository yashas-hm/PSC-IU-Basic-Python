# Write a Python program that matches a string that has an a followed by three 'b'.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import re


def search(data):
    return re.findall(r'ab{3}\b', str(data))


if __name__ == '__main__':
    s = 'aab bba abbb abbbb'
    print(search(s))