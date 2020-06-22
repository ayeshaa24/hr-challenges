import timeit

# faster but not as neat
def surfaceArea():
    H = 3
    W = 3
    A = [
        [1, 3, 4],
        [2, 2, 3],
        [1, 2, 4]
    ]

    total = 2 * len(A) * len(A[0])
    # top, bottom
    for row in range(len(A)):
        for col in range(len(A[row])):
            # left
            if row - 1 > -1:
                if A[row-1][col] < A[row][col]:
                    total += A[row][col] - A[row-1][col]
            else:
                total += A[row][col]
            # right
            if row + 1 < len(A):
                if A[row+1][col] < A[row][col]:
                    total += A[row][col] - A[row+1][col]
            else:
                total += A[row][col]
            # up
            if col - 1 > -1:
                if A[row][col-1] < A[row][col]:
                    total += A[row][col] - A[row][col-1]
            else:
                total += A[row][col]
            # down
            if col + 1 < len(A[row]):
                if A[row][col+1] < A[row][col]:
                    total += A[row][col] - A[row][col+1]
            else:
                total += A[row][col]
    return(total)

def altSurfaceArea():
    H = 3
    W = 3
    A = [
        [1, 3, 4],
        [2, 2, 3],
        [1, 2, 4]
    ]

    total = 2 * W * H
    # top, bottom
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for row in range(H):
        for col in range(W):
            for r, c in directions:
                if -1 in [row+r, col+c] or row+r==len(A) or col+c==len(A[row]):
                    total += A[row][col]
                # if neighbour is out of bounds, then the area must be visible
                else:
                    total += max(0, A[row][col]-A[row+r][col+c])
                # if 0 is max, then area is not visible
                # if 0 is not max, then area is visible and the amount
                # covered is taken into acocunt
    return(total)



if __name__ == '__main__':
    setup = """
from __main__ import surfaceArea
"""
    test = """
surfaceArea()
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 3,
                          number = 100000)

    # printing minimum exec. time
    print('Calculation: {}'.format(min(times)))

    setup = """
from __main__ import altSurfaceArea
"""
    test = """
altSurfaceArea()
"""
    times = timeit.repeat(setup = setup,
                          stmt = test,
                          repeat = 3,
                          number = 100000)

    print('Calculation: {}'.format(min(times)))



    # HW = input().split()
    # H = int(HW[0])
    # W = int(HW[1])
    #
    # A = []
    # for _ in range(H):
    #     A.append(list(map(int, input().rstrip().split())))
