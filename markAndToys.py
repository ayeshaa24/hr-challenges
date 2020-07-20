def maximumToys(prices, k):
    # prices = sorted(prices)
    # total = 0
    # c = 0
    # for i in prices:
    #     total += i
    #     if total > k:
    #         break
    #     c += 1
    # return c

    # uses one less variable
    prices.sort()
    c = 0
    for i in prices:
        k -= i
        if k < 0:
            break
        c += 1
    return c

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(result)
