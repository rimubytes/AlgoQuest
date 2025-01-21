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
    
def visualize_solution(graph: Graph, source: int) -> None:
    """
    Visualize the Bellman-Ford algorithm solution with step-by-step path construction.
    
    Args:
        graph (Graph): Input graph
        source (int): Source vertex
    """
    distances, predecessors = bellman_ford(graph, source)
    
    if distances is None or predecessors is None:
        print("Cannot visualize due to negative weight cycle")
        return
    
    print("\nShortest Paths from source vertex", source)
    print("=====================================")
    
    for vertex in range(graph.vertices):
        if vertex != source:
            path = []
            current = vertex
            
            # Reconstruct path
            while current is not None:
                path.append(current)
                current = predecessors.get(current)
            
            # Print path and distance
            path = path[::-1]  # Reverse path
            if distances[vertex] != inf:
                print(f"\nPath to vertex {vertex}:")
                print(f"Distance: {distances[vertex]}")
                print(f"Path: {' -> '.join(map(str, path))}")
            else:
                print(f"\nNo path exists to vertex {vertex}")

# Test the implementation
if __name__ == "__main__":
    # Test Case 1: Basic graph with positive weights
    print("\nTest Case 1: Basic graph with positive weights")
    g1 = Graph(5)
    g1.add_edge(0, 1, 4)
    g1.add_edge(0, 2, 2)
    g1.add_edge(1, 2, 1)
    g1.add_edge(1, 3, 5)
    g1.add_edge(2, 3, 8)
    g1.add_edge(2, 4, 10)
    g1.add_edge(3, 4, 2)
    visualize_solution(g1, 0)
    
    # Test Case 2: Graph with negative weights (but no negative cycles)
    print("\nTest Case 2: Graph with negative weights")
    g2 = Graph(5)
    g2.add_edge(0, 1, 4)
    g2.add_edge(0, 2, 2)
    g2.add_edge(1, 2, -1)
    g2.add_edge(2, 3, 2)
    g2.add_edge(3, 4, -3)
    visualize_solution(g2, 0)