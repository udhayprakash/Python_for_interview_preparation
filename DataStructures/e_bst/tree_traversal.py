# Python3 program to construct tree using inorder
# and postorder traversals


# A binary tree node has data, pointer to left
# child and a pointer to right child
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


# Recursive function to construct binary of size n
# from Inorder traversal in[] and Postorder traversal
# post[]. Initial values of inStrt and inEnd should
# be 0 and n -1. The function doesn't do any error
# checking for cases where inorder and postorder
# do not form a tree


def buildUtil(inn, post, innStrt, innEnd):
    global mp, index

    # Base case
    if innStrt > innEnd:
        return None

    # Pick current node from Postorder traversal
    # using postIndex and decrement postIndex
    curr = post[index]
    node = Node(curr)
    index -= 1

    # If this node has no children then return
    if innStrt == innEnd:
        return node

    # Else find the index of this node inn
    # Inorder traversal
    iIndex = mp[curr]

    # Using index inn Inorder traversal,
    # construct left and right subtress
    node.right = buildUtil(inn, post, iIndex + 1, innEnd)
    node.left = buildUtil(inn, post, innStrt, iIndex - 1)

    return node


# This function mainly creates an unordered_map,
# then calls buildTreeUtil()


def buildTree(inn, post, lenn):
    global index

    # Store indexes of all items so that we
    # we can quickly find later
    for i in range(lenn):
        mp[inn[i]] = i

    # Index in postorder
    index = lenn - 1
    return buildUtil(inn, post, 0, lenn - 1)


# This function is here just to test


def preOrder(node):
    if node == None:
        return

    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)


# Driver Code
if __name__ == "__main__":
    inn = [4, 8, 2, 5, 1, 6, 3, 7]
    post = [8, 4, 5, 2, 6, 7, 3, 1]
    n = len(inn)
    mp, index = {}, 0

    root = buildTree(inn, post, n)

    print("Preorder of the constructed tree :")
    preOrder(root)
