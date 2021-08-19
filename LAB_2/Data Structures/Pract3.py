# Implement a Singly Linked List. (Insert, Display, Delete).
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        global prev
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next

        temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(" %d" % temp.data, end=' ')
            temp = temp.next
        print()


if __name__ == '__main__':
    sll = LinkedList()
    sll.push(1)
    sll.push(3)
    sll.push(5)

    print('Linked List : ')

    sll.print_list()
    sll.delete_node(3)

    print('Linked List : ')
    sll.print_list()
