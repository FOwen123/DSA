class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        hash_val = self._hash(key)
        if self.table[hash_val] is None:
            self.table[hash_val] = ListNode(key, value)
        else:
            current = self.table[hash_val]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = ListNode(key, value)
    
    def get(self, key):
        hash_val = self._hash(key)
        curr = self.table[hash_val]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None

    def delete(self, key):
        hash_val = self._hash(key)
        curr = self.table[hash_val]
        prev = None
        while curr:
            if curr.key == key:
                if prev == None:
                    self.table[hash_val] = curr.next
                else:
                    prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        
    def display(self):
        for i, node in enumerate(self.table):
            curr = node
            while curr:
                print(f"Bucket {i}: Key: {curr.key}, Value: {curr.value}")
                curr = curr.next

HT = HashTable(5)
HT.insert("Owen", 18)
HT.insert("Felix", 12)
HT.insert("Dad", 61)
HT.insert("Mom", 54)
HT.insert("Gabriel", 18)
HT.display()