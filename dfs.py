class Node():
    def __init__(self, value):
        self.value = value
        self.adjacent = []

    def __repr__(self):
        return("{}".format(self.value))

class Graph():
    def __init__(self):
        self.node_lookup = {}
        # maps integer value to node

    def add_node(self, value):
        self.node_lookup[value] = Node(value)

    def get_node(self, value):
        return self.node_lookup[value]

    def connect_nodes(self, source, destination):
        one = self.get_node(source)
        two = self.get_node(destination)
        one.adjacent.append(two)
        # two.adjacent.append(one)
        #^ OPTIONAL?? children cant find their parents without this...

    def check_path(self, source, destination):
        # parameters are both integers
        s = self.get_node(source)
        d = self.get_node(destination)

        visited = set()

        return self.dfs(s, d, visited)

    def dfs(self, source, destination, visited):
        if source.value in visited:
            return False

        visited.add(source.value)

        if source is destination: # (checking if identical)
            return True

        for node in source.adjacent:
            if self.dfs(node, destination, visited):
                return True

        return False

if __name__ == "__main__":
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    graph.connect_nodes(1, 2)
    graph.connect_nodes(1, 3)
    graph.connect_nodes(3, 4)
    print(graph.check_path(1, 5))
