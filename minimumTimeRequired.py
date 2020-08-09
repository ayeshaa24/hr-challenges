import math
def minTime(machines, goal):
    # obvious solution
    # from collections import Counter
    # c = dict(Counter(machines))
    # i = 0
    # while goal > 0:
    #     i += 1
    #     for k, v in c.items():
    #         print(k)
    #         if i % k == 0:
    #             goal -= v
    # return i

    # in search, so must be search
    right = math.ceil(goal/len(machines) * max(machines))
    # number of days if every machine was the slowest machine

    left = math.ceil(goal/len(machines) * min(machines))
    # number of days if every machine was the fastest machine

    from collections import Counter
    c = dict(Counter(machines)).items()

    ans = 0

    # a 'sort of' binary search for the day that has items >= goal 
    while left <= right:
        middle = (left+right)//2
        total = count(c, middle)
        if total < goal:
            left = middle + 1
        else:
            ans = middle
            right = middle - 1
            # saves an answer that is bigger than the goal
            # but it continues, trying to find a smaller goal
            # this is necessary in case the exact goal is never reached
            # (if it instead overshoots)
    return ans

def count(machines, i):
    # counts the number of items made by the given day, i
    total = 0
    for k, v in machines:
        total += int(i/k) * v
    return total



if __name__ == '__main__':
    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    print(ans)
