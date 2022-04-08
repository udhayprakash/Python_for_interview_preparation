#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


#
# Complete the 'maximumPages' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.
#


def maximumPages(head):
    if head == None:
        return 'list is empty'

    maxpages = 0
    while head:
        firstval = head.data

        # removing head node
        head = head.next
        if not head:
            lastval = 0
            continue
        current = head
        while current != None:
            if current == head:
                previous = current
                lastval = current.data
                current = current.next
        # removing last node

        pagesperday = firstval + lastval
        if pagesperday > maxpages:
            maxpages = pagesperday

    return maxpages


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    head_count = int(input().strip())

    head = SinglyLinkedList()

    for _ in range(head_count):
        head_item = int(input().strip())
        head.insert_node(head_item)

    result = maximumPages(head.head)

    fptr.write(str(result) + '\n')

    fptr.close()
