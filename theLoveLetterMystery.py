#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    n = len(s)
    cnt = 0
    for i in range(n//2):
        # if s[i] == s[n-i-1]:
        #     continue
        # ^ not necessary, can just add 0
        cnt += abs(ord(s[i]) - ord(s[n-i-1]))

    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
