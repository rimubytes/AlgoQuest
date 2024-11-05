def two_sum(nums, target):
    """
    Finds a pair of indices from the input list 'nums' that add up to the 'target'

    Parameters:
    nums (List[int]): The input list of integers
    target (int): The target sum

    Returns:
    List[int]: A list of two indices, where the elements at those indices 
    """

    # Create a dictionary to store the complements
    complements = {}

    # Iterate through the list of numbers
    for i, num in enumerate(nums):
        # Check if the current number's complement is in the dictionary
        complement = target - num
        if complement in complements:
            # If so, return the indices of the pair
            return [complements[complements], i]
        # Otherwise, store the current number and its index in the dictionary
        complements[num] = 1

    # If no pair is found, return an empty list
    return []