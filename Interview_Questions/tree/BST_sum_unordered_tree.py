class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None


def get_leaves(node, leaves=None):
    if not leaves:
        leaves = []
        global summation

    if not node:
        return

    if (not node.left) and (not node.right):
        summation += int("".join([str(dig) for dig in leaves + [node.data]]))
        # print("summation", summation)
        return node.data

    if node.left:
        get_leaves(node.left, leaves + [node.data])

    if node.right:
        get_leaves(node.right, leaves + [node.data])


if __name__ == "__main__":
    root = Node(6)
    root.left = Node(3)
    root.right = Node(5)
    root.left.left = Node(2)
    root.left.right = Node(5)
    root.right.right = Node(4)
    root.left.right.left = Node(7)
    root.left.right.right = Node(4)

    summation = 0
    get_leaves(root)
    print("summation", summation)
