# LinkedLists are fundamental data structures
# A LinkedList has a head and a tail - the first and last node value respectively
# Each node points only to a single node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node 
            return 
        self.insertBefore(self.head, node)