"""
Purpose: Implement a queue ↴ with 2 stacks.

    Queue should have an enqueue and a dequeue method;
    and it should be "first in first out" (FIFO).

"""


class QueueTwoStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:

            # Move items from in_stack to out_stack, reversing order
            while len(self.in_stack) > 0:
                newest_in_stack_item = self.in_stack.pop()
                self.out_stack.append(newest_in_stack_item)

            # If out_stack is still empty, raise an error
            if len(self.out_stack) == 0:
                raise IndexError("Can't dequeue from empty queue!")

        return self.out_stack.pop()


q2s = QueueTwoStacks()

for num in range(1, 9):
    q2s.enqueue(num**2)

for _ in range(1, 9):
    print("q2s.dequeue()", q2s.dequeue())
