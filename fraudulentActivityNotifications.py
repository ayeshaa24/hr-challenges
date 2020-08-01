#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    n = 0

    # current set being looked at
    current = expenditure[:d]

    # initial sort
    current.sort()

    # initial check
    # (e.g. if d = 5, initial check is on 6th day )
    if d % 2 == 0:
        median = (expenditure[d//2]+expenditure[(d//2)-1]) / 2
        if expenditure[d] >= median*2:
            n += 1
    else:
        if expenditure[d] >= current[d//2]*2:
            n += 1
    # note day '5' is with 0 index (technically its 6th day)

    # starts on d+1, as dth day has already been checked
    for i in range(d+1, len(expenditure)):
        # i is the current day
        # so exp[i] is the current transaction

        current.remove(expenditure[i-(d+1)])
        # have to remove d+1 days ago

        new = expenditure[i-1]
        # have to add yesterday's, not today's

        # PUTTING NEW IN CORRECT PLACE
        # too slow to sort each time
        # e.g. current.append(new), current.sort()


        # linear insertion
        # still too slow
        # for j in range(d-1):
        #     if current[j] > new:
        #         current.insert(j, new)
        #         break
        #     if j == d-2:
        #         current.append(new)

        # https://www.geeksforgeeks.org/binary-insertion-sort/
        start = 0
        end = d - 2
        while (True):
        # we need to distinugish whether we should insert
        # before or after the left boundary.
        # imagine [0] is the last step of the binary search
        # and we need to decide where to insert -1
            if start == end:
                if expenditure[start] > new:
                    current.insert(start, new)
                    break
                    #return start # e.g. if in middle of two
                else:
                    current.insert(start + 1, new)
                    break
                    #return start+1 # e.g. if at the end...??

            # this occurs if we are moving beyond left's boundary
            # meaning the left boundary is the least position to
            # find a number greater than new
            if start > end:
                current.insert(start, new)
                break
                #return start

            middle = (start+end)//2

            if expenditure[middle] < new:
                start = middle + 1
            elif expenditure[middle] > new:
                end = middle - 1
            else:
                current.insert(middle, new)
                break
                #return middle

        if d % 2 == 0:
            median = (expenditure[d//2]+expenditure[(d//2)-1]) / 2
            if expenditure[i] >= median*2:
                n += 1
        else:
            if expenditure[i] >= current[d//2]*2:
                n += 1

    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
