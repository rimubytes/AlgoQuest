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

def insertion_sort_with_steps(arr):
    """
    Implementation of insertion sort algorithm with step-by-step visualization.
    
    This version prints the state of the array after each insertion operation,
    making it useful for educational purposes.
    
    Args:
        arr (list): The array/list to be sorted
        
    Returns:
        list: The sorted array
        
    Example:
        >>> insertion_sort_with_steps([5, 2, 4, 6, 1, 3])
        Step 1: [2, 5, 4, 6, 1, 3]
        Step 2: [2, 4, 5, 6, 1, 3]
        Step 3: [2, 4, 5, 6, 1, 3]
        Step 4: [1, 2, 4, 5, 6, 3]
        Step 5: [1, 2, 3, 4, 5, 6]
        [1, 2, 3, 4, 5, 6]
    """
    # Make a copy of the input array
    arr = arr.copy()
    
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1
        
        # Move elements greater than current_element one position ahead
        while j >= 0 and arr[j] > current_element:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Place current element at its correct position
        arr[j + 1] = current_element
        
        # Print the current state of the array
        print(f"Step {i}: {arr}")
        
    return arr

def test_insertion_sort():
    """
    Test function for insertion sort implementation.
    
    This function tests insertion sort with various inputs:
    - Random array
    - Already sorted array
    - Reverse sorted array
    - Array with duplicate elements
    - Empty array
    - Array with one element
    """

    test_cases = [
        [5, 2, 4, 6, 1, 3],           
        [1, 2, 3, 4, 5, 6],           
        [6, 5, 4, 3, 2, 1],           
        [3, 1, 4, 1, 5, 9, 2, 6, 5],  
        [],                           
        [1]                           
    ]

    for i, test_case in enumerate(test_cases):
        print(f"Test case {i+1}: {test_case}")
        sorted_arr = insertion_sort(test_case)
        print(f"Sorted result: {sorted_arr}")
        
        # Verify result with Python's built-in sort
        expected = sorted(test_case)
        assert sorted_arr == expected, f"Sort failed! Expected {expected}, got {sorted_arr}"
        print("Test passed!")
        print("-" * 40)