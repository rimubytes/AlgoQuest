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
