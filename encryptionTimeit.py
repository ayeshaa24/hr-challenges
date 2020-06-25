import timeit
def f1(): # faster :D
    from math import ceil
    s = "haveaniceday"
    col = ceil(len(s) ** 0.5)
    ans = " ".join([s[i::col] for i in range(col)])
    return(ans)

def f2(): # from editorial
    from math import sqrt, floor, ceil
    s = "haveaniceday"
    n = len(s)
    r = int(floor(sqrt(n)))
    c = int(ceil(sqrt(n)))
    if r * c < n:
        r += 1

    res = [[0 for _ in range(c)] for __ in range(r)]

    it = 0
    i = 0
    j = 0

    while it < n:
        res[i][j] = s[it]
        it += 1
        j += 1
        if j == c:
            j = 0
            i += 1
    out = ""
    for i in range(c):
        for j in range(r):
            if res[j][i] != 0:
                out += res[j][i]
        out += " "
    return(out)

if __name__ == "__main__":
    setup = """
from __main__ import f1
"""
    test = """
f1()
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 3,
                          number = 1000000)

    # printing minimum exec. time
    print('Time taken: {}'.format(min(times)))

    setup = """
from __main__ import f2
"""
    test = """
f2()
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 3,
                          number = 1000000)

    # printing minimum exec. time
    print('Time taken: {}'.format(min(times)))
