def happyLadybugs(b):
    b = list(b)
    s = set(b)

    if not "_" in b:
        if len(b) == 1:
            return("NO")
        if len(s) == 1:
            return("YES")
        # e.g. AAAAA

        letter = ""
        count = 0
        for i in b:
            if i != letter:
                if count == 1:
                    return("NO")
                    # e.g. ACABB
                letter = i
                count = 1
            else:
                count += 1
        if count == 1:
            return("NO")
            # e.g. AABBC
        else:
            return("YES")
            # e.g. AABBB

    for i in s:
        if i == "_":
            continue
        if b.count(i) == 1:
            return "NO"
    return "YES"

if __name__ == '__main__':
    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        print(result)
