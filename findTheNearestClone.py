class Node():
    def __init__(self, value, colour):
        self.value = value
        self.colour = colour
        self.adjacent = []

    def __repr__(self):
        return("{}".format(self.value))

def connect_nodes(a, b):
    a.adjacent.append(b)
    b.adjacent.append(a)

# not sure if its 100% correct -_- test cases dont test well
# an issue both have:
# if on the same level, e.g. 1 out
# if we're on their second node on that level, path will be 2
# when it should be 1
# however both code sort of works anyway
# as we look at node in the node pair, if one path is incorrect
# the other is correct
# iffy -_-

# dfs approach
def dfsFindShortest(graph_nodes, graph_from, graph_to, ids, val):
    all_nodes = {}
    for i in range(graph_nodes):
        all_nodes[i+1] = Node(i+1, ids[i])

    for i in range(len(graph_from)):
        a = all_nodes[graph_from[i]]
        b = all_nodes[graph_to[i]]
        connect_nodes(a, b)

   ans = 100000000
   for i in all_nodes.values():
       if i.colour != val:
           continue

        visited = set()

        temp = dfs(i, visited, 0, val)
        if temp and temp < ans:
            ans = temp

    return ans if ans != 100000000 else -1


def dfs(node, visited, path, val):
    if node in visited:
        return 0

    if path and node.colour == val:
        return path

    visited.add(node)
    path += 1

    for n in node.adjacent:
        new_path = dfs(n, visited, path, val)
        if new_path:
            return new_path

    return 0


# bfs approach
def bfsFindShortest(graph_nodes, graph_from, graph_to, ids, val):
    all_nodes = {}
    for i in range(graph_nodes):
        all_nodes[i+1] = Node(i+1, ids[i])

    for i in range(len(graph_from)):
        a = all_nodes[graph_from[i]]
        b = all_nodes[graph_to[i]]
        connect_nodes(a, b)

    ans = 100000000

    for i in all_nodes.values():
        if i.colour != val:
            continue

        visited = set()
        need_to_visit = [i]
        path = 0

        while need_to_visit:
            current = need_to_visit.pop(0)

            if current in visited:
                continue

            if path and current.colour == val:
                break

            visited.add(current)
            path += 1


            for n in current.adjacent:
                need_to_visit.append(n)

        if path != graph_nodes and path < ans:
            ans = path

    return ans if ans != 100000000 else -1







if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
