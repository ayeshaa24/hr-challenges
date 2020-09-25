#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    _, swaps = mergesort(arr)
    return swaps


def mergesort(arr):
    n = len(arr)

    if n <= 1:
        return arr, 0
    # basecase


    left = arr[:n//2]
    right = arr[n//2:]

    left, left_swaps = mergesort(left)
    right, right_swaps = mergesort(right)
    result, merge_swaps = mergehalves(left, right)

    return result, left_swaps + right_swaps + merge_swaps

def mergehalves(left, right):
    swaps = 0
    result = []

    left_index = 0
    left_len = len(left)
    right_index = 0
    right_len = len(right)
    # ^ better than recalculating length each time, times out otherwise


    while left_index < left_len and right_index < right_len:
        if left[left_index] <= right[right_index]:
            # result.append(left.pop(0))
            # ^ times out

            result.append(left[left_index])
            left_index += 1
        else:
            # num += len(left[left_index:]) # shifts left left_len times
            # ^ times out!!
            swaps += left_len - left_index
            # adds on the number of shifts left it has to take

            result.append(right[right_index])
            right_index += 1


    result += left[left_index:] + right[right_index:]

    return result, swaps



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
