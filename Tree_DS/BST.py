# Binary Search Tree Implementation

class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        self.root = self.insert_recursive(self.root, key)
    
    def insert_recursive(self, root, key):
        if root is None:
            return Node(key)

        if key < root.value:
            root.left = self.insert_recursive(root.left, key)
        elif key > root.value:
            root.right = self.insert_recursive(root.right, key)
        
        return root
    
    def search(self, key):
        return self.search_recursive(self.root, key)

    def search_recursive(self, root, key):
        if root is None or root.value == key:
            return root

        if key < root.value:
            return self.search_recursive(root.left, key)
        return self.search_recursive(root.right, key)

    def remove(self, key):
        self.root = self.remove_recursive(self.root, key)

    def remove_recursive(self, root, key):
        if root is None:
            return root

        if key < root.value:
            root.left = self.remove_recursive(root.left, key)    
        elif key > root.value:
            root.right = self.remove_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            min_right_subtree = self.find_min(root.right) # Find the smallest value in the right subtree
            root.value = min_right_subtree.value  # Duplicate the value 
            root.right = self.remove_recursive(root.right, min_right_subtree.value) # Erase the duplicate
        
        return root

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def inorder_traversal(self):
        result = []
        self.inorder_traversal_recursive(self.root, result)
        return result

    def inorder_traversal_recursive(self, root, result):
        if root:
            self.inorder_traversal_recursive(root.left, result)
            result.append(root.value)
            self.inorder_traversal_recursive(root.right, result)

    def display(self):
        return self.display_recursive(self.root, 0)
    
    def display_recursive(self, root, level):
        if root:
            self.display_recursive(root.left, level + 1)
            print("  " * level + str(root.value))
            self.display_recursive(root.right, level + 1)
        

bst = BinarySearchTree()
keys = [9, 5, 10, 0, 6, 11, -1, 1, 2, 3]

for key in keys:
    bst.insert(key)
a = bst.inorder_traversal()
print(a)
print(bst.display()) 
bst.remove(9)
print(bst.display()) 
   

        

