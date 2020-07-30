def getMinimumCost(k, c):
    c.sort(reverse=True)
    return sum(c[i] * ((i//k)+1) for i in range(len(c)))


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    print(minimumCost)
