from collections import defaultdict

def makeAnagram(a, b):
    ac = defaultdict(int)
    bc = defaultdict(int)
    for i in a:
        ac[i] += 1
    for i in b:
        bc[i] += 1
    ans = 0

    for i in (ac.keys() | bc.keys()):
        ans += abs(ac[i]-bc[i])

    return ans

if __name__ == '__main__':
    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(res)
