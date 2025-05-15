# Mastering Algorithms One Step at a Time

A repository dedicated to mastering algorithms through hands-on practice. This project breaks down various algorithms into classes, starting from the basics and progressing to more advanced techniques. Each section introduces a class of algorithms, providing an overview of its approach, typical use cases, and a checklist to track progress as you implement them.

## Project Overview

The goal of this repository is to:

- Gain a deep understanding of algorithmic techniques and their applications.
- Implement each algorithm from scratch to solidify problem-solving skills.
- Document insights and challenges faced while solving each problem.
  
You'll find algorithms divided into categories such as Divide and Conquer, Greedy Algorithms, Dynamic Programming, Backtracking, and more. Each section includes a brief description of the category followed by a checklist to track your learning.

## Algorithm Categories

### 1. **Divide and Conquer Algorithms**

Divide and Conquer is a technique where a problem is divided into smaller sub-problems, each of which is solved independently before combining the results. These algorithms are often recursive and are especially useful for problems that can be broken down into smaller, similar sub-problems.
Common use cases: Sorting, searching, and geometric problems.
  
**Algorithms to Implement:**

- [x] Merge Sort
- [x] Quick Sort
- [x] Binary Search
- [x] Closest Pair of Points

---

### 2. **Greedy Algorithms**

Greedy algorithms make a series of choices, each of which looks the best at that moment (locally optimal), with the hope of finding the overall best (globally optimal) solution. They are faster but may not always lead to the optimal solution.
Common use cases: Optimization problems like shortest paths and spanning trees.
  
**Algorithms to Implement:**

- [x] Dijkstra's Algorithm (Shortest Path)
- [x] Prim's Algorithm (Minimum Spanning Tree)
- [ ] Kruskal's Algorithm (Minimum Spanning Tree)
- [ ] Huffman Coding
- [ ] Fractional Knapsack

---

### 3. **Dynamic Programming (DP)**

Dynamic Programming is used to solve problems by breaking them down into overlapping sub-problems and storing the results of these sub-problems to avoid redundant work. This technique is particularly powerful for optimization problems where decisions need to be made sequentially.
Common use cases: Sequence alignment, knapsack problem, and pathfinding.
  
**Algorithms to Implement:**

- [x] Fibonacci Sequence
- [x] Longest Common Subsequence
- [ ] 0/1 Knapsack Problem
- [x] Bellman-Ford Algorithm (Shortest Path)
- [ ] Coin Change Problem

---

### 4. **Backtracking Algorithms**

Backtracking is a technique used to solve constraint satisfaction problems by incrementally building a solution and abandoning (backtracking) if it doesn’t meet the constraints. It's a brute-force algorithmic approach with pruning.
Common use cases: Puzzles like Sudoku, and combinatorial problems.
  
**Algorithms to Implement:**

- [x] N-Queens Problem
- [x] Sudoku Solver
- [ ] Hamiltonian Path Problem
- [ ] Subset Sum Problem

---

### 5. **Branch and Bound Algorithms**

Branch and Bound is an optimization technique similar to backtracking but focuses on exploring the most promising branches first, while using bounds to eliminate others. It is often used to find optimal solutions to NP-hard problems.
Common use cases: Knapsack problems and combinatorial optimization.
  
**Algorithms to Implement:**

- [ ] Traveling Salesman Problem (TSP)
- [ ] 0/1 Knapsack Problem (Branch and Bound)

---

### 6. **Graph Algorithms**

Graph algorithms operate on data structures made up of nodes and edges, solving problems like finding the shortest path, detecting cycles, and more. Graph theory forms the foundation for much of modern networking and data structure design.
Common use cases: Pathfinding, scheduling, and network flow.
  
**Algorithms to Implement:**

- [x] Breadth-First Search (BFS)
- [x] Depth-First Search (DFS)
- [ ] Floyd-Warshall Algorithm (All-Pairs Shortest Paths)
- [ ] Topological Sort
- [ ] A* Algorithm

---

### 7. **Sorting Algorithms**

Sorting algorithms are fundamental and deal with arranging data in a particular order. They are essential for optimizing other algorithms that require sorted data (like search algorithms) and are a key aspect of computer science.
Common use cases: Data analysis, searching, and preprocessing.
  
**Algorithms to Implement:**

- [x] Bubble Sort
- [x] Selection Sort
- [x] Insertion Sort
- [x] Heap Sort
- [ ] Merge Sort
- [ ] Quick Sort

---

### 8. **Search Algorithms**

Search algorithms are used to find specific data within a data structure. Whether searching in linear or non-linear data structures, they are key for applications ranging from databases to artificial intelligence.
Common use cases: Searching elements in a list or tree.
  
**Algorithms to Implement:**

- [x] Linear Search
- [x] Binary Search
- [x] Depth-First Search (DFS)
- [ ] Breadth-First Search (BFS)

---

### 9. **Mathematical Algorithms**

These algorithms are based on fundamental mathematical principles and are often used to solve number theory problems, perform calculations, or work with primes and factors.
Common use cases: Cryptography, number theory, and combinatorics.
  
**Algorithms to Implement:**

- [ ] Euclidean Algorithm (GCD)
- [ ] Sieve of Eratosthenes (Prime Numbers)
- [ ] Fast Fourier Transform (FFT)
- [ ] Exponentiation by Squaring

---

### 10. **String Algorithms**

String algorithms handle operations related to sequences of characters, like pattern matching and substring search. Efficient string manipulation is crucial in fields like computational biology and text processing.
Common use cases: Pattern matching, text analysis, and bioinformatics.
  
**Algorithms to Implement:**

- [ ] Knuth-Morris-Pratt (KMP) Pattern Matching
- [ ] Rabin-Karp Algorithm
- [ ] Z Algorithm (Pattern Matching)
- [ ] Longest Palindromic Substring

---

### 11. **Randomized Algorithms**

These algorithms use random choices during execution to provide solutions, often simplifying complex problems. They are particularly useful when deterministic algorithms are too slow or complicated.
Common use cases: Approximation problems and probabilistic data structures.
  
**Algorithms to Implement:**

- [ ] Randomized Quick Sort
- [ ] Monte Carlo Algorithm
- [ ] Las Vegas Algorithm
- [ ] Randomized Min-Cut Algorithm

---

### Progress Overview:

- [ ] Beginner Algorithms
- [ ] Intermediate Algorithms
- [ ] Advanced Algorithms

---

## How to Use This Repository

1. Pick an algorithm category that interests you.
2. Learn about the theory behind each algorithm.
3. Implement the algorithm from scratch in your language of choice.
4. Document challenges, insights, and optimizations in the `Notes` section.
5. Check off the algorithms as you complete them.

---

### Notes:

Document any challenges or insights you faced while solving the algorithms here.
