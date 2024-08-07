#!/usr/bin/python
"""
Purpose: linkedList creation

node1 -> node2  -> node3 , ...

each node:
    |data|address of next node

    n1              n2         n3           n4
 10|id(n2)     20|id(n2)    30|id(n4)    40|None
"""


class LinkedList:
    def __init__(self, data, next_node_addr=None):
        self.data = data
        self.next_node_addr = next_node_addr

    def __repr__(self):
        return f"{self.data} | {self.next_node_addr}"

    __str__ = __repr__

    def get_data(self):
        return self.data

    def add_node(self, new_node):
        self.next_node_addr = id(new_node)


n1 = LinkedList(10)
print(f"n1: {n1}")

n2 = LinkedList(20)
print(f"n2: {n2}")

n3 = LinkedList(30)
print(f"n3: {n3}")

n4 = LinkedList(40)
print(f"n4: {n4}")

# print(dir(n4))
n1.add_node(n2)
n2.add_node(n3)
n3.add_node(n4)


print("\n After relating ....")
print(f"n1: {n1}")
print(f"n2: {n2}")
print(f"n3: {n3}")
print(f"n4: {n4}")
