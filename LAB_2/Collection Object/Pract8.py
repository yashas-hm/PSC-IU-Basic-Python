# Write a menu driven program to implement following methods on Dictionary.
# (1) Create (2) Update particular element of dictionary (3) Append to the
# dictionary (4) Delete whole dictionary (5) Delete particular element (6) Sort
# the dictionary (7) Find length
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


if __name__ == '__main__':
    driver_dictionary = dict()
    ch = '1'
    while ch != '8':
        print('Choose form the following\n'
              '1. Update element\n'
              '2. Add to dictionary\n'
              '3. Delete whole dictionary\n'
              '4. Delete particular element\n'
              '5. Sort the dictionary\n'
              '6. Find length\n'
              '7. Show dictionary\n'
              '8. Exit')
        ch = str(input('Enter choice : '))
        if ch == '1':
            element = int(input('Enter key to update : '))
            for i in driver_dictionary.keys():
                if element == i:
                    update = int(input('Enter update value : '))
                    driver_dictionary[element] = update
                    break
        elif ch == '2':
            key = int(input('Enter key to append : '))
            element = int(input('Enter number to append : '))
            driver_dictionary[key] = element
        elif ch == '3':
            driver_dictionary.clear()
        elif ch == '4':
            element = int(input('Enter key to delete : '))
            try:
                del driver_dictionary[element]
            except ValueError:
                print('element not found')
        elif ch == '5':
            driver_dictionary = sorted(driver_dictionary)
        elif ch == '6':
            print('length of dictionary is : {}'.format(len(driver_dictionary)))
        elif ch == '7':
            print(driver_dictionary)
        elif ch == '8':
            break
        else:
            print('Wrong choice choose again!')