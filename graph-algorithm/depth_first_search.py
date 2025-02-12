from typing import List, Set, Dict, Optional
from collections import defaultdict

class Graph:
    """
    A class representing a graph using adjacency list representation.
    
    Attributes:
        vertices (int): Number of vertices in the graph
        graph (Dict[int, List[int]]): Adjacency list representation of the graph
    """
    
    def __init__(self, vertices: int):
        """
        Initialize the graph with given number of vertices.
        
        Args:
            vertices (int): Number of vertices in the graph
        """
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u: int, v: int) -> None:
        """
        Add an edge to the graph.
        
        Args:
            u (int): Source vertex
            v (int): Destination vertex
        """
        self.graph[u].append(v)
