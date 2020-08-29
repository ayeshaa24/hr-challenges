#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    # stored = arr[-1]
    # i = len(arr) - 2
    # while i >= 0 and arr[i] > stored:
    #     arr[i+1] = arr[i]
    #     print(*arr)
    #     i -= 1

    # if i == -1:
    #     arr[0] = stored
    # else:
    #     stored, arr[i+1] = arr[i], stored
    # print(*arr)
    # ^ inefficient as we compare to before instead of ahead so it requires another if else statement

    stored = arr[-1]
    i = len(arr) - 1

    while i > 0 and arr[i-1] > stored:
        arr[i]= arr[i-1]
        print(*arr)
        i -= 1

    arr[i] = stored
    print(*arr)



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
