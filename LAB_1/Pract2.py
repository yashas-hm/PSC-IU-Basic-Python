# Aim: Demonstrate arrays (Insertion,Deletion,arithmetic operations).
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066

arr = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    arr.append(6)
    print(arr)
    arr.remove(3)
    print(arr)
    add = sub = 0
    div = mul = 1.0
    for i in arr:
        add += i
        sub -= i
        div /= i
        mul *= i
    print(add, sub, div, mul)

