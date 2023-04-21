"""
Pattenr: Chain of Responsibility

Example:
    we have a system that processes incoming customer support tickets,
    and we want to implement a chain of handlers to handle different
    types of tickets based on their priority.
"""


class SupportTicket:
    """
    Class representing a support ticket.
    """

    def __init__(self, priority):
        self._priority = priority

    def get_priority(self):
        """
        Get the priority of the support ticket.
        """
        return self._priority


class Handler:
    """
    Abstract base class for handlers in the chain.
    """

    def __init__(self, successor=None):
        self._successor = successor

    def handle_ticket(self, ticket):
        """
        Handle a support ticket. If the handler can handle the ticket, it does so.
        Otherwise, it passes the ticket to the next handler in the chain.
        """
        if self._successor is not None:
            return self._successor.handle_ticket(ticket)

    def set_successor(self, successor):
        """
        Set the successor handler in the chain.
        """
        self._successor = successor


class Level1SupportHandler(Handler):
    """
    Concrete handler for level 1 support tickets.
    """

    def handle_ticket(self, ticket):
        if ticket.get_priority() == "low":
            print("Level 1 support handles a low-priority ticket.")
        else:
            super().handle_ticket(ticket)


class Level2SupportHandler(Handler):
    """
    Concrete handler for level 2 support tickets.
    """

    def handle_ticket(self, ticket):
        if ticket.get_priority() == "medium":
            print("Level 2 support handles a medium-priority ticket.")
        else:
            super().handle_ticket(ticket)


class Level3SupportHandler(Handler):
    """
    Concrete handler for level 3 support tickets.
    """

    def handle_ticket(self, ticket):
        if ticket.get_priority() == "high":
            print("Level 3 support handles a high-priority ticket.")
        else:
            super().handle_ticket(ticket)


# Client code
if __name__ == "__main__":
    # Create the chain of support handlers
    level1_handler = Level1SupportHandler()
    level2_handler = Level2SupportHandler()
    level3_handler = Level3SupportHandler()

    level1_handler.set_successor(level2_handler)
    level2_handler.set_successor(level3_handler)

    # Send support tickets to the chain
    ticket1 = SupportTicket("low")
    ticket2 = SupportTicket("medium")
    ticket3 = SupportTicket("high")

    level1_handler.handle_ticket(
        ticket1
    )  # Level 1 support handles a low-priority ticket.
    level1_handler.handle_ticket(
        ticket2
    )  # Level 2 support handles a medium-priority ticket.
    level1_handler.handle_ticket(
        ticket3
    )  # Level 3 support handles a high-priority ticket.

"""
Explanation:
    In this example, we have implemented a chain of support handlers
    (Level1SupportHandler, Level2SupportHandler, and Level3SupportHandler)
    that handle support tickets of different priorities.

    Each handler in the chain has a reference to its successor handler,
    and it can choose to handle a support ticket or pass it to the next
    handler in the chain based on the priority of the ticket.

    The client code creates the chain of handlers and sends support tickets
    to the chain, which is then processed by the appropriate handler in
    the chain based on the priority of the ticket.

    If no handler can handle the ticket, it is not handled by any handler
    in the chain.
"""
