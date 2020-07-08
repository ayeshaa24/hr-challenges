from collections import defaultdict

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    c = defaultdict(lambda: 0)
    for i in magazine:
        c[i] += 1
    for i in note:
        c[i] -= 1
        if c[i] < 0:
            return("No")
    return("Yes")


# The Python defaultdict type behaves almost exactly like a regular Python
# dictionary, but if you try to access or modify a missing key, then
# defaultdict will automatically create the key and generate a default value
# for it. This makes defaultdict a valuable option for handling missing keys
# in dictionaries.

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    ans = checkMagazine(magazine, note)

    print(ans)
