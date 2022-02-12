from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
    
class Binary_tree:
    def __init__(self) -> None:
        self.root = None
        self.queue = deque()
        
    def create_root_node(self, data):
        node = Node(data)
        self.root = node
      
    def create_other_node(self):
        self.queue.append(self.root)
        while len(self.queue):
            temp = self.queue.popleft()
            val = int(input('Enter left child of {}: '.format(temp.data)))
            if val != -1:
                node = Node(val)
                temp.left = node
                self.queue.append(node)
            val = int(input('Enter right child of {}: '.format(temp.data)))
            if val != -1:
                node = Node(val)
                temp.right = node
                self.queue.append(node)
    
    def preorder_traversal_recursive(self, root):
        if root:
            print(root.data)
            self.preorder_traversal_recursive(root.left)
            self.preorder_traversal_recursive(root.right)
            
    def preorder_traversal_iterative(self, root):
        a_queue = deque()
        temp = root
        elements = []
        while len(a_queue) or temp:
            if temp:
                elements.append(temp.data)
                a_queue.append(temp)
                temp = temp.left
            else:
                temp = a_queue.pop()
                temp = temp.right                
        print(elements)
        
    def inorder_traversal_recursive(self, root):
        if root:
            self.inorder_traversal_recursive(root.left)
            print(root.data)
            self.inorder_traversal_recursive(root.right)
         
    def inorder_traversal_iterative(self, root):
        a_queue = deque()
        elements = []
        while len(a_queue) or root:
            if root:
                a_queue.append(root)
                root = root.left
            else:
                root = a_queue.pop()
                elements.append(root.data)
                root = root.right
        print(elements)
        
    def counting_nodes(self, root):
        if not root:
            return 0
        else:
            x = self.counting_nodes(root.left)
            y = self.counting_nodes(root.right)
            return x + y + 1
            
    def counting_leaf_nodes(self, root):
        if not root:
            return 0
        else:
            x = self.counting_leaf_nodes(root.left)
            y = self.counting_leaf_nodes(root.right)
            if not(root.left or root.right):
                return x + y + 1
            else:
                return x + y   
            
    def height(self, root):
        if not root:
            return 0
        else:
            x = self.height(root.left)
            y = self.height(root.right)
            if x > y:
                return x + 1
            else:
                return y + 1
            
    def counting_non_leaf_nodes(self, root):
        if not root:
            return 0
        else:
            x = self.counting_leaf_nodes(root.left)
            y = self.counting_leaf_nodes(root.right)
            if root.left or root.right:
                return x + y + 1
            else:
                return x + y
            
            
           
binary_tree = Binary_tree()
binary_tree.create_root_node(10)
binary_tree.create_other_node()
binary_tree.preorder_traversal_recursive(binary_tree.root)
print('=' * 30)
binary_tree.preorder_traversal_iterative(binary_tree.root)
print('=' * 30)
binary_tree.inorder_traversal_recursive(binary_tree.root)
print('=' * 30)
binary_tree.inorder_traversal_iterative(binary_tree.root)
print(binary_tree.counting_nodes(binary_tree.root))
print(binary_tree.counting_leaf_nodes(binary_tree.root))
height = binary_tree.height(binary_tree.root)
print('Height of a tree is : {}'.format(height))
