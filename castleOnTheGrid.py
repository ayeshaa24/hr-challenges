#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumMoves function below.

class Node:
    def __init__(self, dis, r, c):
        self.row = r
        self.col = c
        self.distance = dis

    def __repr__(self):
        return("{}".format(self.distance))

def minimumMoves(grid, startX, startY, goalX, goalY):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    need_to_visit = [Node(0, startX, startY)]

    lookup = {}
    lookup[(startX, startY)] = need_to_visit[0]

    while need_to_visit:
        current = need_to_visit.pop(0)

        for d0, d1 in directions:
            temp = (d0 + current.row, d1 + current.col)
            new = False

            while  0 <= temp[0] < len(grid) and 0 <= temp[1] < len(grid[0]) and grid[temp[0]][temp[1]] != "X":
                if temp in lookup and not lookup[temp].distance > current.distance:
                    break
                # if theres a shorter route to a node that has already been found, it is remade

                new = Node(current.distance+1, temp[0], temp[1])
                lookup[temp] = new
                temp = (temp[0]+d0, temp[1]+d1)

                need_to_visit.append(new)

    return lookup[(goalX, goalY)].distance



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
