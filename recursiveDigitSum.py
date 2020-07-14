def superDigit(n, k):
    # if len(n) == 1:
    #     return int(n)
    # else:
    #     n = str(sum(map(int, n*k)))
    #     return superDigit(n, 1)
    # causes memory errors...

    n = str(sum(map(int, n)))
    print(n, n*k)
    # note: n*k != n initially, but is later nk = n
    if len(n*k) == 1:
        return int(n*k)
    else:
        return superDigit(n*k, 1)


if __name__ == '__main__':
    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    print(result)
