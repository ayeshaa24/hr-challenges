#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    counter = [0 for i in range(100)]

    for i in arr:
        counter[i] += 1


    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
