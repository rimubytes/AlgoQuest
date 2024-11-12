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

"""
The `max_subarray` function takes a list of integers `nums` as input and returns the maximum sum of a contiguous subarray within the input array.

Here's how the algorithm works:

1. Initialize `max_sum` and `current_sum` to the first element of the input array `nums`.
2. Iterate through the rest of the array starting from the second element.
3. For each element:
   - Update the `current_sum` by taking the maximum of:
     - The current element `nums[i]`
     - The sum of the current element and the previous `current_sum` (`current_sum + nums[i]`)
   - Update the `max_sum` by taking the maximum of:
     - The current `current_sum`
     - The previous `max_sum`
4. After the loop, return the final `max_sum`.

The key idea behind this algorithm is to keep track of the maximum sum seen so far (`max_sum`) and the maximum sum ending at the current element (`current_sum`). By updating these two values at each step, we can efficiently find the maximum subarray sum.

"""