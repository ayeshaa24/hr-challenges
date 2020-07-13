# NOTE:
# BASECASES:
# f(0) = 1, f(1) = 2, f(2) = 4
# STEPCASE:
# f(i) = f(i-1) + f(i-2) + f(i-3)


# --- METHODS THAT WORK ---
# METHOD 1: using 'cache' and base/step cases

cache = {
    1: 1,
    2: 2,
    3: 4
}

def stepPerms(n):
    if n in cache:
        return cache[n]
    cache[n] = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
    return cache[n]

# METHOD TO TRY OUT: linear recurrences...
# https://www.hackerearth.com/practice/notes/solving-linear-recurrence-relation/
# def stepPerms(n):
    # f1 = [[1], [2], [4]]
    # t = [
    #     [0, 1, 0],
    #     [0, 0, 1],
    #     [4, 2, 1]
    # ]

    # result = [
    #     [0,0,0],
    #     [0,0,0],
    #     [0,0,0]
    # ]

    # for i in range(n-1):
    #     # iterate through rows of X
    #     for i in range(len(result)):
    #     # iterate through columns of Y
    #         for j in range(len(f1[0])):
    #             # iterate through rows of Y
    #             for k in range(len(f1)):
    #                 result[i][j] += result[i][k] * f1[k][j]
    # UNFINISHED
    # need to do t^(n-1) * f1 and then get the first row...?

# --- METHODS THAT TIME OUT ---

# METHOD: just logic...
# def stepPerms(n):
    # TIME OUT
    # if n == 0:
    #     return 1
    # elif n < 0:
    #     return 0
    # return stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)


# METHOD: using base/step case
# def stepPerms(n):
    # if n == 1:
    #     return 1
    # elif n == 2:
    #     return 2
    # elif n == 3:
    #     return 4
    # return stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)

# METHOD: using loop
# def stepPerms(n):
    # if n == 0:
    #     return 1
    # count = 0
    # for i in range(1, min(4, n+1)):
    #     count += stepPerms(n-i)
    # return count

if __name__ == '__main__':
    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        print(res)
