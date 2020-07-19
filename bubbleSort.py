def countSwaps(a):
    flag = True
    c = 0
    while (flag):
        flag = False
        for i in range(len(a)-1):
            if a[i+1] < a[i]:
                flag = True
                a[i], a[i+1] = a[i+1], a[i]
                c += 1
                
    print("Array is sorted in {} swaps.".format(c))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[len(a)-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
