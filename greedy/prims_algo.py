# Prim's ALgorithm is primarily used to solve the Minimum Spanning Tree (MST)
# A Minimum Spanning Tree is a subset of edges in a weighted graph that:
#       - Connects all vertices
#       - Has the minimum total weight
#       - Contains no cycles

import heapq
from typing import Dict, List, Tuple

def prims_algorithm(graph: Dict[str, Dict[str, int]]) -> List[Tuple[str, str, int]]:
    """
    Implements Prim's algorithm to find the Minimum Spanning Tree (MST).
    
    Parameters:
    graph (Dict): Adjacency list representing the weighted, undirected graph
    
    Returns:
    List of tuples representing edges in the Minimum Spanning Tree
    
    Time Complexity: O(E log V)
    Space Complexity: O(V + E)
    """
    # If graph is empty, return empty MST
    if not graph:
        return []
    
    # Start with an arbitrary node (first node in the graph)
    start_node = list(graph.keys())[0]
    
    # Track visited nodes and the minimum spanning tree
    visited = set([start_node])
    mst = []
    
    # Priority queue to store edges (weight, from_node, to_node)
    edges = [(weight, start_node, to_node) 
             for to_node, weight in graph[start_node].items()]
    heapq.heapify(edges)

    while edges:
        # Get the minimum weight edge
        weight, from_node, to_node = heapq.heappop(edges)

        # Skip if the destination node is already is the MST
        if to_node in visited:
            continue

        # Add the edge to the MST
        mst.append((from_node, to_node, weight))
        visited.add(to_node)

        # Add edges from the newly visited node
        for next_node, next_weight in graph[to_node].items():
            if next_node not in visited:
                heapq.heappush(edges, (next_weight, to_node, next_node))
    
    return mst

def total_mst_weight(mst: List[Tuple[str, str, int]]) -> int:
    """
    Calculate the total weight of the Minimum Spanning Tree.
    
    Parameters:
    mst (List): List of edges in the Minimum Spanning Tree
    
    Returns:
    Total weight of the MST
    """
    return sum(weight for _, _, weight in mst)