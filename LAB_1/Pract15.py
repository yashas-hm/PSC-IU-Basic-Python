# Aim:
# Write a program to find out Fibonacci series using recursion and function as an object.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


if __name__ == '__main__':
    a = int(input("Enter a positive number "))
    if a <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(a):
            print(recursive_fibonacci(i), end=' ')
