#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    c = 0
    for i in range(len(q)-1, -1, -1):
        if q[i] != i + 1:
            if q[i-1] == i + 1:
                c += 1

                # temp = q[i-1]
                # q[i-1] = q[i]
                # q[i] = temp

                #q[i], q[i-1] = q[i-1], q[i]

                q[i-1] = q[i]
                # we don't really need to update the current value as we don't check it again...
            elif q[i-2] == i + 1:
                c += 2

                # temp = q[i-2]
                # q[i-2] = q[i-1]
                # q[i-1] = q[i]
                # q[i] = temp

                # q[i-2], q[i-1], q[i] = q[i-1], q[i], q[i-2]

                q[i-2], q[i-1] = q[i-1], q[i]
                # no need to update q[i]
            else:
                return "Too chaotic"
    return c

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        ans = minimumBribes(q)

        print(ans)
