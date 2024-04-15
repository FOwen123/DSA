# Indexed Priority Queue implementation using Min Binary Heap

class IndexedPQ:
    def __init__(self):
        self.heap = [] # (value, index) pairs
        self.position_map = {} # Mapping of item index to its position in the heap
        self.inverse_map = {} # Mapping of heap position to item index

    def isEmpty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)
    
    # ki = key index
    def parent(self, ki):
        return (ki - 1) // 2
    
    # ki = key index
    def leftchild(self, ki):
        return 2 * ki + 1
    
    # ki = key index
    def rightchild(self, ki):
        return 2 * ki + 2
    
    def insert(self, ki, value):
        if ki in self.position_map:
            raise ValueError(f"Index: {ki}, already existed")
        
        entry = (value, ki)
        self.heap.append(entry)
        heap_index = len(self.heap) - 1 # Find the bottom right position in the heap
        self.position_map[ki] = heap_index
        self.inverse_map[heap_index] = ki
        self.heapify_up(heap_index)

    # Swim
    def heapify_up(self, ki):
        parent = self.parent(ki)
        while ki > 0 and self.heap[ki][0] < self.heap[parent][0]:
            self.swap(ki, parent)
            ki = parent
            parent = self.parent(ki)

    # Sink
    def heapify_down(self, ki):
        leftchild_index = self.leftchild(ki)
        rightchild_index = self.rightchild(ki)
        smallest = ki

        if leftchild_index < len(self.heap) and self.heap[leftchild_index][0] < self.heap[smallest][0]:
            smallest = leftchild_index
        if rightchild_index < len(self.heap) and self.heap[rightchild_index][0] < self.heap[smallest][0]:
            smallest = rightchild_index
        
        if smallest != ki:
            self.swap(ki, smallest)
            self.heapify_down(smallest)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.position_map[self.heap[i][1]] = i # In the code above the self.heap[i] has been swapped
        self.position_map[self.heap[j][1]] = j # In the code above the self.heap[j] has been swapped
        self.inverse_map[i], self.inverse_map[j] = self.inverse_map[j], self.inverse_map[i]

    def update(self, ki, new_value):
        if ki not in self.position_map:
            raise ValueError(f"Index: {ki}, does not existed")

        heap_index = self.position_map[ki]
        old_value = self.heap[heap_index][0]
        self.heap[heap_index] = (new_value, ki)

        if new_value < old_value:
            self.heapify_up(heap_index)
        self.heapify_down(heap_index)

    def extract_min(self):
        if self.isEmpty():
            return None

        min_entry = self.heap[0]
        ki_to_remove = min_entry[1]
        heap_index = self.position_map[ki_to_remove]

        del self.position_map[ki_to_remove]
        del self.inverse_map[heap_index]

        if len(self.heap) == 1:
            return self.heap.pop()
        else:
            self.heap[0] = self.heap.pop() # the last element became the root
            self.position_map[self.heap[0][1]] = 0
            self.inverse_map[0] = self.heap[0][1]
            self.heapify_down(0)
        
        return ki_to_remove

    def display(self):
        print("Heap: ")
        for entry in self.heap:
            print(f"Key index: {entry[1]}, Value: {entry[0]}")
        print("Position Map: ")
        for ki, heap_index in self.position_map.items():
            print(f"Key index: {ki}, Heap Position: {heap_index}")
        print("Inverse Map: ")
        for heap_index, ki in self.inverse_map.items():
            print(f"Heap Position: {heap_index}, Key index: {ki}")


ipq = IndexedPQ()
ipq.insert(0, 5)
ipq.insert(1, 3)
ipq.insert(2, 8)
ipq.insert(3, 10)
ipq.display()
ipq.insert(4, 1)
ipq.display()
