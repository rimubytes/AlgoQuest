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