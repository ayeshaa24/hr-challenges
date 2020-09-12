import timeit

# Complete the gemstones function below.
def gemstones(arr):
    # gemstones = set(arr[0])
    # for rock in arr[1:]:
    #     gemstones = [gem for gem in gemstones if gem in rock]

    # return len(gemstones)

    # SET THEORY!!!
    gemstones = set(arr[0])
    for rock in arr[1:]:
        gemstones = gemstones.intersection(set(rock))

    return(len(gemstones))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
