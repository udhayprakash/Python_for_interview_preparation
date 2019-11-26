#!/usr/bin/python
"""
Purpose: Implementing Linked List
"""


class Node:
    def __init__(self, val, _next=None):
        self.data = val
        self.next = _next

    def __str__(self):
        print(f'data:{self.data} next:{self.next}')

    __repr__ = __str__


class SingleLinkedList:
    def __init__(self):
        self.nodes = []

    def insert_tail(self, _val):
        new_node = Node(_val)
        if self.nodes:
            self.nodes[-1].next = id(new_node)
        self.nodes.append(new_node)

    def __str__(self):
        result = ''
        for each_node in self.nodes:
            result += str(each_node) + '\n'
        return result

    __repr__ = __str__

# if __name__ == '__main__':
#     s = SingleLinkedList()
#     choice = input('''
#         Single Linked List Initialized ...
#         Choose an option for the operations:
#             1. Add a node at right end
#             2. Add a node at left end
#             3. Add a node at kth position
#             4. pop a node from right end
#             5. pop a node from left end
#             6. remove a node from kth position
#             7. Get the LinkedList size
#             8. Display LinkedList
#             
#         NOTE: Choosing any other option will terminate the process 
#         ''')
# 
#     if choice == '1':
#         val = input('Enter the value:')
#         s.add_node_right_end(val)
# 
#     print(s)
