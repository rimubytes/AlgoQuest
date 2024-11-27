def quick_sort(arr):
    """
    Implements the Quick Sort algorithm to sort an array in ascending order

    Parameters:
    arr (list): The input list is to be sorted

    Returns:
    list: A new sorted list

    Time Complexity: O(n log n) average case, O(n^2) worst case
    Space Complexity: O(log n) due to recursion
    """
    # Base case: if the list has 1 or 0 elements, its already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the pivot (last element)
    pivot = arr[-1]

    # Partition the array
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    # Recursively sort left and right partitions and combine
    return quick_sort(left) + [pivot] + quick_sort(right)

 