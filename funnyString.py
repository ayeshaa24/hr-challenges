#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the funnyString function below.

# (funny => list is symmetrical)
def funnyString(s):
    # n = len(s)
    # for i in range(n-1):
    #     if abs(ord(s[i])-ord(s[i+1])) != abs(ord(s[n-1-i])-ord(s[n-2-i])):
    #         return "Not Funny"
    # return "Funny"

    # can just check if list is symmetrical
    l = [abs(ord(s[i])-ord(s[i+1])) for i in range(len(s)-1)]
    return "Funny" if l == l[::-1] else "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
