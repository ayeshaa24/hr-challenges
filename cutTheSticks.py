import timeit

def v1():
    arr = [int(i) for i in "1 2 3 4 3 3 2 1".strip().split(' ')]
    s = sorted(set(arr), reverse=True)
    noLeft = len(arr)
    ans = []
    while noLeft > 0:
        ans.append(noLeft)
        noLeft -= arr.count(s.pop())
    return ans

def v2(): # winner
    arr = [int(i) for i in "1 2 3 4 3 3 2 1".strip().split(' ')]
    arr = sorted(arr)
    ans = []
    while len(arr) > 0:
        ans.append(len(arr))
        arr = arr[arr.count(arr[0]):]
    return ans

setup = """
from __main__ import v1
"""
test1_code = """
v1()
"""

times = timeit.repeat(
    setup = setup,
    stmt = test1_code,
    repeat = 3,
    number = 100000
)

print('Binary search time: {}'.format(min(times)))

setup = """
from __main__ import v2
"""
test2_code = """
v2()
"""

times = timeit.repeat(
    setup = setup,
    stmt = test2_code,
    repeat = 3,
    number = 100000
)

print('Binary search time: {}'.format(min(times)))
