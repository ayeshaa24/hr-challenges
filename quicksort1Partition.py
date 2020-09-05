#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    # p = arr[0]
    # left = []
    # equal = []
    # right = []
    # for i in arr:
    #     if i < p:
    #         left.append(i)
    #     elif i > p:
    #         right.append(i)
    #     else:
    #         equal.append(i)

    # return (left + equal + right)
    # ^ takes up three extra arrays

    # since the pivot is the first element
    # all elements greater than are already on the right side of the element, and therefore do not need to be moved
    # all elements less than, need to be moved to the left side of the element
    # this would lead to an incorrect solution if the pivot showed up again, but the question states that all numbers are unique
    p = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < p:
            for j in range(i, 0, -1):
                arr[j], arr[j-1] = arr[j-1], arr[j]
                # shuffles to the beginning, instead of del and insert, should be quicker(?)

    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
