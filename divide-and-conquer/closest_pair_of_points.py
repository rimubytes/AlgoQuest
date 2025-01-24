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
    """
    Find minimum distance among points in strip.
    
    Time Complexity: O(n), as inner loop runs at most 6 times
    """
    min_dist = d
    size = len(strip)
    
    for i in range(size):
        j = i + 1
        while j < size and (strip[j][1] - strip[i][1]) < min_dist:
            min_dist = min(min_dist, distance(strip[i], strip[j]))
            j += 1
    return min_dist

def closest_pair(points: List[Tuple[float, float]]) -> Tuple[float, List[Tuple[float, float]]]:
    # Sort points by x and y coordinates
    points_x = sorted(points, key=lambda p: p[0])
    points_y = sorted(points, key=lambda p: p[1])
    
    def closest_util(points_x: List[Tuple[float, float]], 
                    points_y: List[Tuple[float, float]], 
                    n: int) -> Tuple[float, List[Tuple[float, float]]]:
        if n <= 3:
            min_d = brute_force(points_x, n)
            closest = []
            for i in range(n):
                for j in range(i + 1, n):
                    if distance(points_x[i], points_x[j]) == min_d:
                        closest = [points_x[i], points_x[j]]
            return min_d, closest