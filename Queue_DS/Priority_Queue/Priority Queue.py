# Priority Queue implementation using Binary Heap

# This is Priority Queue implementation using a Min Heap
class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def isEmpty(self):
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)
    
    def parent(self, index):
        return (index - 1) // 2
    
    def leftchild(self, index):
        return 2 * index + 1
    
    def rightchild(self, index):
        return 2 * index + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def peek(self):
        return self.heap[0] if not self.isEmpty() else None
    
    def heapify_up(self, index): # Swimming or Bubbling Up
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            parent_index = self.parent(index)
            self.swap(index, parent_index)
            index = parent_index
    
    def heapify_down(self, index): # Sinking or Bubbling Down  
        smallest = index
        left = self.leftchild(index)
        right = self.rightchild(index)
            
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down(smallest)
    
    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def poll(self): # Remove the root
        if not self.isEmpty():
            self.swap(0, len(self.heap) - 1)
            self.heap.pop()
            self.heapify_down(0)

    def display(self):
        if self.isEmpty():
            print("Priority Queue is Empty")
            return
        
        def print_tree(node, level=0):
            if node < len(self.heap):
                print(" " * level + str(self.heap[node]))
                left = self.leftchild(node)
                right = self.rightchild(node)
                print_tree(left, level + 1)
                print_tree(right, level + 1)
        
        print_tree(0)


a = PriorityQueue()
a.insert(10)
a.insert(2)
a.insert(0)
a.insert(4)
a.insert(2)
a.insert(3)
a.insert(1)
print(a.display())
  

    

