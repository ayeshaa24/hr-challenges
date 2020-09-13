import timeit

# Complete the gemstones function below.
def gemstones(arr):
    # seems to be faster tho...
    gemstones = set(arr[0])
    for rock in arr[1:]:
        gemstones = [gem for gem in gemstones if gem in rock]

    return len(gemstones)

def alt_gemstones(arr):
    # SET THEORY!!!
    gemstones = set(arr[0])
    for rock in arr[1:]:
        gemstones = gemstones.intersection(set(rock))

    return(len(gemstones))


if __name__ == '__main__':
    setup = """
from __main__ import gemstones
"""
    test = """
gemstones(["basdfj", "asdlkjfdjsa", "bnafvfnsd", "oafhdlasd"])
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 3,
                          number = 100000)

    # printing minimum exec. time
    print('Calculation: {}'.format(min(times)))

    setup = """
from __main__ import alt_gemstones
"""
    test = """
alt_gemstones(["basdfj", "asdlkjfdjsa", "bnafvfnsd", "oafhdlasd"])
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 3,
                          number = 100000)

    print('Calculation: {}'.format(min(times)))
