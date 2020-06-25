from math import ceil
s = input().strip().replace(" ", "")
col = ceil(len(s) ** 0.5)
ans = " ".join([s[i::col] for i in range(col)])
print(ans)
