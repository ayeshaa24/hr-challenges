#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    current = {}
    for i in range(len(cost)):
        # leftover = money-cost[i]
        # if leftover in current.keys():
        #     print(current[leftover], i+1)
        #     break
        # current[cost[i]] = i + 1

        # saves the opposite of the above in the dictionary
        if cost[i] in current:
            print(current[cost[i]], i+1)
            break
        current[money-cost[i]] = i + 1

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
