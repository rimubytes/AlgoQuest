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