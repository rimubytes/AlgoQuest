from typing import List, Set, Dict, Optional
from collections import defaultdict

class Graph:
    
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.graph = defaultdict(list)