# Linked List
class Node:
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return f"<Node data: {self.data}>" # <-- to give a more clear definition of the node


class LinkedList: # <-- Singly Linked List 
    def __init__(self):
        self.head = None
    
    def isEmpty(self): # <-- To check if the list is empty or not
        return self.head == None
    
    def size(self): # This takes O(n) runtime because we need to check every note 
        current = self.head 
        count = 0
        
        while current: # <-- the same as while current != None
            count += 1
            current = current.next_node
        
        return count
    
    def add(self, data): 
        # Add new Node containing data at head of the list
        # Takes O(1) time
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        # Search for the first node containing data that matches the key
        # Takes O(n) time
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
                 
        return f"'{key}' is not found"
    
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

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node
    
    def remove(self, key):
        # Remove Node containing data that matches the key
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return f"'{current} is removed'"
    
    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def __repr__(self):
        # Return a string representation of the list
        # Takes O(n) time
        nodes = []
        current = self.head
        
        while current:
            if current == self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node == None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            
            current = current.next_node
        return "--> ".join(nodes)

a = LinkedList()
a.add(1)
a.add(2)
a.add(3)
print(a.size())
print(a.search(2))
a.insert(10, 1)
print(a)
print(a.remove(2))
print(a)


