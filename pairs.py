#!/bin/python3
import timeit
import math
import os
import random
import re
import sys


# Complete the pairs function below.
def pairs(k, arr):
    from collections import Counter
    c = Counter(arr)
    ans = 0

    # note: arr has unique items only
    for i in arr:
        ans += c[i+k]
    return ans

def altPairs(k, arr): # faster
    a = set(arr)
    # make a set of all a[i] + k
    b = set(x + k for x in arr)
    # return the length of the intersection set
    return len(a&b)


if __name__ == '__main__':
    setup = """
from __main__ import pairs
"""
    test = """
pairs(2, [1, 5, 3, 4, 2])
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 3,
                          number = 100000)

    # printing minimum exec. time
    print('Calculation: {}'.format(min(times)))

    setup = """
from __main__ import altPairs
"""
    test = """
altPairs(2, [1, 5, 3, 4, 2])
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 3,
                          number = 100000)

    # printing minimum exec. time
    print('Calculation: {}'.format(min(times)))
