# Easier way to implement and visualize binary tree
# Thanks to pypi

from binarytree import Node

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

print(root)
print(root.leaves)
print(root.preorder)
print(root.inorder)
print(root.levelorder)
print(root.postorder)

assert root.height == 2