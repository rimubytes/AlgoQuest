from typing import List, Tuple
import math

def distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force(points: List[Tuple[float, float]], n: int) -> float:
    """Find minimum distance between points using brute force."""
    min_dist = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            min_dist = min(min_dist, distance(points[i], points[j]))
    return min_dist

def strip_closest(strip: List[Tuple[float, float]], d: float) -> float:

    min_dist = d
    size = len(strip)
    
    for i in range(size):
        j = i + 1
        while j < size and (strip[j][1] - strip[i][1]) < min_dist:
            min_dist = min(min_dist, distance(strip[i], strip[j]))
            j += 1
    return min_dist