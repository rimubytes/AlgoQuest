def solve_n_queens(n: int) -> List[List[str]]:
    """
    Solves the N-Queens problem, finding all possible configurations 
    of N queens on an N×N chessboard without any queens attacking each other.
    
    Parameters:
    n (int): Size of the chessboard and number of queens
    
    Returns:
    List[List[str]]: All valid board configurations
    
    Time Complexity: O(N!)
    Space Complexity: O(N^2)
    """
    def create_board(state):
        """
        Converts the queen positions to a board representation.
        
        Parameters:
        state (List[int]): Column positions of queens
        
        Returns:
        List[str]: Visual representation of the board
        """
        board = []
        for row in range(n):
            # Create a row with '.' for empty and 'Q' for queen
            line = ['.' * state[row] + 'Q' + '.' * (n - state[row] - 1)]
            board.append(line[0])
        return board

    def is_safe(state, row, col):
        """
        Checks if a queen can be placed at the given position without conflicts.
        
        Parameters:
        state (List[int]): Current queen positions
        row (int): Row to place the queen
        col (int): Column to place the queen
        
        Returns:
        bool: True if the position is safe, False otherwise
        """
        for prev_row in range(row):
            # Check column conflicts
            if state[prev_row] == col:
                return False
            
            # Check diagonal conflicts
            # Absolute difference in rows equals absolute difference in columns
            if abs(state[prev_row] - col) == abs(prev_row - row):
                return False
        
        return True
    
    def backtrack(row, state):
        """
        Recursive backtracking to find all valid N-Queens configurations.
        
        Parameters:
        row (int): Current row being processed
        state (List[int]): Current board state
        
        Returns:
        None, but populates solutions list
        """
        # Base case: all queens are placed
        if row == n:
            solutions.append(create_board(state))
            return
        
        # Try placing queen in each column of the current row
        for col in range(n):
            if is_safe(state, row, col):
                # Place queen and move to next row
                state[row] = col
                backtrack(row + 1, state)
    
    # Initialize solutions and board state
    solutions = []
    state = [0] * n
    
    # Start backtracking from the first row
    backtrack(0, state)
    
    return solutions

def print_solutions(solutions):
    """
    Prints all N-Queens solutions in a readable format.
    
    Parameters:
    solutions (List[List[str]]): List of board configurations
    """
    for i, solution in enumerate(solutions, 1):
        print(f"Solution {i}:")
        for row in solution:
            print(row)
        print()

# Demonstrate N-Queens solution
def demonstrate_n_queens():
    """
    Demonstrates N-Queens solution for different board sizes.
    """
    board_sizes = [4, 8]
    
    for size in board_sizes:
        print(f"\n{size}-Queens Problem Solutions:")
        solutions = solve_n_queens(size)
        print(f"Total Solutions: {len(solutions)}")
        
        # Print first two solutions if available
        if solutions:
            print_solutions(solutions[:2])

# Run demonstration
if __name__ == "__main__":
    demonstrate_n_queens()