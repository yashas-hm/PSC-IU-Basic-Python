# Aim: Create a menu driven program to show various operators supported by python.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066

if __name__ == '__main__':
    number = int(input("Enter a number : "))
    choice = 0
    while choice != 5:
        print("Enter 1 to Add\nEnter 2 to Subtract\nEnter 3 to divide\nEnter 4 to Multiply\nEnter 5 to Exit")
        choice = int(input())
        if choice == 1:
            num = int(input("Enter number to add : "))
            print(number + num)
        elif choice == 2:
            num = int(input("Enter number to subtract : "))
            print(number - num)
        elif choice == 3:
            num = int(input("Enter number to multiply : "))
            print(number * num)
        elif choice == 4:
            num = int(input("Enter number to divide : "))
            print(number / num)
        else:
            if choice != 5:
                print("Wrong choice enter again!")
