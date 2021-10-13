# Perform Matrix multiplication on 2 matrices.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import numpy as np

if __name__ == '__main__':
    a = np.array([[1, 2, 3],
                 [3, 4, 5],
                 [7, 6, 4]])

    b = np.array([[5, 2, 6],
                 [5, 6, 7],
                 [7, 6, 4]])

    print(a.dot(b))
