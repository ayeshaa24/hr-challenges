from collections import defaultdict

# KEY CONCEPT: Reverse lookup ({v: k})
# http://stupidpythonideas.blogspot.com/2014/07/reverse-dictionary-lookup-and-more-on.html

if __name__ == '__main__':
    q = int(input().strip())

    freq = defaultdict(int)
    # Keeps track of frequency of each item

    rev = defaultdict(int)
    # Keeps track of frequencies

    for _ in range(q):
        query = list(map(int, input().rstrip().split()))

        q = query[0]
        x = query[1]

        if q == 1:
            rev[freq[x]] -= 1
            freq[x] += 1
            rev[freq[x]] += 1
        elif q == 2:
            if freq[x] > 0:
                rev[freq[x]] -= 1
                freq[x] -= 1
                rev[freq[x]] += 1
        else:
            if rev[x] > 0:
                print(1)
            else:
                print(0)
