# Fenwick Tree
class FenwickTree:
    def __init__(self, size_or_array):
        if isinstance(size_or_array, int):
            self.size = size_or_array
            self.tree = [0] * (self.size + 1)
        if isinstance(size_or_array, list):
            self.size = len(size_or_array)
            self.tree = [0] * (self.size + 1)
            for i in range(self.size):
                self.update(i + 1, size_or_array[i]) # We plus it by one because fenwick tree is a one based array

    def update(self, index, value):
        while index < self.size:
            self.tree[index] += value
            index += index & -index # The & operator return the LSB
        
    def prefixSum(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

    def rangeQueries(self, i, j):
        if i > j:
            return 0
        return self.prefixSum(j) - self.prefixSum(i-1)

    def display(self):
        return self.tree
        
elements = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
n = len(elements)
FT = FenwickTree(elements)
print(FT.prefixSum(3))
print(FT.prefixSum(4))
print(FT.rangeQueries(3, 4))
print(FT.display())
