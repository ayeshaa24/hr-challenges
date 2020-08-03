def activityNotifications(expenditure, d):
    n = 0

    current = [expenditure[0]] + expenditure[:d-1]
    # (Repeats index 0 for the sake of the loop)

    count = [0 for i in range(max(expenditure)+1)]

    for i in current:
        count[i] += 1
    # Step 1 of counting sort (counting)
    # (Uses counting sort but seperates the processes
    # so the above process is not repeated each time)

    #d += 1
    # Makes life easier when working with the other arrays later

    for x in range(d, len(expenditure)):
        old = current.pop(0)
        new = expenditure[x-1]
        current.append(new)
        # Adds and removes from the current queue


        count[old] -= 1
        count[new] += 1
        # Updates current count

        acc_count = list(count)
        # Makes a second count for the accumulating process

        for i in range(1, len(count)):
            acc_count[i] += acc_count[i-1]
        # Step 2 of counting sort (accumulating)
        # ^ creates a histogram sort of


        # Note: Step 3 of counting sort has been ignored
        # for the sake of timing, we will not sort
        # Instead, we look for the median in the count array

        if d % 2 == 0:
        # Switched around as d was incremented
        # so even d are, at this point, odd
            for i in range(len(count)):
                # Looking for the frequency bucket with the median
                # The index is then the median
                if acc_count[i] >= math.ceil(d/2):
                    # e.g. If d = 6, we are looking for the 3rd item
                    # in what would be the sorted list, from the buckets
                    # instead of from an actual list (for timing)
                    left = i
                    break
            for i in range(left, len(count)):
                if acc_count[i] >= math.ceil(d/2) + 1:
                    # and also the 4th item
                    right = i
                    break
            median = (left + right)
            if expenditure[x] >= median:
                n += 1
        else:
            for i in range(len(count)):
                if acc_count[i] >= math.ceil(d/2):
                    # Need to round d/2 up
                    # e.g. if d = 5, the 3rd thing is the median
                    # (not the 2nd)
                    #  So we are looking for the 'histogram' 'bucket'
                    # that has the third item
                    median = i
                    break
            if expenditure[x] >= median*2:
                n += 1

    return(n)

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)
