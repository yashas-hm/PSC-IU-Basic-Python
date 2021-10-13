# Convert a 1D array to a 2D array with 2 rows and 5 columns.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import numpy as np

if __name__ == '__main__':
    d = []

    for i in range(100):
        d.append(i)

    arr = np.array(d)

    arr = np.reshape(arr, (-1, 10))

    print(arr)
