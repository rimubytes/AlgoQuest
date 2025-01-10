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
