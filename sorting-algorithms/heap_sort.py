def heapify(arr, n, i):

    largest = i
    
    left = 2 * i + 1     
    right = 2 * i + 2    
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


