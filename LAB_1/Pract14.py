# Aim:
# Write a function to find out factorial of a given number.
# I) without recursion
# II) with recursion
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


def recursive_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n - 1)


def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


if __name__ == '__main__':
    a = int(input("Enter a Number : "))
    print("Factorial with recursion : {}".format(recursive_factorial(a)))
    print("Factorial without recursion : {}".format(fact(a)))
