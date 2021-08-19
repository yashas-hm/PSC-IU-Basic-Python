# Write a menu driven program to implement the following methods on set.
# (1) Create (2) Update particular element of set (3) Append to the set
# (4) Delete whole set (5) Delete particular element (6) Sort the set (7) Find length
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


if __name__ == '__main__':
    driver_set = set()
    ch = '1'
    while ch != '8':
        print('Choose form the following\n'
              '1. Update element\n'
              '2. Add to set\n'
              '3. Delete whole set\n'
              '4. Delete particular element\n'
              '5. Sort the set\n'
              '6. Find length\n'
              '7. Show Set\n'
              '8. Exit')
        ch = str(input('Enter choice : '))
        if ch == '1':
            element = int(input('Enter number to update : '))
            for i in driver_set:
                if element == driver_set:
                    update = int(input('Enter update value : '))
                    driver_set.remove(element)
                    driver_set.add(update)
                    break

                if i == len(driver_set) - 1:
                    print('element not found')
        elif ch == '2':
            element = int(input('Enter number to append : '))
            driver_set.add(element)
        elif ch == '3':
            driver_set.clear()
        elif ch == '4':
            element = int(input('Enter number to delete : '))
            try:
                driver_set.remove(element)
            except ValueError:
                print('element not found')
        elif ch == '5':
            driver_set = sorted(driver_set)
        elif ch == '6':
            print('length of set is : {}'.format(len(driver_set)))
        elif ch == '7':
            print(driver_set)
        elif ch == '8':
            break
        else:
            print('Wrong choice choose again!')
