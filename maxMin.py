def maxMin(k, arr):
    m = 10**9
    arr.sort()
    for i in range(len(arr)-k+1):
        print(i)
        if arr[i+k-1] - arr[i] < m:
            m = arr[i+k-1] - arr[i]
    return m

if __name__ == '__main__':
    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    print(result)
