"""
Fibonacci Sequence - Dynamic Programming Implementations

This module demonstrates two primary dynamic programming approaches:
1. Top-down Memoization (Recursive with Caching)
2. Bottom-up Tabulation (Iterative with DP Table)

Dynamic Programming Characteristics:
- Breaks complex problem into simpler subproblems
- Stores results to avoid redundant calculations
- Significantly improves time complexity from O(2^n) to O(n)
"""

class FibonacciDP:
    @staticmethod
    def memoization(n, memo=None):
        """
        Top-down Dynamic Programming (Memoization)
        
        Args:
            n (int): Index of Fibonacci number to calculate
            memo (dict, optional): Memoization cache
        
        Returns:
            int: Fibonacci number at index n
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Initialize memoization dictionary if not provided
        if memo is None:
            memo = {}
        
        # Check if result is already computed
        if n in memo:
            return memo[n]
        
        # Base cases
        if n <= 1:
            return n
        
        # Compute and memoize result
        memo[n] = FibonacciDP.memoization(n-1, memo) + FibonacciDP.memoization(n-2, memo)
        return memo[n]

    @staticmethod
    def tabulation(n):
        """
        Bottom-up Dynamic Programming (Tabulation)

        Args:
            n (int): Index of Fibonacci number to calculate

        Returns:
            int: Fibonacci number at indexn

        Time Complexity: 0(n)
        Space COmplexity: 0(n)
        """
        # Handle base cases
        if n <= 1:
            return n
        
        # Create DP table
        dp = [0] * (n + 1)
        dp[1] = 1
        
        # Build solution iteratively
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

        