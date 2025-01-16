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

def visualize_tree_depth(root: TreeNode) -> None:
    """
    Visualize the depth calculation process for a binary tree.
    
    Args:
        root (TreeNode): Root node of the binary tree
    """
    def _visualize_depth(node: TreeNode, depth: int, prefix: str = "") -> None:
        if not node:
            print(f"{prefix}None (Depth: {depth})")
            return
        
        print(f"{prefix}Node: {node.val} (Depth: {depth})")
        _visualize_depth(node.left, depth + 1, prefix + "├── Left: ")
        _visualize_depth(node.right, depth + 1, prefix + "└── Right: ")
    
    print("\nTree Structure with Depths:")
    _visualize_depth(root, 1)
    print(f"\nMaximum Depth: {maxDepth(root)}")

# Test cases
def test_max_depth():
    """
    Test the maxDepth function with various tree configurations.
    """
    # Test Case 1: Regular balanced tree
    #      3
    #     / \
    #    9  20
    #       / \
    #      15  7
    tree1 = TreeNode(3)
    tree1.left = TreeNode(9)
    tree1.right = TreeNode(20)
    tree1.right.left = TreeNode(15)
    tree1.right.right = TreeNode(7)
    print("\nTest Case 1: Balanced Tree")
    visualize_tree_depth(tree1)

    # Test Case 2: Linear tree (skewed)
    #    1
    #     \
    #      2
    #       \
    #        3
    tree2 = TreeNode(1)
    tree2.right = TreeNode(2)
    tree2.right.right = TreeNode(3)
    print("\nTest Case 2: Skewed Tree")
    visualize_tree_depth(tree2)
    
    # Test Case 3: Empty tree
    print("\nTest Case 3: Empty Tree")
    visualize_tree_depth(None)
    
    # Test Case 4: Single node tree
    print("\nTest Case 4: Single Node Tree")
    visualize_tree_depth(TreeNode(1))

if __name__ == "__main__":
    test_max_depth()