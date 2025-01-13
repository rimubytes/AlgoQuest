from collections import deque
from typing import Dict, List, Set

class Graph:
    """
    A class to represent a graph using an adjacency list representation.
    """
    def __init__(self):
        """Initialize an empty graph using dictionary to store edges."""
        self.graph: Dict[int, List[int]] = {}
    
    def add_edge(self, u: int, v: int) -> None:
        """
        Add an edge between vertices u and v.
        
        Args:
            u (int): Source vertex
            v (int): Destination vertex
        """
        # Add edge from u to v
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        
        # Add edge from v to u (for undirected graph)
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

def bfs(graph: Graph, start_vertex: int) -> Dict[int, int]:
    """
    Performs Breadth First Search traversal of the graph.
    
    BFS explores all vertices at the current depth before moving to vertices
    at the next depth level. It uses a queue to keep track of vertices to visit.
    
    Args:
        graph (Graph): The graph to traverse
        start_vertex (int): The starting vertex for BFS
        
    Returns:
        Dict[int, int]: Dictionary containing distances from start vertex to all reachable vertices
        
    Time Complexity:
        - O(V + E) where V is number of vertices and E is number of edges
        
    Space Complexity:
        - O(V) for the queue and visited set
        
    Example:
        >>> g = Graph()
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(2, 3)
        >>> distances = bfs(g, 0)
        >>> print(distances)
        {0: 0, 1: 1, 2: 1, 3: 2}
    """
    # Initialize visited set and queue
    visited: Set[int] = set()
    queue = deque()
    distances: Dict[int, int] = {}
    
    # Start from the initial vertex
    queue.append(start_vertex)
    visited.add(start_vertex)
    distances[start_vertex] = 0
    
    # Process vertices in queue
    while queue:
        # Remove vertex from queue
        current_vertex = queue.popleft()
        
        # Process all adjacent vertices
        for neighbor in graph.graph.get(current_vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                distances[neighbor] = distances[current_vertex] + 1
    
    return distances

def visualize_bfs(graph: Graph, start_vertex: int) -> None:

    visited: Set[int] = set()
    queue = deque()
    level = 0
    
    queue.append(start_vertex)
    visited.add(start_vertex)
    
    print(f"\nStarting BFS from vertex {start_vertex}")
    
    while queue:
        vertices_at_level = len(queue)
        print(f"\nLevel {level}:")
        print(f"Queue: {list(queue)}")
        
        for _ in range(vertices_at_level):
            current_vertex = queue.popleft()
            print(f"Processing vertex: {current_vertex}")
            
            for neighbor in graph.graph.get(current_vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    print(f"  Discovered neighbor: {neighbor}")
        
        level += 1
