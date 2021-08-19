# Write a Python program which accepts a sequence of comma-separated
# numbers from the user and generate a list and a tuple with those numbers.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


if __name__ == '__main__':
    data = str(input('Enter comma separated string : '))
    list_1 = data.split(',')
    tuple_1 = tuple(list_1)
    print('List is : ', end=' ')
    print(list_1)
    print('Tuple is :', end=' ')
    print(tuple_1)
