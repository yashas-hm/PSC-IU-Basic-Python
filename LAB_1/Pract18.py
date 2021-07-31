# Aim:
# Write a Python program to find whether a given string ends with a given character using Lambda.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


if __name__ == '__main__':
    string = "Hello World, this is testing"
    check_str = input("Enter a character : ")
    check = lambda a, b: str(a).endswith(a)
    if not check(string, check_str):
        print("{} ends with {}".format(string, check_str))
    else:
        print("\"{}\" does not end with \"{}\"".format(string, check_str))
