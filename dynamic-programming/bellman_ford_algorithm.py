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
    
    def add_edge(self, source: int, dest: int, weight: float) -> None:
        """
        Add an edge to the graph.
        
        Args:
            source (int): Source vertex
            dest (int): Destination vertex
            weight (float): Weight of the edge
        """
        self.edges.append((source, dest, weight))

def bellman_ford(graph: Graph, source: int) -> Tuple[Optional[Dict[int, float]], Optional[Dict[int, int]]]:
    """
    Implement Bellman-Ford algorithm using dynamic programming approach.
    
    The algorithm finds shortest paths from source vertex to all other vertices.
    It can detect negative weight cycles in the graph.
    
    Dynamic Programming Aspects:
    1. Optimal Substructure: Shortest path contains other shortest paths
    2. Overlapping Subproblems: Same shortest paths are computed multiple times
    3. State: dp[v] represents shortest distance to vertex v
    4. Recurrence Relation: dp[v] = min(dp[v], dp[u] + weight(u,v))
    
    Time Complexity:
        O(V * E) where V is number of vertices and E is number of edges
        
    Space Complexity:
        O(V) for storing distances and predecessors
        
    Args:
        graph (Graph): Input graph with weighted edges
        source (int): Source vertex
        
    Returns:
        Tuple[Optional[Dict[int, float]], Optional[Dict[int, int]]]: 
            - Dictionary of shortest distances and predecessors
            - None, None if negative cycle exists
            
    """
    # Initialize distances and predecessors (dp table)
    distances: Dict[int, float] = {i: inf for i in range(graph.vertices)}
    distances[source] = 0
    predecessors: Dict[int, int] = {i: None for i in range(graph.vertices)}
    
    # Dynamic Programming: Relax edges |V| - 1 times
    for _ in range(graph.vertices - 1):
        # For each edge, try to relax it
        for u, v, weight in graph.edges:
            # Recurrence relation of DP
            if distances[u] != inf and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u
    
    # Check for negative weight cycles
    for u, v, weight in graph.edges:
        if distances[u] != inf and distances[u] + weight < distances[v]:
            print("Graph contains negative weight cycle")
            return None, None
    
    return distances, predecessors