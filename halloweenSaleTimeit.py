import timeit

def howManyGames(p, d, m, s): # winner
    n = 0
    while s - p >= 0 and p > m:
        n += 1
        s -= p
        p -= d
    if p <= m:
        n += s // m
    return(n)


def altHowManyGames(p, d, m, s):
    n = 0
    while s >= p:
        s -= p
        p = max(p - d, m)
        n += 1
    return(n)


if __name__ == '__main__':
    setup = """
from __main__ import howManyGames
""" 
    test = """
howManyGames(20, 3, 6, 85)
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 3,
                          number = 1000000)

    # printing minimum exec. time
    print('My Calculation: {}'.format(min(times)))

    setup = """
from __main__ import altHowManyGames
"""
    test = """
altHowManyGames(20, 3, 6, 85)
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 3,
                          number = 1000000)

    # printing minimum exec. time
    print('Their Calculation: {}'.format(min(times)))
