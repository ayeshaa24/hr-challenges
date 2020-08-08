#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    a, b, c = map(lambda l: sorted(set(l)), [a, b, c])

    ac = 0
    bc = 0
    cc = 0

    ans = 0
    while bc < len(b):
        while ac < len(a) and a[ac] <= b[bc]:
            ac += 1

        while cc < len(c) and c[cc] <= b[bc]:
            cc += 1


        ans += ac * cc

        bc += 1

    return ans

    # takes too much time - its just a more complex version of the above
    # a, b, c = map(lambda l: sorted((set(l))), [a, b, c])
    # minA = min(a)
    # minC = min(c)
    # cache = (0, 0)
    # ans = 0
    # for i in b:
    #     if i < minA or i < minC:
    #         continue
    #     countA = 0
    #     countC = 0
    #     for j in range(len(a)-1, -1, -1):
    #         if a[j] <= i:
    #             countA += 1
    #             a.pop(j)
    #     for k in range(len(c)-1, -1, -1):
    #         if c[k] <= i:
    #             countC += 1
    #             c.pop(k)
    #     new = (countA, countC)
    #     cache = tuple(map(lambda n, c: n+c, new, cache))
    #     ans += cache[0] * cache[1]
    # return ans

    # takes up too much storage
    # maxB = max(b)
    # countA = [0 for i in range(maxB)]
    # countC = [0 for i in range(maxB)]
    # a = sorted(set(a))
    # for i in a:
    #     if i > maxB:
    #         break
    #     countA[i-1] += 1

    # # accumulate
    # for i in range(1, maxB):
    #     countA[i] += countA[i-1]

    # c = sorted(set(c))
    # for i in c:
    #     if i > maxB:
    #         break
    #     countC[i-1] += 1

    # # accumulate
    # for i in range(1, maxB):
    #     countC[i] += countC[i-1]

    # ans = 0
    # for i in set(b):
    #     ans += countA[i-1] * countC[i-1]

    # return ans





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
