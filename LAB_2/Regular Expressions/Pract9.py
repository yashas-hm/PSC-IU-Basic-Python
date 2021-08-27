# Write a regular expression to retrieve all single digits from a string.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import re


def search(data):
    return re.findall(r'[0-9]', str(data))


if __name__ == '__main__':
    s = '224 ye3 skl8vw dac85'
    print(search(s))