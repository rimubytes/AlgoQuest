from typing import List, Tuple, Optional
import copy

class SudokuSolver:
    
    def __init__(self, board: List[List[int]]):
        self.board = board
        self.SIZE = 9
        self.BOX_SIZE = 3