import Pract1_1 as p1
import Pract1_2 as p2
import Pract1_3 as p3
import Pract1_4 as p4

# Implement following inheritance:
# (1) single (2) Multiple (3) Multilevel (4) Hybrid
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


if __name__ == '__main__':
    # Single Inheritance
    emp = p1.Person('yashas')
    print(emp.getName())
    print(emp.isEmployee())
    emp = p1.Employee('Someone')
    print(emp.getName())
    print(emp.isEmployee())

    # Multiple Inheritance
    data = p2.Derived()
    data.print_data()

    # Multilevel Inheritance
    grandchild = p3.GrandChild('Yashas', 20, 'Ahmedabad')
    print(grandchild.get_name(), grandchild.get_age(), grandchild.get_address())

    # Hybrid Inheritance
    grandchild = p4.GrandChild('Yashas', 20, 'Ahmedabad', '08/05/2001')
    print(grandchild.get_name(), grandchild.get_age(), grandchild.get_address(), grandchild.get_dob())
