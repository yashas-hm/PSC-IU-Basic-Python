from Pract21_a import A


class B:
    def arithmetic_calc(self, data):
        number = int(data)
        choice = 0
        while choice != 5:
            print("Enter 1 to Add"
                  "\nEnter 2 to Subtract"
                  "\nEnter 3 to divide"
                  "\nEnter 4 to Multiply"
                  "\nEnter 5 to new number"
                  "\nEnter 6 to Exit")
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
            elif choice == 5:
                A(self).get_number()
            else:
                if choice != 6:
                    print("Wrong choice enter again!")
