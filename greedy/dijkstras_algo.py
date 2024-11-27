# Dijkstra's algorithm used to find the shortest path between nodes in a graph
# with non-negative edge weights.
# Core Purpose:
#   - Finds shortest paths from a starting node to all other nodes
#   - Works on weighted graphs
#   - Guarantees optimal path calculation
    
import heapq # represents a priority queue
from typing import Dict, List, Tuple

def dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> Tuple[Dict[str, int], Dict[str, str]]:
    """
    Implements Djikstra's shortest path algorithm

    Parameters:
    graph (Dict): Adjacency list representing the graph
    start (str): Starting node

    Returns:
    Tuple of distances and previous nodes dictionary

    Time Complexity: O((V +E ) log V)
    Space Complexity: O(V)
    """
    # Initialize distances and previous nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}

    # Priority queue to track minimum distances
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip if we've found a shorter path
        if current_distance > distances[current_node]:
            continue

        # Check all neighboring nodes
        for neighbor, weight in graph [current_node].items():
            distance = current_distance + weight

            # Update if a shorter path is found
            if distance < distance[neighbor]:
                distance[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distance, previous

