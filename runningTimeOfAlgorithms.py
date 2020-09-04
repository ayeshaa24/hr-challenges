#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    cnt = 0
    for i in range(1, len(arr)):
        j = i
        stored = arr[j]
        while j > 0 and arr[j-1] > stored:
            arr[j] = arr[j-1]
            j -= 1
            cnt += 1
        arr[j] = stored
    return(cnt)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
