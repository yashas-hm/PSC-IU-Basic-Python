# Replace all odd numbers in array with -1
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import numpy as np

if __name__ == '__main__':
    d = []

    for i in range(100):
        d.append(i)

    arr = np.array(d)

    arr[arr % 2 != 0] = -1

    print(arr)
