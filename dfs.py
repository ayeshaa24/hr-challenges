def check_path(source, destination):
    # parameters are both integers
    s = getNode(source)
    d = getNode(destination)

    visited = set()

    return dfs(s, d, visited)

def dfs(source, destination, visited):
    if source.value in visited:
        return False

    visited.add(source.value)

    if source is destination: # (checking if identical)
        return True

    for node in source.adjacent:
        if dfs() # AHTHIS IS DFS NOT BFS
