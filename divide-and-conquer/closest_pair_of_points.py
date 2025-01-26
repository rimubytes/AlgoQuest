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
    """
    Find closest pair of points using Divide and Conquer.
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Args:
        points: List of (x, y) coordinates
        
    Returns:
        Tuple of minimum distance and list of closest points
    """
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

        mid = n // 2
        mid_point = points_x[mid]
        
        # Split points into left and right halves
        points_y_left = [p for p in points_y if p[0] <= mid_point[0]]
        points_y_right = [p for p in points_y if p[0] > mid_point[0]]
        
        # Recursively find minimum distances in left and right halves
        left_min, left_pair = closest_util(points_x[:mid], points_y_left, mid)
        right_min, right_pair = closest_util(points_x[mid:], points_y_right, n - mid)
        
        min_d = min(left_min, right_min)
        closest_pair = left_pair if left_min < right_min else right_pair
        
        # Create strip of points closer than min_d to the middle line
        strip = [p for p in points_y if abs(p[0] - mid_point[0]) < min_d]
        strip_min = strip_closest(strip, min_d)
        
        if strip_min < min_d:
            min_d = strip_min
            closest_pair = []
            for i in range(len(strip)):
                for j in range(i + 1, len(strip)):
                    if distance(strip[i], strip[j]) == min_d:
                        closest_pair = [strip[i], strip[j]]
        
        return min_d, closest_pair
    
    return closest_util(points_x, points_y, len(points))

def visualize_points(points: List[Tuple[float, float]], closest: List[Tuple[float, float]]) -> None:
    """Print visual representation of points and closest pair."""
    import matplotlib.pyplot as plt

    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]

    plt.scatter(x_coords, y_coords, color='blue', label='Points')
    if closest:
        closest_x = [p[0] for p in closest]
        closest_y = [p[1] for p in closest]
        plt.plot(closest_x, closest_y, 'r-', label='Closest Pair')