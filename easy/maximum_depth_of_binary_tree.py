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

def maxDepth(root: TreeNode) -> int:
    """
    Find the maximum depth (height) of a binary tree.
    
    The maximum depth is the number of nodes along the longest path 
    from the root node down to the farthest leaf node.
    
    Time Complexity:
        O(n) where n is the number of nodes in the tree
        We visit each node exactly once
        
    Space Complexity:
        O(h) where h is the height of the tree
        In worst case (skewed tree), h = n
        In best case (balanced tree), h = log(n)
        
    Args:
        root (TreeNode): Root node of the binary tree
        
    Returns:
        int: Maximum depth of the tree. Returns 0 for empty tree.
        
    Example:
        Given binary tree [3,9,20,null,null,15,7]:
             3
            / \
           9  20
              / \
             15  7
        Returns 3
    """
    # Base case: empty tree has depth 0
    if not root:
        return 0
    
    # Recursively find the depth of left and right subtrees
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    # Return the maximum depth between left and right subtrees, plus 1 for current node
    return max(left_depth, right_depth) + 1