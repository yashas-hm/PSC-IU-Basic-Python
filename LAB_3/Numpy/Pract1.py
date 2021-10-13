# Extract all odd numbers from the array using “where” clause.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import numpy as np


if __name__ == '__main__':
    d = []

    for i in range(100):
        d.append(i)

    arr = np.array(d)

    print(np.where(arr % 2 != 0))
