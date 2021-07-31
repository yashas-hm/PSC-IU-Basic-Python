# Aim:
# Write a Python program to check whether a specified value is contained in a group of values using lambda function.
# Test Data:
# 3 -> [1, 5, 8, 3] : True
# 1-> [1, 5, 8, 3] : False
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7]
    element = int(input("Enter a number : "))
    find = lambda a, b: list(b).__contains__(a)
    print(find(element, data))
