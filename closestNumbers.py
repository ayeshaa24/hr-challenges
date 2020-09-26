#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr = sorted(arr)
    # once sorted, numbers with the smallest difference will be next to each other

    least = sys.maxsize
    result = []

    for i in range(1, len(arr)):
        diff = arr[i]-arr[i-1]
        if diff < least:
            least = diff
            result = [arr[i-1], arr[i]]
        elif diff == least:
            result.extend([arr[i-1], arr[i]])

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
