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

def bubble_sort_verbose(arr: list) -> list:
    """
    Implements bubble sort with step-by-step visualization of the sorting process.
    
    Parameters:
    arr (list): The input list to be sorted
    
    Returns:
    list: The sorted list
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    steps = []
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                # Store the current state of array after swap
                steps.append(f"Step {len(steps) + 1}: Swapped {arr[j+1]} and {arr[j]}")
                steps.append(f"Current array: {arr}")
        
        if not swapped:
            steps.append("Array is sorted!")
            break
    
    # Print all steps
    for step in steps:
        print(step)
    
    return arr

def demonstrate_bubble_sort():
    """
    Demonstrates the usage of bubble sort with various examples.
    """
    # Test cases
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1]   # Reverse sorted
    ]
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"\nTest Case {i}:")
        print(f"Original array: {arr}")
        sorted_arr = bubble_sort(arr.copy())
        print(f"Sorted array: {sorted_arr}")
        
    print("\nDetailed sorting process for [64, 34, 25, 12, 22]:")
    bubble_sort_verbose([64, 34, 25, 12, 22])

if __name__ == "__main__":
    demonstrate_bubble_sort()