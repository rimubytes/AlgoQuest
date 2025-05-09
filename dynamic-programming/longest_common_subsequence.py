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