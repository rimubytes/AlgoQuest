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

        self.board = board
        self.SIZE = 9
        self.BOX_SIZE = 3