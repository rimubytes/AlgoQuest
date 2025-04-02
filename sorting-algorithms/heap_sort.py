def heapify(arr, n, i):

    # Initialize largest as root
    largest = i
    
    # Calculate indices of left and right children
    left = 2 * i + 1     # Left child index
    right = 2 * i + 2    # Right child index
    
    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

def heap_sort(arr):
    # Make a copy of the input array to avoid modifying the original
    result = arr.copy()
    n = len(result)
    
    # Build a max heap
    # We start from the last non-leaf node and heapify each node in reverse order
    for i in range(n // 2 - 1, -1, -1):
        heapify(result, n, i)
    
    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Move current root (maximum element) to the end
        result[i], result[0] = result[0], result[i]
        
        # Heapify the reduced heap (excluding the sorted elements)
        heapify(result, i, 0)
    
    return result

def heap_sort_with_steps(arr):
    result = arr.copy()
    n = len(result)
    
    print("Initial array:", result)
    
    # Build a max heap
    print("\nBuilding max heap:")
    for i in range(n // 2 - 1, -1, -1):
        heapify(result, n, i)
        print(f"After heapifying at index {i}: {result}")
    
    print("\nMax heap built:", result)
   # Extract elements one by one
    print("\nExtracting elements:")
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        result[i], result[0] = result[0], result[i]
        print(f"Moved max element {result[i]} to position {i}: {result}")
        
        # Heapify the reduced heap
        heapify(result, i, 0)
        print(f"After heapifying reduced heap: {result}")

def test_heap_sort():
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
        sorted_arr = heap_sort(test_case)
        print(f"Sorted result: {sorted_arr}")
        
        # Verify result with Python's built-in sort
        expected = sorted(test_case)
        assert sorted_arr == expected, f"Sort failed! Expected {expected}, got {sorted_arr}"
        print("Test passed!")
        print("-" * 40)