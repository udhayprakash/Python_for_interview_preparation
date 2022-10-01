"""
Python program to create and reverse the singly linked list.

Problem Statement:
    Our program will take the linked list elements from the user as the input and return the reversed linked list.
For example:

Case1:
    If the user input the linked list as 1, 2, 3, 4.
    The output should be “4, 3, 2, 1”.

Case2:
    If the user input the linked list as 7, 9, 1, 0.
    The output should be 0, 1, 9, 7.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    def reverse(self):
        prev_node, curr_node = None, self.head
        while curr_node:
            temp = curr_node.next  # addr
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp
        self.head = prev_node

    # Function to add element at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # to show the elements of the linked list
    def show(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


test_list = ["abcde", "12345", "xxxxhhhh"]
for string in test_list:
    s = SinglyLinkedList()
    for char in string:
        s.push(char)
    print("Given linked list (Original Linked list) : ")
    s.show()
    s.reverse()
    print("\nReversed linked list : ")
    s.show()
    print("\n")
