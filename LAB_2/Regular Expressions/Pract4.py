# Write a Regular Expression to find Words or strings having three characters and
# with ‘m’ as first character.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import re


def search(data):
    return re.findall(r'\bm[a-zA-Z]{2}\b', str(data))


if __name__ == '__main__':
    s = 'mom mum dot mode mole ude mol'
    print(search(s))