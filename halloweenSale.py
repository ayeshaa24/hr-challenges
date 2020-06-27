def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    n = 0
    while s - p >= 0 and p > m:
        n += 1
        s -= p
        p -= d
    if p <= m:
        n += s // m
    return(n)


if __name__ == '__main__':
    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    print(answer)
