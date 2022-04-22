from typing import *

"""
preorder DLR [1, 2, 4, 7, 3]
inorder LDR [2, 1, 7, 4, 3]

1
| \
2 4
| \
7 3
"""


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


def __repr__(self):
    return f"D={self.val}, L={self.left.val if self.left else None}, R={self.right.val if self.right else None}"


def reconstruct_binary_tree(
    pre_order: List[int], in_order: List[int]
) -> Optional["TreeNode"]:
    root = None
    if in_order:
        root = TreeNode(pre_order.pop(0))
        root_index = in_order.index(root.val)
        root.left = reconstruct_binary_tree(pre_order, in_order[:root_index])
        root.right = reconstruct_binary_tree(pre_order, in_order[root_index + 1 :])
    return root


def traverse_post_order(root: "TreeNode", values=None) -> List[int]:
    if not values:
        values = []
    if root:
        traverse_post_order(root.left)
        traverse_post_order(root.right)
        values.append(root.val)
    return values


def main():
    pre_order = [1, 2, 4, 7, 3]
    in_order = [2, 1, 7, 4, 3]
    root = reconstruct_binary_tree(pre_order, in_order)
    assert traverse_post_order(root) == [2, 7, 3, 4, 1]


if __name__ == "__main__":
    main()
