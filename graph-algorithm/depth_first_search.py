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
        """
        Perform Depth First Search starting from given vertex using iteration.
        
        Args:
            start (int): Starting vertex for DFS
        
        Returns:
            List[int]: List of vertices in DFS traversal order
        """
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

def dfs_find_path(self, start: int, end: int) -> Optional[List[int]]:
    """
    Find a path between start and end vertices using DFS.
    
    Args:
        start (int): Starting vertex
        end (int): Target vertex
    
    Returns:
        Optional[List[int]]: Path from start to end if exists, None otherwise
    """
    visited = set()
    path = []
    
    def dfs_path_helper(current: int) -> bool:
        visited.add(current)
        path.append(current)
        
        if current == end:
            return True
            
        for neighbor in self.graph[current]:
            if neighbor not in visited:
                if dfs_path_helper(neighbor):
                    return True
        
        path.pop()
        return False
    
    if dfs_path_helper(start):
        return path
    return None

def test_dfs():
    """
    Test function demonstrating the usage of DFS implementations.
    """
    # Create a sample graph
    #     0
    #    / \
    #   1   2
    #  /   / \
    # 3   4   5
    
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    
    print("Graph Structure:")
    print("0 -> 1, 2")
    print("1 -> 3")
    print("2 -> 4, 5")
    print("\nTest Results:")
    
    # Test recursive DFS
    print("Recursive DFS starting from vertex 0:", g.dfs_recursive(0))
    
    # Test iterative DFS
    print("Iterative DFS starting from vertex 0:", g.dfs_iterative(0))
    
    # Test path finding
    print("Path from 0 to 5:", g.dfs_find_path(0, 5))
    print("Path from 3 to 5:", g.dfs_find_path(3, 5))  # No path exists

# Run the test
if __name__ == "__main__":
    test_dfs()