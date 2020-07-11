from collections import defaultdict
import operator as op
from functools import reduce

# unfinished :(

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

# Complete the countTriplets function below.
def countTriplets(arr, r):
    cnt = defaultdict(int)
    ans = 0
    for i in arr:
        cnt[i] += 1

    trip = set()
    k = cnt.keys()
    hm = 0
    for i in k:
        if r == 1:
            if cnt[i] >= 3:
                ans += ncr(cnt[i], 3)
            continue
        if i*r in cnt and i*r*r in cnt:
            hm += 1
            trip.add((i, i*r, i*r*r))
            print((i, i*r, i*r*r))
            print(cnt[i*r] * cnt[i*r*r] * cnt[i])
            ans += (cnt[i] * cnt[i*r] * cnt[i*r*r])
        # if _ in arr times out...

    # ans = 0
    # cnt = defaultdict(int)
    # trip = defaultdict(int)
    # for i in arr:
    #     cnt[i] += 1
    print(cnt)
    print(trip)
    # print(hm)

    return ans

if __name__ == '__main__':
    file = open("countTriplets.txt", "r")

    nr = file.readline().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, file.readline().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)
    print(ans - 2325652489)
