from collections import deque


class TreeNode:
    """
    A class representing a node in a tree structure.
    
    Attributes:
        value: The value stored in the node
        children: A list of child nodes
    """
    def __init__(self, value):
        """Initialize a TreeNode with the given value and empty children list."""
        self.value = value
        self.children = []
    
    def add_child(self, child_node):
        """Add a child node to this node."""
        self.children.append(child_node)
    
    def __repr__(self):
        """Return string representation of the node."""
        return f"TreeNode({self.value})"
    

class Graph:
    def __init__(self, directed=False):
        """Initialize an empty graph."""
        self.graph = {}
        self.directed = directed
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        """Add an edge between two vertices."""
        # Add vertices if they don't exist
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        
        # Add edge
        self.graph[from_vertex].append(to_vertex)
        
        # If undirected, add reverse edge
        if not self.directed:
            self.graph[to_vertex].append(from_vertex)

    def get_neighbors(self, vertex):
        """Get all neighbors of a vertex."""
        return self.graph.get(vertex, [])