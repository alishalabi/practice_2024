class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def print_list(self):
        current = self.head
        while current != self.tail:
            print(current.data)
            current = current.next
        print(self.tail.data)

# node1 = Node("A")
# node2 = Node("B")
# node3 = Node("C")
#
# LL = LinkedList()
# LL.add_node(node1)
# LL.add_node(node2)
# LL.add_node(node3)
#
# LL.print_list()
