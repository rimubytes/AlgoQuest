class TreeNode:
    """
    Definition for a binary tree node.
    
    Attributes:
        val (int): The value stored in the node
        left (TreeNode): Reference to the left child node
        right (TreeNode): Reference to the right child node
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right