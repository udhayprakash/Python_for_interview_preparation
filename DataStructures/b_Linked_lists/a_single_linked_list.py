#!/usr/bin/python
"""
Purpose: Single Linked List
    - A chain of connected nodes
    - single linked list node
        - single entity containing both value and address of next node

----------------------
Value | addrOfNextNode
-----------------------

H
    ----------       ----------        ----------     ----------
    12 | 12323    ==> '34'|13223   ==> 89.9|13234 ==> 'apple'|None
    ----------       ----------        ----------     ----------

"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_value = None

    def __str__(self):
        return f"{self.value} | {self.next_value}"

    __repr__ = __str__


n1 = Node(12)

# print(n1)        # __str__
# print(str(n1))   # __str__
# print(repr(n1))  # __repr__
# print(f'{n1}')   # __str__
# print(f'{n1 =}')  # __repr__


class SingleLinkedList:
    def __init__(self):
        self.head = None  # contains starting node

    def add_node(self, data):
        new_node = Node(data)
        if self.head:
            current_node = self.head
            while current_node.next_value:
                current_node = current_node.next_value
            current_node.next_value = new_node
        else:
            # adding first node
            self.head = new_node

    def __str__(self):
        current_node = self.head
        print(current_node)
        while current_node.next_value:
            current_node = current_node.next_value
            print(current_node)


s = SingleLinkedList()
s.add_node(12)
s.add_node("34")
s.add_node(89.9)
s.add_node("apple")

print(s)
