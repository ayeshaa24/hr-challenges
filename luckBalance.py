def luckBalance(k, contests):
    luck = 0
    contests.sort(reverse=True) # sorts by first value automatically
    for l, t in contests:
        if not t:
            luck += l
        elif k:
            luck += l
            k -= 1
        else:
            luck -= l
    return luck


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(result)
