class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Singly_LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_first(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        # temp = self.head
        # self.head = new_node
        # self.head.next = temp

        # More Precise Way
        new_node.next = self.head
        self.head = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = new_node

    def traverse_ascending(self):
        if not self.head:
            print("List is Empty...")
        else:
            while self.head:
                print(self.head.data)
                self.head = self.head.next

    def reverse_singly_linkedlist(self):
        if not self.head:
            print("List is Empty...")
            return
        current = self.head
        prev = None

        while current:
            temp = current
            current = current.next
            temp.next = prev
            prev = temp

        self.head = prev
        self.traverse_ascending()

    def delete_first(self):
        self.head = self.head.next

    def delete_last(self):
        if not self.head:
            print("List is Empty...")
            return
        elif not self.head.next:
            self.head = None
            return
        temp = self.head
        prev = temp

        # while temp.next:
        #     prev = temp
        #     temp = temp.next

        # prev.next = None

        # another way to delete from last or capture second last element
        while temp.next.next:
            temp = temp.next
        temp.next = None


singly = Singly_LinkedList()
# singly.insert_at_first(10)
# singly.insert_at_first(20)
# singly.insert_at_first(30)
# singly.insert_at_first(40)
# singly.insert_at_first(50)

singly.insert_at_last(60)
singly.insert_at_last(70)
singly.insert_at_last(80)
singly.insert_at_last(90)

# singly.delete_first()
# singly.delete_last()
# singly.delete_last()
singly.reverse_singly_linkedlist()
# singly.traverse_ascending()
