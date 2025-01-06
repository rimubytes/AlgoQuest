def selection_sort(arr):
    """
    Implements the selection sort algorithm to sort a list in ascending order.
    
    The algorithm works by repeatedly finding the minimum element from the unsorted portion
    of the array and placing it at the beginning of the sorted portion.
    
    Args:
        arr (list): The input list to be sorted
        
    Returns:
        list: The sorted list in ascending order
        
    Time Complexity:
        - Best Case: O(n^2)
        - Average Case: O(n^2)
        - Worst Case: O(n^2)
        
    Space Complexity:
        - O(1) as it sorts in-place
        
    Example:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> selection_sort(arr)
        [11, 12, 22, 25, 34, 64, 90]
    """