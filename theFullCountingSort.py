#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    m = int(max(arr, key=lambda x: x[0])[0]) + 1
    counter = [[] for i in range(m)]
    n = len(arr)
    for i in range(n):
        if i < n//2:
            counter[int(arr[i][0])].append("-")
        else:
            counter[int(arr[i][0])].append(arr[i][1])

    print(" ".join([word for sublist in counter for word in sublist]))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
