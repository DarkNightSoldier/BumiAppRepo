class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class BidirectionalNode(Node):
    def __init__(self, data):
        super().__init__()
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        temp = Node(data)
        if self.with_tail == False:
            if self.head == None:
                self.head = temp
                return 1
            current = self.head
            while current.next != None:
                current = current.next
            current.next = temp
        else:
            self.tail.next = temp

    def display(self):
        current = self.head
        while current != None:
            print(current, end = " => ")
            current = current.next
        print(None)

class LinkedListTail(LinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None

    def insert(self, data):
        temp = Node(data)
        self.tail.next = temp
        self.tail = self.tail.next

class DoubleLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def insert(self, data):
        temp = BidirectionalNode(data)
        if self.head == None:
            self.head = temp
            return 1
        prev = None
        current = self.head
        while current.next != None:
            prev = current
            current = current.next
        current.next = temp
        current.prev = prev

class DoubleLinkedListTail(LinkedListTail):
    def __init__(self):
        super().__init__()

    def insert(self, data):
        temp = BidirectionalNode(data)
        prev = self.tail # New previous.
        self.tail.next = temp # Update next.
        self.tail = self.tail.next
        self.prev = prev
  
if __name__ == '__main__':
    llist1 = LinkedList(with_tail = False)
    llist1.insert("A")
    llist1.insert("B")
    llist1.display()

    llist2 = LinkedList(with_tail = True)
    llist2.insert("C")
    llist2.insert("D")
    llist2.display()
    print(llist2.tail.data)