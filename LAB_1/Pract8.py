# Aim:
# Write a python program to check entered year is leap year or not.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


def check_leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    a = int(input("Enter year : "))
    if check_leap(a):
        print("{} is a leap year".format(a))
    else:
        print("{} is not a leap year".format(a))
