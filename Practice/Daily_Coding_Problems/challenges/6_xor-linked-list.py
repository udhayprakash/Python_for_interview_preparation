"""
#6
Google

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer
and dereference_pointer functions that converts between nodes and memory addresses.

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.both = 0

    def __str__(self):
        return str(self.val)


class XORLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

    def add(self, _element):
        new_node = Node(_element)
        if self.head.val:
            new_node.both = get_pointer(self.tail)
            self.tail.both = self.tail.both ^ get_pointer(new_node)
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    def get(self, _ind):
        previous_addr = 0
        current = self.head
        for i in range(0, _ind - 1):
            temp = get_pointer(current)
            current = dereference_pointer(previous_addr ^ current.both)
            previous_addr = temp
            if curret.both == previous_addr and i < _ind - 2:
                print("Invalid index.")
                return None
        return current


if __name__ == "__main__":
    xorLinkedList = XORLinkedList()

    while True:
        choice = int(input("1. ADD\n2. GET\n3. EXIT").strip())
        if choice == 1:
            element = int(input("Enter the element: ").strip())
            xorLinkedList.add(element)
        elif choice == 2:
            ind = int(input("Enter the index: ").strip())
            node = xorLinkedList.get(ind)
            if node:
                print(node)
        elif choice == 3:
            exit(0)
        else:
            print("Invalid choice.")
