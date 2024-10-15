
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

def merge(arr: List[int], left: List[int], right: List[int]) -> None:
    """
    Merges two sorted arrays into the original array.
    
    Args:
    arr (List[int]): The original array to merge into.
    left (List[int]): The left sorted half.
    right (List[int]): The right sorted half.
    
    Returns:
    None: The merge is done in-place.
    """
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def main():
    """
    Example usage of the merge sort algorithm.
    """
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr)
    merge_sort(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()
