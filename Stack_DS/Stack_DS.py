# You can implement stack through arrays or linked list

# Stack implementation through Arrays
class Array_Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        if not self.isEmpty():
            self.items.pop()
        else:
            raise IndexError("Stack is Empty")
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("Stack is Empty")
    
    def size(self):
        return len(self.items)
    
    def __repr__(self):
        return f"Stack: {self.items}"

stack = Array_Stack()
stack.push(100)
stack.push(12)
stack.push(9)
stack.push(6)
print(stack)
stack.pop()
print(stack.peek())
print(stack)

# Stack implementation through Linked List
import sys
sys.path.append("DSA\Linked_List_DS")

import Linked_List_DS

class Stack(Linked_List_DS.LinkedList): # Inheritance Class
    def __init__(self):
        super().__init__() # super() is to call the parent class to initialize any attributes in the parent class

    def push(self, data):
        self.add(data)

    def pop(self):
        if not self.head:
            raise IndexError("Stack is empty")

        deleted_node = self.head
        self.head = deleted_node.next_node

    def peek(self):
        if self.head:
            return f"[HeadStack: {self.head.data}]"
        else:
            raise IndexError("Stack is empty")

    def __repr__(self):
        # Return a string representation of the list
        # Takes O(n) time
        nodes = []
        current = self.head
        
        while current:
            if current == self.head:
                nodes.append(f"[HeadStack: {current.data}]")
            elif current.next_node == None:
                nodes.append(f"[TailStack: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            
            current = current.next_node
        return "--> ".join(nodes)
    
a = Stack()
a.push(10)
a.push(2)
a.push(-1)
a.push(15)
print(a)
a.pop()
print(a.peek())
print(a)