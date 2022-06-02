#!/usr/bin/python
"""
Purpose: Insert the word 'hello' in single linked list

    h|id(e)     e|id(l)      l|id(l)      l|id(o)    o|None
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


# list_of_nodes = []
# for each_char in 'hello':
#     node = LinkedList(each_char, None)
#     list_of_nodes.append(node)

# print(list_of_nodes)


list_of_nodes = []
word = "hello"
for loop_index, each_char in enumerate(word):
    # current_char = each_char  # word[loop_index]
    # previous_char = word[loop_index - 1]
    # print(loop_index, previous_char, current_char)

    current_node = LinkedList(each_char, None)
    list_of_nodes.append(current_node)

    if loop_index:
        previous_node = list_of_nodes[loop_index - 1]
        previous_node.next_node_addr = id(current_node)
        # print(f'{loop_index =} {previous_node =} {current_node =}')

print(list_of_nodes)
