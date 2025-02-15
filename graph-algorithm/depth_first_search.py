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

    def dfs_recursive(self, start: int, visited: Optional[Set[int]] = None) -> List[int]:
        # Initialize visited set if None
        if visited is None:
            visited = set()
            
        result = []
        
        # Mark current node as visited and add to result
        visited.add(start)
        result.append(start)
        
        # Recur for all adjacent vertices
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                result.extend(self.dfs_recursive(neighbor, visited))
                
        return result