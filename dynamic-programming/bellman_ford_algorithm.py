from typing import List, Dict, Tuple, Optional
from math import inf

class Graph:
    """
    A class to represent a weighted directed graph for Bellman-Ford algorithm.
    
    Attributes:
        vertices (int): Number of vertices in the graph
        edges (List[Tuple[int, int, float]]): List of edges with weights
    """
    def __init__(self, vertices: int):
        """
        Initialize graph with given number of vertices.
        
        Args:
            vertices (int): Number of vertices in the graph
        """
        self.vertices = vertices
        self.edges: List[Tuple[int, int, float]] = []