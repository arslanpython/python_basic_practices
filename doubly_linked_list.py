class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly_Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_first(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp

            current = self.tail
            while current.prev:
                current = current.prev

            current.prev = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.tail
            self.tail = new_node
            self.tail.prev = temp

            current = self.head
            while current.next:
                current = current.next

            current.next = new_node

    def traverse_ascending(self):
        print("\n--> Traverse in Ascending Order Using Head * pointer")
        if not self.head:
            print('Empty List...')
            return

        while self.head:
            print(self.head.data)
            self.head = self.head.next

    def traverse_descending(self):
        print("\n--> Traverse in Descending Order Using Tail * pointer ")
        if not self.tail:
            print('Empty List...')
            return

        while self.tail:
            print(self.tail.data)
            self.tail = self.tail.prev

    def reverse_doubly_linked_list(self):
        # Reverse Doubly LinkedList to Much Simple as Compared to Singly LinkedList

        # temp = self.head
        # self.head = self.tail
        # self.tail = temp

        # OR More Precise Way
        self.head, self.tail = self.tail, self.head

        if not self.tail:
            print('Empty List...')
            return

        print('--> Print Data Using Tail and next pointer :- ')

        while self.tail:
            print(self.tail.data)
            self.tail = self.tail.next

        print('\n--> Print Data Using Head and prev pointer:- ')
        while self.head:
            print(self.head.data)
            self.head = self.head.prev

    def delete_first(self):
        if not self.head:
            print('Empty...')
        else:
            self.head = self.head.next
            current = self.tail
            while current.prev.prev:
                current = current.prev

            current.prev = None

    def delete_last(self):
        if not self.head:
            print('Empty List...')
            return

        self.tail = self.tail.prev
        if not self.head.next:
            self.head = None
        else:
            current = self.head
            while current:
                temp = current
                current = current.next

                if not current.next:
                    temp.next = None
                    return


obj = Doubly_Linked_list()

# obj.insert_at_first(10)
# obj.insert_at_first(20)
# obj.insert_at_first(30)
# obj.insert_at_first(40)

obj.insert_at_last(10)
obj.insert_at_last(20)
# obj.insert_at_last(30)
# obj.insert_at_last(40)

# obj.delete_first()
obj.delete_last()
obj.traverse_ascending()
obj.traverse_descending()
# obj.reverse_doubly_linked_list()
