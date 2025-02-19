def insertion_sort(arr):
    """
    Implementation of insertion sort algorithm.
    
    Insertion sort builds the final sorted array one item at a time. It iterates through
    an array, consuming one input element at each repetition, and growing a sorted output list.
    At each iteration, insertion sort removes one element from the input data, finds the
    location it belongs within the sorted list, and inserts it there.
    
    Args:
        arr (list): The array/list to be sorted
        
    Returns:
        list: The sorted array
        
    Time Complexity:
        - Best Case: O(n) when the array is already sorted
        - Average Case: O(n²)
        - Worst Case: O(n²) when the array is sorted in reverse order
        
    Space Complexity:
        - O(1) as it sorts in-place
        
    Example:
        >>> insertion_sort([5, 2, 4, 6, 1, 3])
        [1, 2, 3, 4, 5, 6]
    """
    # Make a copy of the input array to avoid modifying the original
    arr = arr.copy()
    
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Store the current element to be compared
        current_element = arr[i]
        
        # Initialize j to the position before the current element
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than current_element
        # to one position ahead of their current position
        while j >= 0 and arr[j] > current_element:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Place the current element at its correct position
        arr[j + 1] = current_element
        
    return arr