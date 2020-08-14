#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxRegion function below.
class Cell():
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.adjacent = []


def maxRegion(grid):
    # Creates all ones,
    # saved in a dictionary mapped from coordinate to cell
    # (no need to create a cell for zeroes)
    ones = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                ones[(i, j)] = Cell(grid[i][j])


    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]

    # Fills adjacent with all adjacent one ones
    for k, v in ones.items():
        for x, y in directions:
            try:
                v.adjacent.append(ones[(k[0]+x, k[1]+y)])
            except:
                continue

    ans = 0
    for v in ones.values():
        temp = 0
        if not v.visited:
            temp = dfs(v)

        if temp > ans:
            ans = temp

    return ans

def dfs(current):
    if current.visited:
        return 0

    ans = 1
    current.visited = True

    for i in current.adjacent:
        ans += dfs(i)

    return ans



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
