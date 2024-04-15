class Node:
    
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None
    
    def __repr__(self):
        return f"<Node data: {self.data}>"
    
class Doubly_LinkedList: # <-- Doubly Linked List 
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self): # <-- To check if the list is empty or not
        return self.head == None
    
    def addFirst(self, data): 
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node
    
    def addLast(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    def insert(self, data, index):
        # Inserts a new Node containing data at index position
        # Insertion takes O(1) time but finding the node at the insertion point takes O(n) time
        # Takes overall O(n) time
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1
                
            new.next_node = current.next_node
            new.prev_node = current

            current.next_node.prev_node = new
            current.next_node = new

    def __repr__(self):
        # Return a string representation of the list
        # Takes O(n) time
        nodes = []
        current = self.head
        
        while current:
            if current == self.head and current.prev_node == None:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node == None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            
            current = current.next_node
        return "<--> ".join(nodes)

a = Doubly_LinkedList()
a.addFirst(10)
a.addFirst(5)
a.addFirst(0)
a.addFirst(50)
print(a)
a.insert(100, 2)
a.insert(200, 3)
print(a)
a.addLast(-1)
print(a)
