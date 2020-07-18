# TAKEN FROM DISCUSSION
# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
def commonChild(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    # c = [[0]*(l2+1)]*(l1+1) doesnt work even though it generates the same array...

    c = [[0]*(l2+1) for _ in range(l1+1)]

    for i in range(l1):
        for j in range(l2):
            if s1[i] == s2[j]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])

    return c[l1-1][l2-1]

if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    print(result)
