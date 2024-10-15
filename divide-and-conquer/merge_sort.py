
from typing import List

def merge_sort(arr: List[int]) -> None:
    """
    Sorts an array in-place using the merge sort algorithm.
    
    Args:
    arr (List[int]): The input array to be sorted.
    
    Returns:
    None: The array is sorted in-place.
    
    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)
    merge(arr, left_half, right_half)

