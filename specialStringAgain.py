
import re

# triangle numbers:
# n * (n+1)/2
# 1 = 1
# 2 = 2*1.5 = 3
# 3 = 3*2 = 6
# 4 = 4*2.4 = 10

def substrCount(n, s):
    ans = 0

    # counting substrings where all characters are the same
    one = re.findall(r'(([a-z])\2*)', s)
    # \1 = whole group matched e.g. aaaa
    # \2 = letter matched e.g. a
    # need outside () so it is returned
    # alt, can use finditer

    ans = sum([len(i) * ((len(i)+1)/2) for i, j in one])
    # use triangle numbers to count all potential combinations within one string

    # counting substrings with the palindrome
    two = re.findall(r'(([a-z])\2*)(?!\1)(?=[a-z]\1)', s)
    # \1 = whole group matched e.g. ooo
    # \2 = letter matched e.g. o
    # two rules follow, a positive look ahead and a negative lookahead
    # 1. can't be followed by \1 e.g. oooooo where \1 is ooo
    # 2. must be followed by a letter and then \1
    # these rules are both applied on everything that follows \1, not applied one after each other

    ans += sum([len(i[0]) for i in two])


    return int(ans)

if __name__ == '__main__':
    n = int(input())

    s = input()

    result = substrCount(n, s)

    print(result)
