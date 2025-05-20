"""
Longest Common Subsequence (LCS) Dynamic Programming Implementation

This module implements the LCS algorithm which finds the longest subsequence
common to two sequences. A subsequence is a sequence that can be derived from
another sequence by deleting some or no elements without changing the order
of the remaining elements.
"""
    
def longest_common_subsequence(text1, text2):
    """
    Find the longest common subsequence between two strings using dynamic programming.
    
    Args:
        text1 (str): First string
        text2 (str): Second string
        
    Returns:
        str: The longest common subsequence
    
    Time Complexity: O(m*n) where m and n are the lengths of the input strings
    Space Complexity: O(m*n)
    """
    
    m, n = len(text1), len(text2)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If current characters match, extend the LCS by 1
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Otherwise, take the maximum LCS possible by excluding either character
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct the LCS from the dp table
    lcs = []
    i, j = m, n
    
    while i > 0 and j > 0:
        # If current characters match, they are part of LCS
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        # Otherwise, move in the direction of the larger value
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    # Return the reconstructed LCS (reversed, since we built it backwards)
    return ''.join(reversed(lcs))

def lcs_length(text1, text2):
    """
    Find only the length of the longest common subsequence.
    This is more memory-efficient if we don't need the actual subsequence.
    
    Args:
        text1 (str): First string
        text2 (str): Second string
        
    Returns:
        int: The length of the longest common subsequence
    
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    # Get the lengths of the input strings
    m, n = len(text1), len(text2)
    
    # Create a 2D DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # The bottom-right cell contains the length of the LCS
    return dp[m][n]

def lcs_optimized_space(text1, text2):
    """
    Find the longest common subsequence between two strings using dynamic programming.
    
    Args:
        text1 (str): First string
        text2 (str): Second string
        
    Returns:
        str: The longest common subsequence
    
    Time Complexity: O(m*n) where m and n are the lengths of the input strings
    Space Complexity: O(m*n)
    """
    # Ensure text1 is the shorter string to optimize space
    if len(text1) > len(text2):
        text1, text2 = text2, text1
    
    m, n = len(text1), len(text2)
    
    # We only need to store two rows of the DP table at any time
    prev_row = [0] * (m + 1)
    curr_row = [0] * (m + 1)
    
    # Fill the dp table one row at a time
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                curr_row[i] = prev_row[i - 1] + 1
            else:
                curr_row[i] = max(prev_row[i], curr_row[i - 1])
        
        # Update prev_row for the next iteration
        prev_row, curr_row = curr_row, [0] * (m + 1)
    
    # The last filled row contains the answer
    return prev_row[m]

def print_dp_table(dp, text1, text2):
    """
    Helper function to visualize the DP table for educational purposes.
    
    Args:
        dp (list): 2D DP table
        text1 (str): First string
        text2 (str): Second string
    """
    # Print header
    print("    ", end="")
    print("  ", end="")
    for char in text2:
        print(f" {char} ", end="")
    print()
    
    # Print the table with row and column labels
    for i in range(len(dp)):
        if i == 0:
            print("  ", end="")
        else:
            print(f"{text1[i-1]} ", end="")
        
        for j in range(len(dp[0])):
            print(f" {dp[i][j]} ", end="")
        print()

# Example usage
if __name__ == "__main__":
    # Example 1
    s1 = "ABCBDAB"
    s2 = "BDCABA"
    
    result = longest_common_subsequence(s1, s2)
    print(f"String 1: {s1}")
    print(f"String 2: {s2}")
    print(f"Longest Common Subsequence: {result}")  # Output: "BCBA"
    print(f"Length of LCS: {lcs_length(s1, s2)}")  # Output: 4
    print(f"Length of LCS (space optimized): {lcs_optimized_space(s1, s2)}")  # Output: 4