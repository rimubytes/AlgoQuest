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
