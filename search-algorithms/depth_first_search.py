def dfs(graph, start, visited=None):
    """
    Depth-First Search algorithm implementation.

    Parameters:
    -----------
    graph : dict
        A dictionary representing the graph as an adjacency list.
    start : str or int
        The starting node for DFS traversal.
    visited : set
        A set to keep track of visited nodes. Defaults to None.

    Returns:
    --------
    visited : set
        A set of nodes visited during DFS traversal.
    """
    if visited is None:
        visited = set()

    # Mark the current node as visited
    visited.add(start)

    # Recursively visit all unvisited neighbors
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

# Example Usage
if __name__ == "__main__":
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # Start DFS from node 'A'
    visited_nodes = dfs(graph, 'A')
    print("DFS Traversal Order:", visited_nodes)
