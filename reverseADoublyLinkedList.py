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

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
# alternative method with temp var
# def reverse(head):
#     pointer = head

#     current = head

#     while pointer:
#         current = pointer

#         temp = current.prev

#         current.prev = current.next

#         pointer = current.next

#         current.next = temp


#     return current

def reverse(head):
    while head.next:
        # head.prev, head, head.next = head.next, head.next, head.prev
        # head, head.prev, head.next = head.next, head.next, head.prev
        # ^ don't work...?
        head.prev, head.next, head = head.next, head.prev, head.next

    head.prev, head.next = None, head.prev

    return head

if __name__ == '__main__':
