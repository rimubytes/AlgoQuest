def linear_search(arr: list, target: int) -> int:
    """
    Performs linear search to find the index of a target value in an array.
    
    Parameters:
    arr (list): List of elements to search through
    target (int): Value to search for
    
    Returns:
    int: Index of target if found, -1 otherwise
    
    Time Complexity: O(n) - where n is the length of the array
    Space Complexity: O(1) - constant space used
    """
    # Iterate through each element in the array
    for i in range(len(arr)):
        # If target is found, return its index
        if arr[i] == target:
            return i
    
    # Target not found in array
    return -1

