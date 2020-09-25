#!/bin/python3

import math
import os
import random
import re
import sys

num = 0
# Complete the countInversions function below.
def countInversions(arr):
    global num
    num = 0
    answer = mergesort(arr)
    print(num)
    return num

def mergesort(arr):
    n = len(arr)

    if n <= 1:
        return arr
    # basecase


    left = arr[:n//2]
    right = arr[n//2:]

    left = mergesort(left)
    right = mergesort(right)

    return mergehalves(left, right)

def mergehalves(left, right):
    global num
    result = []

    left_index = 0
    left_len = len(left)
    right_index = 0
    right_len = len(right)

    # ^ better than recalculating length each time, times out otherwise


    while left_index < left_len and right_index < right_len:
        if left[left_index] <= right[right_index]:
            #result.append(left.pop(0))
            result.append(left[left_index])
            left_index += 1
        else:
            #num += len(left[left_index:]) # shifts left left_len times
            # ^ times out!!
            num += left_len - left_index
            #result.append(right.pop(0))
            result.append(right[right_index])
            right_index += 1


    result += left[left_index:] + right[right_index:]

    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
