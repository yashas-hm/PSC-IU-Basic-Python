# Get the common items between array1 and array2
# Input:
# array1 = [1,2,3,2,3,4,3,4,5,6]
# array2 = [7,2,10,2,7,4,9,4,9,8]
# Desired Output:
# array([2, 4])
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import numpy as np

if __name__ == '__main__':
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

    print(np.intersect1d(a, b))
