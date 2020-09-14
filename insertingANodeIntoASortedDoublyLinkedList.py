#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    new = DoublyLinkedListNode(data)

    if not head:
        return new

    current = head

    while current.next and data > current.next.data:
        current = current.next
    # current is the node before where the new node should be inserted
    # (unless current == head in which case, the new node *could* be inserted before)

    if current is head and data <= current.data:
        new.next = current
        current.prev = new
        return new

    new.prev = current
    new.next = current.next
    current.next = new
    return head


if __name__ == '__main__':
