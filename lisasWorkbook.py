def workbook(n, k, arr):
    count = 0
    page = 1
    for noProblems in arr:
        for problem in range(1, noProblems+1):
            if problem == page:
                count += 1
            if problem%k == 0 or problem == noProblems:
                page += 1
    return count

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    print(result)
