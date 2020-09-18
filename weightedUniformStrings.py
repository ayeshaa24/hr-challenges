#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.

def weightedUniformStrings(s, queries):
    temp = 0
    possible = {}
    # better to use dict, only O(1) to find existing score

    for i in range(len(s)):
        if s[i] != s[i-1] and i != 0:
            temp = 0
        temp += ord(s[i]) - ord("a") + 1
        possible[temp] = "."

    return ["Yes" if q in possible else "No" for q in queries]


if __name__ == '__main__':
    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    for r in result:
        print(r)
