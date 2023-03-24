#!/usr/bin/python
"""
Purpose: Implementing Linked List
"""


class Node:
    def __init__(self, data, _next=None) -> None:
        self.data = data
        self.next = _next

    def __str__(self) -> None:
        return f"[data:{self.data} next:{self.next}]"

    __repr__ = __str__


class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print(self):
        # print(self.head)
        values = []
        curr_node = self.head
        while curr_node:
            values.append(curr_node.data)
            curr_node = curr_node.next
        print(values)

    def reverse(self):
        values = []
        curr_node = self.head
        while curr_node:
            values.insert(0, curr_node.data)
            curr_node = curr_node.next
        print(values)

    def delete_node(self, expected_data):
        if self.head is None:
            return
        prev_node, curr_node = None, self.head
        while curr_node:
            if curr_node.data == expected_data:
                print(prev_node, "--->", curr_node)
                print(curr_node.data, expected_data, "\n\n")
                if curr_node.next is None:
                    break
                prev_node, curr_node = (
                    curr_node,
                    curr_node.next.next,
                )  # TODO - if last node, delete
            prev_node, curr_node = curr_node, curr_node.next

            # curr_node = curr_node.next
            # first, middle , last
            # firt -
            #   if prev_node is None:
            #     prev_node, curr_node = None, self.head.next
            #     continue
            #   prev_node.next = curr_node.next if curr_node.next else None
            #   curr_node = curr_node.next


names = SingleLinkedList()
names.insert_first("Andrew")
names.insert_last("Zoomanzi")
names.insert_last("Yalk")
names.insert_last("Xxx")
names.insert_first("Bob")
names.insert_last("Watson")
names.print()
print("==========================")
names.delete_node("Xxx")
names.delete_node("Andrew")
print("==========================")
names.print()
names.reverse()


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
