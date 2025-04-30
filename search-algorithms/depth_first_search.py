def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    # Mark the current node as visited
    visited.add(start)

    # Recursively visit all unvisited neighbors
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited