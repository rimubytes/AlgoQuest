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
    
def bfs_tree_search(root, target_value):
    if root is None:
        return None
    
    # Initialize queue with the root node
    queue = deque([root])
    
    while queue:
        # Dequeue the front node
        current = queue.popleft()
        
        # Check if current node contains the target value
        if current.value == target_value:
            return current
        
        # Add all children to the queue for next level exploration
        for child in current.children:
            queue.append(child)
    
    # Target value not found
    return None

def bfs_tree_traversal(root):
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        result.append(current.value)
        
        # Add all children to the queue
        for child in current.children:
            queue.append(child)
    
    return result

def bfs_graph_search(graph, start_vertex, target_value):
    if start_vertex not in graph.graph:
        return None
    
    # Keep track of visited vertices to avoid cycles
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)
    
    while queue:
        current = queue.popleft()
        
        # Check if current vertex is the target
        if current == target_value:
            return current
        
        # Explore all unvisited neighbors
        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    # Target value not found
    return None

def bfs_shortest_path(graph, start_vertex, target_vertex):
    """
    Find the shortest path between two vertices using BFS.
    
    Args:
        graph: Graph object to search in
        start_vertex: The starting vertex
        target_vertex: The target vertex
        
    Returns:
        list: The shortest path as a list of vertices, or None if no path exists
        
    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V) for the visited set, queue, and parent tracking
    """
