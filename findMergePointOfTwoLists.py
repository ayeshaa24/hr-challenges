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

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def returnLength(l):
    count = 0
    while l:
        count += 1
        l = l.next
    return count


def find_merge_node_using_length(head1, head2):
    # o(n)
    # calculates the length of each
    # shifts the longer list until it is the same length as the shorter one
    # then goes through each list until the merge is found
    # longer list = a + b + x <- gets to the point of b + x
    # shorter list = b + x
    l1 = returnLength(head1)
    l2 = returnLength(head2)
    if l1 < l2:
        short = head1
        longer = head2
    else:
        short = head2
        longer = head1

    for i in range(abs(l1-l2)):
        longer = longer.next

    while short != longer:
        short = short.next
        longer = longer.next

    return short.data

# o(n^2) -_-
def find_merge_node_mine_but_two_loops(head1, head2):
    one_pointer = head1

    while one_pointer:
        two_pointer = head2
        while two_pointer:
            if one_pointer is two_pointer:
                return one_pointer.data
            two_pointer = two_pointer.next
        one_pointer = one_pointer.next


# o(n) solution but destroys one list
def find_merge_node_destructive(head1, head2):
    while head1:
        temp = head1
        head1 = head1.next
        temp.next = None

    while head2.next:
        head2 = head2.next

    return head2.data


# o(n) solution, works but confusing
def find_merge_node_confusing(head1, head2):
    # works with two passes
    # if short = bx and long = abx
    # abxbx
    # bxabx
    # when x is reached at the same time, the merge is returned

    one_pointer = head1
    two_pointer = head2
    while one_pointer != two_pointer:
        if not one_pointer.next:
            one_pointer = head2
        else:
            one_pointer = one_pointer.next

        if not two_pointer.next:
            two_pointer = head1
        else:
            two_pointer = two_pointer.next

    return one_pointer.data


if __name__ == '__main__':
