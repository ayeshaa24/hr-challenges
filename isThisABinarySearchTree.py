""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
import sys
# recursive iot
def iot(node, arr):
    if not node:
        return
    iot(node.left, arr)
    arr.append(node.data)
    iot(node.right, arr)

# iterative iot
def iiot(node, arr):
    stack = []
    while not len(stack) == 0 or node: # while stack is full or node exists
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            arr.append(node.data)
            node = node.right

def check(root, mini, maxi):
    if not root:
        # if leaf
        return True
    if root.data <= mini or root.data >= maxi:
        # if node is not within the given ranges
        return False
    # if not root.left and not root.right: <- doesnt work if not a perfect tree
    #     return True
    return check(root.left, mini, root.data) and check(root.right, root.data, maxi)

def checkBST(root):
    # 1) editorial method, checking each value against current min and max
    return check(root, -sys.maxsize-1, sys.maxsize)

    # 2) in order traversal: (less efficient)
    a = []
    iiot(root, a)
    return (a == sorted(set(a)))
    # has to be set, to check if all values were unique
    # e.g. [1, 2, 3, 4, 4] would be wrong, but sorted() would not identify the issue
