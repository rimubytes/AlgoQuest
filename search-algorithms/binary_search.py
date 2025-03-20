def binary_search(arr, target):
    """
    Implementation of binary search algorithm.
    
    Binary search finds the position of a target value within a sorted array.
    It compares the target value to the middle element of the array. If they are not equal,
    the half in which the target cannot lie is eliminated and the search continues
    on the remaining half, again taking the middle element to compare to the target value,
    and repeating until the target value is found. If the search ends with the remaining half
    being empty, the target is not in the array.
    
    Args:
        arr (list): A sorted list of elements
        target: The element to find in the array
        
    Returns:
        int: The index of the target element if found, -1 otherwise
        
    Time Complexity:
        - Best Case: O(1) when the middle element is the target
        - Average Case: O(log n)
        - Worst Case: O(log n) when the target is not in the array or at the ends
        
    Space Complexity:
        - O(1) for iterative implementation
        
    Example:
        >>> binary_search([1, 2, 3, 4, 5, 6], 4)
        3
        >>> binary_search([1, 2, 3, 4, 5, 6], 7)
        -1
    """
    # Set initial boundaries for the search
    left, right = 0, len(arr) - 1
    
    # Continue searching while there are elements to search
    while left <= right:
        # Find middle index, using floor division to get an integer
        # Using (left + right) // 2 can cause overflow in some languages,
        # but Python handles large integers well
        mid = (left + right) // 2
        
        # Check if the middle element is the target
        if arr[mid] == target:
            return mid  # Found the target, return its index
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
            
        # If target is smaller, ignore right half
        else:
            right = mid - 1
            
    # If we reach here, the element was not present
    return -1

def binary_search_recursive(arr, target, left=None, right=None):
    """
    Recursive implementation of the binary search algorithm.
    
    This version uses recursion instead of iteration to perform the search.
    
    Args:
        arr (list): A sorted list of elements
        target: The element to find in the array
        left (int, optional): The left boundary of the search. Defaults to 0.
        right (int, optional): The right boundary of the search. Defaults to len(arr) - 1.

    Returns:
        int: The index of the target element if found, -1 otherwise
        
    Time Complexity:
        - Best Case: O(1) when the middle element is the target
        - Average Case: O(log n)
        - Worst Case: O(log n)
        
    Space Complexity:
        - O(log n) due to recursion stack
        
    Example:
        >>> binary_search_recursive([1, 2, 3, 4, 5, 6], 4)
        3
        >>> binary_search_recursive([1, 2, 3, 4, 5, 6], 7)
        -1
    """
    # Initialize default values for first call
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    
    if left > right:
        return -1
    
    # Find middle index
    mid = (left + right) // 2

    # Check if the middle element is the target
    if arr[mid] == target:
        return mid
    
    # If target is greater, search right half
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    
    # If target is smaller, search left half
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

def test_binary_search():
    test_cases = [
        # (array, target, expected_index)
        ([1, 2, 3, 4, 5, 6], 4, 3),            # Target in the middle
        ([1, 2, 3, 4, 5, 6], 7, -1),           # Target not in array
        ([1, 2, 2, 3, 4, 5], 2, 1),            # First occurrence of duplicate
        ([], 1, -1),                           # Empty array
        ([5], 5, 0),                           # Single element array, target present
        ([5], 1, -1),                          # Single element array, target not present
        ([1, 2, 3, 4, 5, 6], 1, 0),            # Target at beginning
        ([1, 2, 3, 4, 5, 6], 6, 5)             # Target at end
    ]
    
    for i, (arr, target, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: Array: {arr}, Target: {target}")
        
        # Test iterative binary search
        iterative_result = binary_search(arr, target)
        print(f"  Iterative result: {iterative_result}, Expected: {expected}")
        assert iterative_result == expected, f"Iterative search failed! Expected {expected}, got {iterative_result}"
        
        # Test recursive binary search
        recursive_result = binary_search_recursive(arr, target)
        print(f"  Recursive result: {recursive_result}, Expected: {expected}")
        assert recursive_result == expected, f"Recursive search failed! Expected {expected}, got {recursive_result}"
        
        print("  Test passed!")
        print("-" * 40)

print("Demonstration of Binary Search with step-by-step visualization:")
example_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original array: {example_arr}")
print("Searching for 7:")
binary_search_with_steps(example_arr, 7)
print("\nSearching for 11:")
binary_search_with_steps(example_arr, 11)
print("\n")

# Run all tests
print("Running tests for binary search:")
test_binary_search()