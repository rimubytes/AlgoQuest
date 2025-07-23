from collections import deque
"""
Breadth-First Search (BFS) Algorithm Implementation

This module implements the BFS algorithm as a search algorithm for both tree and graph
structures. BFS explores nodes level by level, making it optimal for finding the
shortest path in unweighted graphs and the shallowest solution in tree searches.

"""
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
    if start_vertex not in graph.graph or target_vertex not in graph.graph:
        return None
    
    if start_vertex == target_vertex:
        return [start_vertex]
    
    # Keep track of visited vertices and their parents
    visited = set()
    parent = {}
    queue = deque([start_vertex])
    visited.add(start_vertex)
    parent[start_vertex] = None

    while queue:
        current = queue.popleft()
        
        # Explore all unvisited neighbors
        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
                
                # If we found the target, reconstruct the path
                if neighbor == target_vertex:
                    path = []
                    node = target_vertex
                    while node is not None:
                        path.append(node)
                        node = parent[node]
                    return path[::-1]  # Reverse to get path from start to target    
    # No path found
    return None

def bfs_level_order_with_levels(root):
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        # Process all nodes at the current level
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)
            
            # Add children for the next level
            for child in node.children:
                queue.append(child)
        
        result.append(current_level)
    
    return result

if __name__ == "__main__":
    print("=== BFS Tree Search Examples ===")

    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    
    root.add_child(node2)
    root.add_child(node3)
    root.add_child(node4)
    node2.add_child(node5)
    node2.add_child(node6)
    node4.add_child(node7)
    node4.add_child(node8)

    print("BFS Traversal:", bfs_tree_traversal(root))
    
    # Test BFS search
    found_node = bfs_tree_search(root, 7)
    print(f"Searching for 7: {found_node}")  # TreeNode(7)
    
    not_found = bfs_tree_search(root, 10)
    print(f"Searching for 10: {not_found}")  # None

    # Test level-order traversal with levels
    levels = bfs_level_order_with_levels(root)
    print("Level-order with levels:", levels)  
    
    print("\n=== BFS Graph Search Examples ===")

    graph = Graph()
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    for vertex in vertices:
        graph.add_vertex(vertex)
    
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), 
             ('C', 'E'), ('D', 'F'), ('E', 'F')]
    for from_v, to_v in edges:
        graph.add_edge(from_v, to_v)