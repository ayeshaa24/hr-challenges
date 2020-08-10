#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    left = "{(["
    right = "})]"
    brackets = { r:l for l, r in zip(left, right) }
    for i in s:
        if i in left:
            stack.append(i)
        elif i in right: # in case there was text...
            if not stack or stack.pop() != brackets[i]:
                return "NO"
            # try:
            #     last = stack.pop()
            # except:
            #     return "NO"
            # if (i == "}" and last != "{") or (i == "]" and last != "[") or (i == ")" and last != "("):
            #     return "NO"

    return "NO" if stack else "YES"
    # if len(stack) == 0:
    #     return "YES"
    # else:
    #     return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
