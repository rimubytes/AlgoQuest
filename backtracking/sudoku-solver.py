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