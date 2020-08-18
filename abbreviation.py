#!/bin/python3

import math
import os
import random
import re
import sys

# def recurse(a, b):
    # if a == b:
    #     return True
    # if b == "" and a.lower() == a:
    #     return True
    # if a == "":
    #     return False
    # if a[-1] == b[-1]:
    #     return recurse("".join(a[:-1]), "".join(b[:-1]))
    # # b.append(cb)
    # if a[-1].upper() == b[-1]:
    #     return recurse("".join(a[:-1]), "".join(b)) or recurse("".join(a), "".join(b[:-1]))
    # if 97 <= ord(a[-1]) <= 122:
    #     return recurse("".join(a[:-1]), "".join(b))
    # return False


def abbreviation(a, b):
    # Recursive method is too slow
    # if recurse(a, b):
    #     return "YES"
    # else:
    #     return "NO"

    # Dynamic programming approach
    dp = [[False for i in range(len(a)+1)] for i in range(len(b)+1)]
    # Initialising using false instead of none

    for row in range(len(dp)):
        if row == 0:
            strB = ""
        else:
            strB = b[row-1]
        for col in range(len(dp[0])):
            if col == 0:
                strA = ""
            else:
                strA = a[col-1]

            # basecase
            if strA == "" and strB == "":
                dp[row][col] = True

            # empty A can never match non empty B
            elif strA == "":
                # dp[row][col] = False
                continue

            # empty b can only match lower case A
            # (have to check left column to see if all true so far)
            elif strB == "" and strA.lower() == strA:
                dp[row][col] = dp[row][col-1]

            # if capitals match, its result depends on the function result of when the character deleted from a and b
            # e.g. f("aB", "fB") => f("a", "f")
            elif strA == strB:
                dp[row][col] = dp[row-1][col-1]

            # if lower a matches, its function results can be one of two routes
            # 1) if accept the lower 2) if we do not accept the lower
            # e.g. f("sa", "sA") => f("s", "s") OR f("s", "sA")
            elif strA.upper() == strB:
                dp[row][col] = dp[row-1][col-1] or dp[row][col-1]

            # if a is lowercase, it's result depends on the function result when it is deleted
            # f("as", "aA") => f("a", "aA")
            elif 97 <= ord(strA) <= 122:
                dp[row][col] = dp[row][col-1]

            # otherwise, a is uppercase and cannot match b
            # else:
            #     dp[row][col] = False

    # the bottom right result tells us the result when both full strings are compared
    if dp[-1][-1]:
        return "YES"
    else:
        return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
