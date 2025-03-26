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
    result = arr.copy()
    n = len(result)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(result, n, i)
    
    for i in range(n - 1, 0, -1):
        result[i], result[0] = result[0], result[i]
        
        heapify(result, i, 0)
    