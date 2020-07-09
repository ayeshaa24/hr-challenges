import timeit
def myTwoStrings(s1, s2):
    for i in set(s1):
        if i in s2:
            return "YES"
    return "NO"

# is meant to be faster but doesn't seem faster...
def theirTwoStrings(s1, s2):
    if set(s1)&set(s2):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    setup = """
from __main__ import myTwoStrings
"""
    test = """
myTwoStrings("qwertyuiopasdfghjklzxcvbnm", "mnbvcxzlkjhgfdsapiuytrewq")
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 3,
                          number = 100000)

    # printing minimum exec. time
    print('Calculation: {}'.format(min(times)))

    setup = """
from __main__ import theirTwoStrings
"""
    test = """
theirTwoStrings("qwertyuiopasdfghjklzxcvbnm", "mnbvcxzlkjhgfdsapiuytrewq")
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 3,
                          number = 100000)

    # printing minimum exec. time
    print('Calculation: {}'.format(min(times)))
