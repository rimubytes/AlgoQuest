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
    left, right = 0, len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  
    
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
