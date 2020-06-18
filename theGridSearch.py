def gridSearch(G, P):
    flag = "NO"
    # initialises answer

    gridLine = "".join(G)
    # joins grid into one large string

    while (True):
        index = gridLine.find(P[0])
        # finds the lowest index of the first line of the pattern

        if index == -1:
            break
        # if it doesn't exist, end the loop and return NO

        if (index % len(G[0])) + len(P[0]) > len(G[0]):
            gridLine = gridLine[index+1:]
            continue
        # prevents matching if pattern trails onto next line
        # example of edge-case:
        # 0001
        # 2003
        # 4000
        # without the above IF, the pattern 12\n34 would be matched

        counter = 1
        # counts if all lines of the pattern are matched

        for c, pattern in enumerate(P):
            if c == 0:
                continue
            # ignore the first line, as we've already matched it

            point = index + (len(G[0])*c)
            # calculates where the start of the next pattern line should be

            if pattern == gridLine[point: point + len(pattern)]:
                counter += 1
                # increments if line of pattern matches
            else:
                break
                # stops checking otherwise

        if counter == len(P):
            flag = "YES"
            break
            # test if all lines of pattern were matched
            # if so, return YES
        else:
            gridLine = gridLine[index+1:]
            # otherwise, repeat process without the first initial match
    return flag


if __name__ == '__main__':
    file = open("theGridSearch.txt", "r")

    t = int(file.readline())

    for t_itr in range(t):
        RC = file.readline().split()
        R = int(RC[0])
        C = int(RC[1])

        G = []
        for _ in range(R):
            line = file.readline()
            G.append(line.rstrip())

        rc = file.readline().split()
        r = int(rc[0])
        c = int(rc[1])

        P = []
        for _ in range(r):
            line = file.readline()
            P.append(line.rstrip())

        result = gridSearch(G, P)
        print(result)
