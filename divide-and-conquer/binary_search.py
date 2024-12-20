def binary_search(arr: list, target: int) -> int:
    """
    Performs binary search to find the index of a target value in a sorted array

    Parameters:
    arr (list): A sorted list of intergers
    target (int): The value to search for

    Returns:
    int: Index of the target value, or -1 if not found

    Time Complexity: 0(log n)
    Space Complexity: 0(1)
    """

    # Initialize left and right pointers
    left, right = 0, len(arr) -1

    # Initialize left and right pointers
    left, right = 0, len(arr) - 1
    
    # Continue searching while the search space is valid
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # Check if target is found
        if arr[mid] == target:
            return mid
        
        # If target is less than middle, search left half
        elif arr[mid] > target:
            right = mid - 1
        
        # If target is greater than middle, search right half
        else:
            left = mid + 1
    
    # Target not found
    return -1

def binary_search_recursive(arr: list, target: int, left: int = None, right: int = None) -> int:
    """
    Performs binary search recursively to find the index of a target value in a sorted array.
    
    Parameters:
    arr (list): A sorted list of integers
    target (int): The value to search for
    left (int, optional): Left boundary of search space
    right (int, optional): Right boundary of search space
    
    Returns:
    int: Index of the target value, or -1 if not found
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursive call stack
    """
    # Initialize boundaries on first call
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    # Base case: search space exhausted
    if left > right:
        return -1
    
    # Calculate middle index
    mid = (left + right) // 2
    
    # Check if target is found
    if arr[mid] == target:
        return mid
    
    # Recursively search left half
    if arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    
    # Recursively search right half
    return binary_search_recursive(arr, target, mid + 1, right)

# Example usage demonstration
def demonstrate_binary_search():
    """
    Demonstrates the usage of both iterative and recursive binary search implementations.
    """
    # Sorted array for demonstration
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    # Test cases
    test_cases = [
        7,      # Existing element
        10,     # Non-existing element
        1,      # First element
        19,     # Last element
    ]
    
    print("Iterative Binary Search Results:")
    for target in test_cases:
        index = binary_search(sorted_array, target)
        print(f"Target {target}: Index {index}")
    
    print("\nRecursive Binary Search Results:")
    for target in test_cases:
        index = binary_search_recursive(sorted_array, target)
        print(f"Target {target}: Index {index}")

# Run demonstration
if __name__ == "__main__":
    demonstrate_binary_search()
