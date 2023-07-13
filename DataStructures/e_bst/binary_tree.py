"""
Binary Tree
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder(self, start, records):
        """Root -> Left subtree -> Right subtree"""
        if start:
            records.append(start.value)
            self.preorder(start.left, records)
            self.preorder(start.right, records)
        return records

    def postorder(self, start, records):
        """Left subtree -> Right subtree -> Root"""
        if start:
            self.postorder(start.left, records)
            self.postorder(start.right, records)
            records.append(start.value)
        return records

    def inorder(self, start, records):
        """Left subtree -> Root -> Right subtree"""
        if start:
            self.inorder(start.left, records)
            records.append(start.value)
            self.inorder(start.right, records)
        return records


tree = BinaryTree(5)
tree.root.left = Node(3)
tree.root.right = Node(7)
tree.root.left.left = Node(2)
tree.root.left.right = Node(4)

#        5
#       /   \
#      3     7
#    /   \
#   2     4


# PreOrder Traversal
print("PreOrder ", tree.preorder(tree.root, []))

# PostOrder Traversal
print("PostOrder", tree.postorder(tree.root, []))


# InOrder Traversal
print("InOrder  ", tree.inorder(tree.root, []))
