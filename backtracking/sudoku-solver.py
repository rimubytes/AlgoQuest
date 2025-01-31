from typing import List, Tuple, Optional
import copy

class SudokuSolver:
    """
    A class to solve Sudoku puzzles using backtracking algorithm.
    
    The solver uses a depth-first search approach with backtracking
    to try different numbers in empty cells until a valid solution
    is found or all possibilities are exhausted.
    """
    
    def __init__(self, board: List[List[int]]):
        """
        Initialize the solver with a 9x9 Sudoku board.
        
        Args:
            board: 9x9 list of lists representing the Sudoku puzzle
                  0 represents empty cells
        """
        self.board = board
        self.SIZE = 9
        self.BOX_SIZE = 3

    def solve(self) -> bool:
        """
        Solve the Sudoku puzzle using backtracking.
        
        Time Complexity: O(9^(n*n)) where n is the board size
        Space Complexity: O(n*n) for recursion stack
        
        Returns:
            bool: True if solution exists, False otherwise
        """
        empty = self.find_empty()
        if not empty:
            return True
            
        row, col = empty
        
        for num in range(1, self.SIZE + 1):
            if self.is_valid(num, row, col):
                # Try placing this number
                self.board[row][col] = num
                
                # Recursively try to solve the rest
                if self.solve():
                    return True
                
                # If placing the number didn't lead to a solution,
                # backtrack by removing it
                self.board[row][col] = 0
                
        return False

    def find_empty(self) -> Optional[Tuple[int, int]]:
        """Find an empty cell in the board."""
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.board[i][j] == 0:
                    return (i, j)
        return None
    
    def is_valid(self, num: int, row: int, col: int) -> bool:

        # Check row
        for j in range(self.SIZE):
            if self.board[row][j] == num and col != j:
                return False

        # Check column
        for i in range(self.SIZE):
            if self.board[i][col] == num and row != i:
                return False

        # Check 3x3 box
        box_row = row - row % self.BOX_SIZE
        box_col = col - col % self.BOX_SIZE
        
        for i in range(self.BOX_SIZE):
            for j in range(self.BOX_SIZE):
                if (self.board[box_row + i][box_col + j] == num and
                    (box_row + i != row or box_col + j != col)):
                    return False
                    
        return True