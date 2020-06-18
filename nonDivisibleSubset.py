n, k = map(int, input().strip().split(" "))
s = map(int,input().strip().split(" "))


modBuckets = [0] * k
for i in s:
    modBuckets[i % k] += 1

answer = 0
# only loops through half inclusive (hence +1)
# so buckets aren't double counted
for bucket in range((len(modBuckets) // 2) + 1):
    otherBucket = k - bucket
    # if bucket is 0, only one value from that bucket can be put in the set
    # as two values would add up to be divisible by k
    # this is also true if the bucket num = half of k
    # however, one value from these buckets can still be put in
    # as no other bucket will add to it to be divisible by k
    # hence, if the bucket is not empty, answer is incremented
    if (bucket == otherBucket or bucket == 0):
        if (modBuckets[bucket] > 0):
            answer += 1
    # for other buckets e.g. if k = 3, buckets 1 and 2 cannot be put in
    # simulatenously as they will be divisble by k if added
    # so the larger of the two buckets is added to answer
    else:
        answer += max(modBuckets[bucket], modBuckets[otherBucket])
print(answer)
