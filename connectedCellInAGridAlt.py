#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the connectedCell function below.
def connectedCell(matrix):
    max_region = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                max_region = max(max_region, dfs(matrix, i, j))

    return max_region

def dfs(matrix, i, j):
    # bounds check
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return 0

    # checks if its a one
    if matrix[i][j] != 1:
        return 0

    region = 1
    matrix[i][j] = -1

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]

    for di, dj in directions:
        region += dfs(matrix, di+i, dj+j)

    return region



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
