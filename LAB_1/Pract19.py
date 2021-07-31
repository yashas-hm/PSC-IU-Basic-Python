# Aim:
# Prime or not prime. Input: L= [3,4,6,9,11] Output: L= [P, NP, NP, NP, P] using map function.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


def check(num):
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    if flag:
        return 'NP'
    else:
        return 'P'


if __name__ == '__main__':
    arr = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
    result = map(check, arr)
    print(list(arr))
    print(list(result))
