# HT Open Addressing using Quadratic probe function (x^2 + x) / 2
class HashTable:
    def __init__(self, size):
        if not self.is_power_of_two(size):
            raise ValueError("Hash table size must be the power of 2")

        self.size = size
        self.key = [None] * size
        self.value = [None] * size
        self.tombstone = object() # Special Marker for lazy deletion
    
    def is_power_of_two(self, n):
        return n % 2 == 0 and n != 0

    def _hashFunction(self, key):
        return hash(key) % self.size
    
    def _quadraticProbe(self, index, x): 
        return (index + x * (x + 1) // 2) % self.size

    def insert(self, key, value):
        index = self._hashFunction(key)
        attempt = 0

        while self.key[index]:
            attempt += 1
            index = self._quadraticProbe(index, attempt)

        self.key[index] = key
        self.value[index] = value
    
    def get(self, key):
        index = self._hashFunction(key)
        attempt = 0

        while self.key[index]:
            if self.key[index] == key:
                return self.value[index]
            attempt += 1
            index = self._quadraticProbe(index, attempt)
        
        return None
    
    def remove(self, key):
        index = self._hashFunction(key)
        attempt = 0

        while self.key[index]:
            if self.key[index] == key:
                self.key[index] = self.tombstone
                self.value[index] = None
                return
            attempt += 1
            index = self._quadraticProbe(index, attempt)
    
    def display(self):
        for i in range(self.size):
            if self.key[i]:
                print(f"Key: {self.key[i]}, Value: {self.value[i]}")

HT = HashTable(8)
HT.insert("apple", 5)
HT.insert("banana", 10)
HT.insert("avocado", 1)
HT.insert("cherry", 3)
HT.insert("kiwi", 50)
HT.insert("melon", 100)
HT.insert("watermelon", 100)
HT.display()
HT.remove("kiwi")
print("\n")
HT.display()
print(HT.get("watermelon"))