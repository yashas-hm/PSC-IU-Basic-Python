# Implement following searching techniques:
# (1) Linear (2) Binary
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


def linear_search(arr, ele):
    for i in range(0, arr.__sizeof__()):
        if arr[i] == ele:
            return i

    return -1


def binary_search(arr, ele):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < ele:
            low = mid + 1
        elif arr[mid] > ele:
            high = mid - 1
        else:
            return mid

    return -1


if __name__ == '__main__':
    array = []
    for i in range(1, 200):
        array.append(i)

    element = int(input("Enter element to search : "))

    print("Performing Linear Search")
    pos = linear_search(array, element)

    if pos != -1:
        print("Element found at {}".format(pos))
    else:
        print("Element not found")

    print()

    print("Performing Binary Search")
    pos = binary_search(array, element)

    if pos != -1:
        print("Element found at {}".format(pos))
    else:
        print("Element not found")