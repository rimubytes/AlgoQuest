def bubble_sort(arr: list) -> list:
    """
    Implements the bubble sort algorithm to sort a list in ascending order.
    
    Parameters:
    arr (list): The input list to be sorted
    
    Returns:
    list: The sorted list
    
    Time Complexity: O(n^2) in worst and average cases
    Space Complexity: O(1) as it sorts in place
    """
    n = len(arr)
    
    # Optimize by adding a flag to detect if any swap happened
    for i in range(n):
        swapped = False
        
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return arr