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
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element of unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

# Example usage with step-by-step visualization
def visualize_selection_sort(arr):
    """
    Demonstrates selection sort with step-by-step visualization.
    
    Args:
        arr (list): The input list to be sorted
        
    Returns:
        None: Prints the sorting steps
    """
    print("Original array:", arr)
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Step {i + 1}: {arr} (Swapped {arr[i]} to position {i})")
