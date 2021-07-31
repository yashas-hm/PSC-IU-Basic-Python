# Aim: Perform Addition, Multiplication for Vectors and  Matrices.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066

matrix = []
vector = []

for i in range(1, 10):
    vector.append(i)

for i in range(3):
    arr = []
    for j in range(3):
        arr.append(vector[3 * i + j])
    matrix.append(arr)


def add():
    print("Sum of vectors is : {}".format(sum(vector)))
    print("Sum of Matrix is : {}".format(sum(map(sum, matrix))))


def multiply():
    mul = 1
    mul_m = 2
    for x in range(len(vector)):
        mul *= vector[x]

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            mul_m *= matrix[x][y]

    print("Product of vectors is : {}".format(mul))
    print("product of Matrix is : {}".format(mul_m))


if __name__ == '__main__':
    add()
    multiply()
