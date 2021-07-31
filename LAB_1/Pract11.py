# Aim:
# Write a Python program to check whether a specified value is contained in a group of values using function.
# Test Data:
# 3 -> [1, 5, 8, 3] : True
# 1-> [1, 5, 8, 3] : False
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


def find(a, arr):
    array = list(arr)
    return array.__contains__(a)


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7]
    element = int(input("Enter a number : "))
    print(find(element, data))

