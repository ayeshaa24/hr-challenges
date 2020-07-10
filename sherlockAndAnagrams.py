# 1 => 0
# 2 => 1
# 3 => 3
# 4 => 6
# sort of triangle numbers but one off
# N * (N-1)/2 !!!!!!!

from collections import defaultdict
def sherlockAndAnagrams(s):
    c = defaultdict(int)
    # used default dict, to avoid missing keys issue

    # generates all possible substrings and counts them
    # saved as sorted tuple keys, so anagrams are counted
    for o in range(len(s)):
        i = 1
        while i + o <= len(s):
            value = tuple(sorted(s[o: o+i]))
            c[value] += 1
            i += 1
    # (tuple = list can't be dictionary keys
    # tuple can as they are immutable and therefore hashable)
    # (sorted = anagrams are the same when sorted)


    # counts how many pairs for each anagram tuple counted
    ans = 0
    for i in c.keys():
        ans += c[i] * ((c[i]-1)/2)

    return int(ans)


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)
