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
        """
        Perform Depth First Search starting from given vertex using recursion.
        
        Args:
            start (int): Starting vertex for DFS
            visited (Set[int], optional): Set to keep track of visited vertices
        
        Returns:
            List[int]: List of vertices in DFS traversal order
        """
        # Initialize visited set if None
        if visited is None:
            visited = set()
            
        result = []
        
        # Mark current node as visited and add to result
        visited.add(start)
        result.append(start)
        
        # Recur for all adjacent vertices
        for neighbour in self.graph[start]:
            if neighbour not in visited:
                result.extend(self.dfs_recursive(neighbour, visited))
                
        return result

def dfs_iterative(self, start: int) -> List[int]:

        visited = set()
        stack = [start]
        result = []
        
        while stack:
            vertex = stack.pop()
            
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                # Add neighbors to stack in reverse order
                # to maintain similar order to recursive version
                for neighbor in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result