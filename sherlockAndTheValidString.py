from collections import Counter
def isValid(s):
    c = Counter(s)
    if len(set(c.values())) == 1:
        return "YES"
        # e.g. one frequency, abc aabbcc aa
    elif len(set(c.values())) > 2:
        return "NO"
        # e.g. too many frequencies, abbccc
    else:
        mi = min(c.values())
        ma = max(c.values())
        if list(c.values()).count(mi) == 1:
            return "YES"
            # e.g. one character of frequency=1, aabbc
        if mi + 1 == ma and list(c.values()).count(ma) == 1:
            return "YES"
            # e.g. aaabbbcccc but NOT aaabbbcc
            # can only delete one, not add one
        return "NO"


if __name__ == '__main__':
    s = input()

    result = isValid(s)

    print(result)
