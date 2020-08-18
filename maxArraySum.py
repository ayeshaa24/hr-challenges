#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    # ty editorial -_-

    # explanation:
    # each position will hold the current maximum so far (that's possible to be create i.e. not including adjacent numbers)

    # max of arr[0] is just arr[0]
    # max of arr[1] is just the max between arr[0] and arr[1]
    arr[1] = max(arr[0], arr[1])
    max_so_far = arr[1]
    # and therefore the max so far is therefore arr[1]

    # after this, the max at the current position is either
    # 1) the max so far (so the subset doesn't include the current number, e.g. if its a negative number that just reduces the max)
    # 2) the current number (so the subset only contains the current number)
    # 3) the current number + the number two behind (so the subset contains the current number and the number behind (which itself is the sum of the max subset so far))
    # max so far is assigned to the current position, and this continues

    # note: max so far = a[i-1] so...
    for i in range(2, len(arr)):
        # max_so_far = max(max_so_far, arr[i], arr[i]+arr[i-2])
        max_so_far = max(arr[i-1], arr[i], arr[i]+arr[i-2])
        arr[i] = max_so_far
    print(arr)
    return max_so_far



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
