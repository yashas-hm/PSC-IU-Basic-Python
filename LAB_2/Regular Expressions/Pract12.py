# Write a regular expression to retrieve DOB from the string.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import re


def search(data):
    return re.findall(r'(\d{2}/\d{2}/\d{4})', str(data))


if __name__ == '__main__':
    s = '08/05/2001 is my birthdate'
    print(search(s))