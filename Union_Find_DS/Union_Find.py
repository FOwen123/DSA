# Union Find Implementation through Array

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, element):
        # Find the root of the element's subset
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]
    
    def union(self, element1, element2):
        # Attach the smaller rank tree to the larger rank tree
        root1 = self.find(element1)
        root2 = self.find(element2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root2] < self.rank[root1]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

    def union_multiple(self, list):
        # Merge multiple elements into a single subset
        if len(list) <= 1:
            return
        
        for i in range(len(list)):
            if i < len(list) - 1:
                self.union(self.find(list[i]), self.find(list[i+1]))

    def are_connected(self, element1, element2):
        # Check if element1 and element2 are in the same subset
        return self.find(element1) == self.find(element2)

    def display(self):
        subsets = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in subsets:
                subsets[root] = []
            subsets[root].append(i)
        
        print("Subsets: ")
        for root, elements in subsets.items():
            print(f"Subset {root}: {elements}")

uf = UnionFind(10)
uf.display()
uf.union(1, 2)
uf.union(3, 4)
list = [5, 6, 7]
uf.union_multiple(list)
uf.union_multiple([5, 3, 1])
uf.display()
    

        