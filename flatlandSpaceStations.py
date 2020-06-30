nm = input().split()

n = int(nm[0])

m = int(nm[1])

c = sorted(list(map(int, input().rstrip().split())))

ans = max(c[0], n-1-c[m-1])
for i in range(m-1):
    diff = (c[i+1] - c[i])//2
    if diff > ans:
        ans = diff

print(ans)
