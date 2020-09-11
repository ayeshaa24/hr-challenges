#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    # ans = 0
    # for i in range(len(s) // 3):
    #     ans += sum(a != b for a, b in zip(s[i*3:i*3+3], "SOS"))

    # return ans

    return sum(s[i] != "SOS"[i%3] for i in range(len(s)))
    # one liner with no ans var

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
