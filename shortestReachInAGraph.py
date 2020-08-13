# BFS: Breadth First search
# best for finding the shortest path
# requires 1) a queue of nodes that need to be visited
# (in this case we don't need it as we can just check the distance value)
# 2) a set of visited nodes
# 3) an iterative approach (that checks if the queue is empty)

class Node():
    def __init__(self, value):
        self.value = value
        self.distance = -1
        self.adjacent = []

    def __repr__(self):
        return(str(self.value))

class Graph():
    def __init__(self, no_of_nodes):
        self.nodes = []
        for i in range(no_of_nodes):
            self.nodes.append(Node(i+1))

    def connect(self, a, b):
        a = self.nodes[a]
        b = self.nodes[b]
        a.adjacent.append(b)
        b.adjacent.append(a)

    def find_all_distances(self, s):
        source = self.nodes[s]
        source.distance = 0

        need_to_visit = []
        need_to_visit.append(source)

        while need_to_visit:
            current = need_to_visit.pop(0)

            # don't need to check if visited (like you normally would)
            # the following code doesnt allow visited nodes to be added

            for i in current.adjacent:
                if i.distance == -1:
                # ^doing this instead of using a visited set avoids the issue
                # of incrementing a node that has been added to the queue twice
                # (if using the set, we would check 1) it hasnt been visited
                # and 2) its not in the need_to_visit list)
                    i.distance = current.distance + 6
                    need_to_visit.append(i)

        ans = [i.distance for i in self.nodes if i != source]

        print(*ans)

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_all_distances(s-1)
