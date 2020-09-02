#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    outer = 1
    while outer < len(arr):
        inner = outer
        stored = arr[inner]
        while inner > 0 and arr[inner-1] > stored:
            arr[inner] = arr[inner-1]
            inner -=1
        arr[inner] = stored
        outer += 1
        print(*arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
