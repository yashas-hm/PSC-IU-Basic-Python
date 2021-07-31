# Aim:
# Write a Python program to print the calendar of a given month and year.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import calendar

if __name__ == '__main__':
    month = int(input("Enter number of month : "))
    year = int(input("Enter year : "))
    print(calendar.month(year, month))
