def fairRations(B):
    # if all subjects have even then sum will be even
    # as only an even number of loaves are distributed (2x)
    # the sum must be in the first place
    # as even + even = even, odd + even = odd
    if sum(B) % 2 != 0:
        return("NO")
    cnt = 0
    for i in range(len(B)-1):
        # not necessary to check before
        if B[i] % 2 != 0:
            # dont necessarily have to increment current
            # as it will not affect algorithm anyway
            B[i+1] += 1
            cnt += 2
    return(cnt)


if __name__ == '__main__':
    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    print(result)
