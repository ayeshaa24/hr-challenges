#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    # logic: find what number should be at position i, and put it there
    s = sorted(arr)
    c = 0
    should_be_at = {}
    for i in range(len(arr)):
        should_be_at[arr[i]] = i


    for i in range(len(arr)):
        actual = arr[i]
        should_be = s[i]

        if actual != should_be:
            arr[i], arr[should_be_at[should_be]] = should_be, actual
            # arr[i] = should_be
            # arr[should_be_at[should_be]] = actual
            # swaps values, using lookup table

            should_be_at[actual] = should_be_at[should_be]
            # updates value of the item that was swapped, but not necessarily put in its correct position

            #should_be_at[should_be] = actual <- don't need to update value that was put its correct place

            c += 1
            # increments swaps counter
    return c



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
