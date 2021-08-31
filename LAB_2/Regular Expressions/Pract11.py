# Write a regular expression to retrieve all words starting with ‘an’ or ‘ak’.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import re


def search(data):
    return re.findall(r'\ban\w+|\bak\w+', str(data))


if __name__ == '__main__':
    s = 'akter and anomaly akshay abnormal adjective'
    print(search(s))