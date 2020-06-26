def kaprekarNumbers(p, q):
    ans = []
    for i in range(p, q+1):
        n = str(i * i)
        d = len(str(n))
        if d > 1:
            l = int(n[:d//2])
        else:
            l = 0
        r = int(n[d//2:])
        if l + r == i:
            ans.append(i)
    if len(ans) > 0:
        print(*ans)
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
