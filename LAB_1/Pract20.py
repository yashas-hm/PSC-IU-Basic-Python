# Aim:
# Write a python program to find out even numbers from a list using filter ().
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


if __name__ == '__main__':
    arr = []
    for i in range(1, 50):
        arr.append(i)

    print("Filtering out even numbers")

    filtered = list(filter(lambda x: x % 2 == 0, arr))
    print(filtered)
