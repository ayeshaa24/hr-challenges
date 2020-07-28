def minimumAbsoluteDifference(arr):
    m = 10**20
    c = sorted(arr)
    for i in range(len(c)-1):
        m = min(m, abs(c[i]-c[i+1]))

    return m

    # m = 10**20
    # for i in range(len(arr)-1):
    #     for j in range(i+1, len(arr)):
    #         if abs(arr[i]-arr[j]) < m:
    #             m = abs(arr[i]-arr[j])
    # return m
    # too slow

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(result)
