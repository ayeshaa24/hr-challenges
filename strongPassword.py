#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    rules = [
        "[a-z]",
        "[A-Z]",
        "[0-9]",
        "[!@#$%^&*()\-+]"
    ]
    # need to escape - to use it literally, hence \-

    ans = 0
    for rule in rules:
        if not re.search(rule, password):
            ans += 1

    return max(6 - n, ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
