"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    # uses storage
    gone_to = set()
    while head:
        if head in gone_to:
            return True
        gone_to.add(head)
        head = head.next
    return False

    # takes into account the fact that the max size of constraints is 100
    if not head:
        return False

    for i in range(101):
        head = head.next
        if not head:
            return False
    return True


    # two pointer solution
    # fast pointer always catches up with slow pointer if there is a loop
    if not head:
        return False

    slow = head
    fast = head.next
    while slow != fast:
        if not fast or not fast.next: # <- prevents fast.next.next from throwing an error
            return False
        slow = slow.next
        fast = fast.next.next

    return True
