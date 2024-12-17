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
    