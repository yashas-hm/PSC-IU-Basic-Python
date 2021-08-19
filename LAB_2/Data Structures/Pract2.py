# Implement following sorting algorithms.
# (1) Selection (2) Merge (3) Tim
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


def selection_sort(arr):
    array = list(arr)
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

    return array


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    array = list(arr)

    if l < r:
        m = l + (r - l) // 2

        merge_sort(array, l, m)
        merge_sort(array, m + 1, r)
        merge(array, l, m, r)

    return array


def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def calcMinRun(n):
    r = 0
    while n >= 32:
        r |= n & 1
        n >>= 1
    return n + r


def tim_sort(array):
    arr = list(array)
    n = len(arr)
    minRun = calcMinRun(n)
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size
    return arr


if __name__ == '__main__':
    arr = [2, 43, 54, 22, 30, 77]
    print(selection_sort(arr))
    print(merge_sort(arr, 0, len(arr)-1))
    print(tim_sort(arr))