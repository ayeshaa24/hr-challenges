import timeit
def sherlockAndAnagrams(s):  # woo faster :D
    from collections import defaultdict
    c = defaultdict(int)
    for o in range(len(s)):
        i = 1
        while i + o <= len(s):
            value = tuple(sorted(s[o: o+i]))
            c[value] += 1
            i += 1

    ans = 0
    for i in c.keys():
        ans += c[i] * ((c[i]-1)/2)
    return int(ans)

def editorialSherlockAndAnagrams(s):
    import string
    ALPHABET = string.ascii_lowercase
    signatures = {}

    signature = [0 for _ in ALPHABET]
    for letter in s:
        signature[ord(letter)-ord(ALPHABET[0])] += 1

    # iterate over all substrings of s
    for start in range(len(s)):
        for finish in range(start, len(s)):
            # initialize substring signature
            signature = [0 for _ in ALPHABET]
            for letter in s[start:finish+1]:
                signature[ord(letter)-ord(ALPHABET[0])] += 1
            # tuples are hashable in contrast to lists
            signature = tuple(signature)
            signatures[signature] = signatures.get(signature, 0) + 1

    res = 0
    for count in signatures.values():
        res += count*(count-1)/2
    return int(res)

if __name__ == '__main__':
    setup = """
from __main__ import sherlockAndAnagrams
"""
    test = """
sherlockAndAnagrams("abba")
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 3,
                          number = 10000)

    # printing minimum exec. time
    print('Calculation: {}'.format(min(times)))

    setup = """
from __main__ import editorialSherlockAndAnagrams
"""
    test = """
editorialSherlockAndAnagrams("abba")
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 3,
                          number = 10000)

    # printing minimum exec. time
    print('Calculation: {}'.format(min(times)))
