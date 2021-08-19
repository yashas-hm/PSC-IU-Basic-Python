# Write a menu driven program to implement the following methods on List.
# (1) Create (2) Update particular element of list (3) Append to the list
# (4) Delete whole list (5) Delete particular element (6) Sort the list (7) Find length
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


if __name__ == '__main__':
    driver_list = []
    ch = '1'
    while ch != '8':
        print('Choose form the following\n'
              '1. Update element\n'
              '2. Add to list\n'
              '3. Delete whole list\n'
              '4. Delete particular element\n'
              '5. Sort the list\n'
              '6. Find length\n'
              '7. Show List\n'
              '8. Exit')
        ch = str(input('Enter choice : '))
        if ch == '1':
            element = int(input('Enter number to update : '))
            for i in range(len(driver_list)):
                if element == driver_list[i]:
                    update = int(input('Enter update value : '))
                    driver_list[i] = update
                    break

                if i == len(driver_list) - 1:
                    print('element not found')
        elif ch == '2':
            element = int(input('Enter number to append : '))
            driver_list.append(element)
        elif ch == '3':
            driver_list.clear()
        elif ch == '4':
            element = int(input('Enter number to delete : '))
            try:
                driver_list.remove(element)
            except ValueError:
                print('element not found')
        elif ch == '5':
            driver_list = driver_list.sort()
        elif ch == '6':
            print('length of list is : {}'.format(len(driver_list)))
        elif ch == '7':
            print(driver_list)
        elif ch == '8':
            break
        else:
            print('Wrong choice choose again!')
