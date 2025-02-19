def insertion_sort(arr):

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