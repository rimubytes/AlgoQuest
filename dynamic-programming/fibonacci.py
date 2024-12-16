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

    @staticmethod
    def space_optimized_tabulation(n):
        """
        Space-Optimized Bottom-up Dynamic Programming
        
        Args:
            n (int): Index of Fibonacci number to calculate
        
        Returns:
            int: Fibonacci number at index n
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Handle base cases
        if n <= 1:
            return n
        
        # Use only two variables instead of entire DP table
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b

    @staticmethod
    def generate_fibonacci_sequence(limit):
        """
        Generate Fibonacci sequence using Dynamic Programming
        
        Args:
            limit (int): Number of Fibonacci numbers to generate
        
        Returns:
            list: Fibonacci sequence
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if limit <= 0:
            return []
        
        # Initialize DP table
        dp = [0] * limit
        
        # Set base cases
        if limit > 1:
            dp[1] = 1
        
        # Generate sequence
        for i in range(2, limit):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp

def main():
    """Demonstration of Dynamic Programming Fibonacci Approaches"""
    # Test different methods
    print("Memoization Method:")
    for i in range(10):
        print(f"F({i}) = {FibonacciDP.memoization(i)}")
    
    print("\nTabulation Method:")
    for i in range(10):
        print(f"F({i}) = {FibonacciDP.tabulation(i)}")
    
    print("\nSpace-Optimized Tabulation:")
    for i in range(10):
        print(f"F({i}) = {FibonacciDP.space_optimized_tabulation(i)}")
    
    print("\nFibonacci Sequence Generation:")
    sequence = FibonacciDP.generate_fibonacci_sequence(10)
    print(sequence)

if __name__ == "__main__":
    main()
