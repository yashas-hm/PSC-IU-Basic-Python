# Do following:
# 1) Define and Call user defined function for n numbers one by one.
# 2) Check each element is Even or Odd and Print it.(Use Class Variable)
# 3) Print List of even numbers and odd numbers
# 4) Print total number of Even numbers and Total number of Odd Numbers.
# Example:  1) function(21), function(22), function(35),function(36),function(40).
#           2) 21 is odd, 22 is even, 35 is odd,36 is even, 40 is even.
#           3) Even={22,36,40} Odd={21,35}
#           4) total number of even = 3, total number of odd=2
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


class OddEven:
    odd = set()
    even = set()

    def check_data(self, data):
        if data%2==0:
            self.even.add(data)
            print('{} is even'.format(data))
        else:
            self.odd.add(data)
            print('{} is odd'.format(data))

    def total(self):
        print('Total even numbers is {}'.format(len(self.even)))
        print('Total odd numbers is {}'.format(len(self.odd)))

    def show(self):
        print('Even : {}'.format(sorted(self.even)))
        print('Odd : {}'.format(sorted(self.odd)))


if __name__ == '__main__':
    oe = OddEven()
    oe.check_data(21)
    oe.check_data(33)
    oe.check_data(24)
    oe.check_data(94)
    oe.check_data(2)
    oe.show()
    oe.total()