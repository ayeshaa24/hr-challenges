#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            deleted = True
            i = max(i - 1, 0)
            # i = max(i - 2, -1) <- to be used without else stm
            # if deleted, it goes back one
            # e.g. can test for baab, after deleting a
            # it will go back to the first b, checking bb
        else:
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
