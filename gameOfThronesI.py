#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    no_pair = set()
    for i in s:
        if i in no_pair:
            no_pair.remove(i)
        else:
            no_pair.add(i)
    return "YES" if 0 <= len(no_pair) <= 1else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
