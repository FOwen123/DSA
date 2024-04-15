# AVL Tree, one of the example of a Balanced Binary Search Tree(BBST)
from collections import deque

class Node():
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree():
    def __init__(self):
        self.root = None
    
    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        # Left is 1, right is -1
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def updateHeight(self, node):
        if not node:
            return
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    def balance(self, root):
        balance = self.getBalance(root)
        
        # Left heavy subtree
        if balance > 1:
            # Left-left subtree
            if self.getBalance(root.left) >= 0:
                return self.rotateRight(root)
            # Left-Right subtree
            else:
                root.left = self.rotateLeft(root.left)
                return self.rotateRight(root)
        
        # Right heavy subtree
        if balance < -1:
            # Right-right subtree
            if self.getBalance(root.right) <= 0:
                return self.rotateLeft(root)
            else:
                root.right = self.rotateRight(root.right)
                return self.rotateLeft(root)
            
        return root


    def rotateRight(self, node):
        newParent = node.left # Make the left child the parent Node
        node.left = newParent.right # Erase the node.left
        newParent.right = node
        self.updateHeight(node)
        self.updateHeight(newParent)

        return newParent

    def rotateLeft(self, node):
        newParent = node.right # Make the left child the parent Node
        node.right = newParent.left # Erase the node.left
        newParent.left = node
        self.updateHeight(node)
        self.updateHeight(newParent)

        return newParent

    def insert(self, key):
        self.root = self.insert_recursive(self.root, key)
    
    def insert_recursive(self, root, key):
        if root is None:
            return Node(key)

        if key < root.value:
            root.left = self.insert_recursive(root.left, key)
        elif key > root.value:
            root.right = self.insert_recursive(root.right, key)
        
        self.updateHeight(root)
        return self.balance(root)

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

            min_right_subtree = self.find_min(root.right)
            root.value = min_right_subtree.value
            root.right = self.remove_recursive(root.right, min_right_subtree.value)

        self.updateHeight(root)
        return self.balance(root)

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def display(self):
        lines, *_ = self._display_aux(self.root) # Unpack the _display_aux function
        for line in lines:
            print(line)
    
    def _display_aux(self, node): # display auxiliary 
        # No child.
        if node.right is None and node.left is None:
            line = f"{node.value}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = f"{node.value}"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = f"{node.value}"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = f"{node.value}"
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

avl = AVLTree()
keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for key in keys:
    avl.insert(key)

avl.display()

