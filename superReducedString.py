#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    deleted = True
    while deleted:
        deleted = False
        i = 0
        while i < len(s)-1:
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                deleted = True
                i -= 1
            i += 1

    if s:
        return s
    else:
        return "Empty String"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
