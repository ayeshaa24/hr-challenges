#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    return len(re.findall("[A-Z]", s)) + 1

    #return sum(list(map(lambda c: c.isupper(), s))) + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
