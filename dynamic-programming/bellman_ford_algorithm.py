from typing import List, Dict, Tuple, Optional
from math import inf

class Graph:

    def __init__(self, vertices: int):

        self.vertices = vertices
        self.edges: List[Tuple[int, int, float]] = []