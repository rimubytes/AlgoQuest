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

    # Base case: empty tree has depth 0
    if not root:
        return 0
    
    # Recursively find the depth of left and right subtrees
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    # Return the maximum depth between left and right subtrees, plus 1 for current node
    return max(left_depth, right_depth) + 1