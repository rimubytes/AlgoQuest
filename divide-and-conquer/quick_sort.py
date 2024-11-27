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

def quick_sort_in_place(arr, low=0, high=None):
    """
    Implements an in-place quick sort algorithm

    Parameters:
    arr (list): The input list to be sorted
    low (int): Starting index of the partition
    high (int): Ending index of the partition
    """
    if high is None:
        high = len(arr) - 1
    
    def partition(arr, low, high):
        """
        Partitions the array and returns the pivot index

        Uses the last element as the pivot
        """
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def _quick_sort(arr, low, high):
        """
        Recursive helper function to perform quick sort
        """
        if low < high:
            # Find pivot index
            pivot_index = partition(arr, low, high)

            # Recursively sort left and right partitions
            _quick_sort(arr, low, pivot_index - 1)
            _quick_sort(arr, pivot_index + 1, high)

    # Call internal recursive function
    _quick_sort(arr, low, high)
    return arr