def linear_search(arr: list, target: int) -> int:
    """
    Performs linear search to find the index of a target value in an array.
    
    Parameters:
    arr (list): List of elements to search through
    target (int): Value to search for
    
    Returns:
    int: Index of target if found, -1 otherwise
    
    Time Complexity: O(n) - where n is the length of the array
    Space Complexity: O(1) - constant space used
    """
    # Iterate through each element in the array
    for i in range(len(arr)):
        # If target is found, return its index
        if arr[i] == target:
            return i
    
    # Target not found in array
    return -1

def linear_search_all_occurrences(arr: list, target: int) -> list:
    """
    Finds all occurrences of a target value in an array using linear search.
    
    Parameters:
    arr (list): List of elements to search through
    target (int): Value to search for
    
    Returns:
    list: List of indices where target was found
    
    Time Complexity: O(n)
    Space Complexity: O(k) where k is the number of occurrences
    """
    indices = []
    
    # Iterate through the array
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
            
    return indices

def demonstrate_linear_search():
    """
    Demonstrates the usage of linear search algorithms with various examples.
    """
    # Test array
    test_array = [4, 2, 7, 1, 8, 3, 6, 7, 9, 5]
    
    # Test cases
    print("Array:", test_array)
    
    # Single occurrence search
    target = 7
    result = linear_search(test_array, target)
    print(f"\nSearching for first occurrence of {target}")
    if result != -1:
        print(f"Found at index: {result}")
    else:
        print("Not found")

    # Multiple occurrences search
    result_all = linear_search_all_occurrences(test_array, target)
    print(f"\nSearching for all occurrences of {target}")
    if result_all:
        print(f"Found at indices: {result_all}")
    else:
        print("Not found")
    
    # Search for non-existent element
    target = 10
    result = linear_search(test_array, target)
    print(f"\nSearching for {target}")
    if result != -1:
        print(f"Found at index: {result}")
    else:
        print("Not found")

if __name__ == "__main__":
    demonstrate_linear_search()