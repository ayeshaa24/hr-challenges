def cavityMap(grid):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[0])-1):
            flag = True
            for i, j in directions:
                if grid[row][col] <= grid[row+i][col+j]:
                    flag = False
                    break
            if flag:
                temp = list(grid[row])
                temp[col] = "X"
                grid[row] = "".join(temp)
    return grid

if __name__ == '__main__':
    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    print(result)
