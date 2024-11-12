def max_subarray(nums):
    """
    Finds the contiguous subarray within an input array (nums) that has the maximum sum

    Parameters:
    int: (List[int]): The input array of integers

    Returns:
    int: The maximum sum od a contiguous subarray
    """

    max_sum = nums[0] # Initialize max_sum to the first element
    current_sum = nums[0] # Initialize current_sum to the first element

    for i in range(1, len(nums)):
        # Update the current_sum by taking the maximum of:
        # 1. The current element
        # 2. The sum of the current element and the previous current_sum
        current_sum = max(nums[i], current_sum + nums[i])

        # Update the max_sum by taking the maximum of:
        # 1. The current_sum
        # 2. The previous max_sum
        max_sum = max(max_sum, current_sum)

    return max_sum

