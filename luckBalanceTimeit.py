import timeit
def luckBalance(k, contests):
    luck = 0
    important = []
    for c in contests:
        if c[1] == 0:
            luck += c[0]
        else:
            important.append(c[0])
    important.sort(reverse=True)
    luck = luck + sum(important[:k]) - sum(important[k:])
    return luck

def altLuckBalance(k, contests): #slightly faster
    luck = 0
    contests.sort(reverse=True) # sorts by first value automatically
    for l, t in contests:
        if not t:
            luck += l
        elif k:
            luck += l
            k -= 1
        else:
            luck -= l
    return luck

if __name__ == '__main__':
    setup = """
from __main__ import luckBalance
"""
    test = """
luckBalance(5, [[13, 1], [10, 1], [9, 1], [8, 1], [13, 1], [12, 1], [18, 1], [13, 1]])
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 3,
                          number = 100000)

    # printing minimum exec. time
    print('Calculation: {}'.format(min(times)))

    setup = """
from __main__ import altLuckBalance
"""
    test = """
altLuckBalance(5, [[13, 1], [10, 1], [9, 1], [8, 1], [13, 1], [12, 1], [18, 1], [13, 1]])
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 3,
                          number = 100000)

    print('Calculation: {}'.format(min(times)))
    # nk = input().split()
    #
    # n = int(nk[0])
    #
    # k = int(nk[1])
    #
    # contests = []
    #
    # for _ in range(n):
    #     contests.append(list(map(int, input().rstrip().split())))
    #
    # result = luckBalance(k, contests)
    #
    # print(result)
