# Write a regular expression to retrieve all words with 3,4 or 5 character length.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import re


def search(data):
    return re.findall(r'\b[a-zA-Z0-9]{3,5}\b', str(data))


if __name__ == '__main__':
    s = 'hello him hi supp wannabe sing petal'
    print(search(s))