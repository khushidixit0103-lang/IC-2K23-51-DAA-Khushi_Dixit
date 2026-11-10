"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 07: NP-Hard and NP-Complete Problems
Experiment: Travelling Salesperson Problem (TSP) using Branch and Bound (Reduced Matrix Method)

Problem Statement:
Solve TSP using Least-Cost Branch and Bound (LCBB) with Matrix Reduction.
Computes a lower bound at each state-space node by:
1. Row reduction: Subtracting min element in each row.
2. Column reduction: Subtracting min element in each column.
Uses a Min-Heap priority queue to expand the most promising partial tour first.
"""

import heapq
import copy

INF = float("inf")

class TSPNode:
    def __init__(self, parent_matrix, level, path, cost, vertex):
        self.matrix = copy.deepcopy(parent_matrix)
        self.level = level          # Number of cities visited so far
        self.path = list(path)      # Sequence of cities visited
        self.cost = cost            # Accumulated lower bound cost
        self.vertex = vertex        # Current city index

    def __lt__(self, other):
        return self.cost < other.cost  # Min-Heap


def reduce_matrix(matrix, n):
    """
    Performs row and column reductions on matrix.
    Returns: reduction_cost
    """
    reduction_cost = 0
    
    # 1. Row reduction
    for i in range(n):
        min_row = min(matrix[i])
        if min_row != INF and min_row > 0:
            reduction_cost += min_row
            for j in range(n):
                if matrix[i][j] != INF:
                    matrix[i][j] -= min_row
                    
    # 2. Column reduction
    for j in range(n):
        min_col = min(matrix[i][j] for i in range(n))
        if min_col != INF and min_col > 0:
            reduction_cost += min_col
            for i in range(n):
                if matrix[i][j] != INF:
                    matrix[i][j] -= min_col
                    
    return reduction_cost


def solve_tsp_branch_and_bound(cost_matrix):
    """
    Solves TSP using LCBB with reduced matrices.
    
    Returns:
        tuple: (min_tour_cost, tour_path, nodes_expanded, nodes_pruned)
    """
    n = len(cost_matrix)
    initial_matrix = copy.deepcopy(cost_matrix)
    
    # Initial root reduction
    root_cost = reduce_matrix(initial_matrix, n)
    root = TSPNode(initial_matrix, level=0, path=[0], cost=root_cost, vertex=0)
    
    pq = []
    heapq.heappush(pq, root)
    
    min_tour_cost = INF
    optimal_path = []
    nodes_expanded = 0
    nodes_pruned = 0
    
    while pq:
        curr = heapq.heappop(pq)
        nodes_expanded += 1
        
        # Pruning check
        if curr.cost >= min_tour_cost:
            nodes_pruned += 1
            continue
            
        # Goal state reached: all n cities visited
        if curr.level == n - 1:
            # Add cost of return edge to start vertex (0)
            return_cost = cost_matrix[curr.vertex][0]
            if return_cost != INF:
                total_cost = curr.cost + curr.matrix[curr.vertex][0]
                # In reduced matrix, curr.matrix[curr.vertex][0] gives remaining cost
                if curr.cost < min_tour_cost:
                    min_tour_cost = curr.cost
                    optimal_path = curr.path + [0]
            continue
            
        # Branch to all unvisited cities
        for nxt in range(n):
            if nxt not in curr.path and cost_matrix[curr.vertex][nxt] != INF:
                child = TSPNode(curr.matrix, level=curr.level + 1,
                                path=curr.path + [nxt], cost=0, vertex=nxt)
                
                # Set outgoing row and incoming column to infinity
                for k in range(n):
                    child.matrix[curr.vertex][k] = INF
                    child.matrix[k][nxt] = INF
                # Prevent returning directly to 0 prematurely
                child.matrix[nxt][0] = INF
                
                # Calculate child lower bound:
                # parent_cost + edge_weight_in_parent_reduced_matrix + child_reduction
                r_cost = reduce_matrix(child.matrix, n)
                child.cost = curr.cost + curr.matrix[curr.vertex][nxt] + r_cost
                
                if child.cost < min_tour_cost:
                    heapq.heappush(pq, child)
                else:
                    nodes_pruned += 1
                    
    return min_tour_cost, optimal_path, nodes_expanded, nodes_pruned


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 7 - TSP (BRANCH AND BOUND / REDUCED MATRIX)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    city_names = ["City 0", "City 1", "City 2", "City 3", "City 4"]
    n = len(city_names)
    
    # 5-city cost matrix
    cost_matrix = [
        [INF, 20, 30, 10, 11],
        [15, INF, 16,  4,  2],
        [ 3,  5, INF,  2,  4],
        [19,  6, 18, INF,  3],
        [16,  4,  7, 16, INF]
    ]
    
    print(f"Number of Cities (N): {n}")
    print("Initial Cost Matrix:")
    for i in range(n):
        row_str = "  [" + ", ".join(f"{cost_matrix[i][j]:4}" if cost_matrix[i][j] != INF else " INF" for j in range(n)) + "]"
        print(row_str)
        
    min_cost, tour, expanded, pruned = solve_tsp_branch_and_bound(cost_matrix)
    
    print("\n--- Execution Metrics ---")
    print(f"  Nodes Expanded from Min-Heap: {expanded}")
    print(f"  Nodes Pruned by Lower Bound : {pruned}")
    print(f"  Total Tree States Generated : {expanded + pruned}")
    print(f"  Minimum Tour Cost           : {min_cost}")
    
    tour_str = " -> ".join(city_names[c] for c in tour)
    print(f"\nOptimal Hamiltonian Cycle Tour:")
    print(f"  {tour_str}")
    
    # Verify leg-by-leg cost sum
    actual_sum = 0
    print("\nTour Step Breakdown:")
    for k in range(len(tour) - 1):
        u, v = tour[k], tour[k + 1]
        c = cost_matrix[u][v]
        actual_sum += c
        print(f"  {city_names[u]} -> {city_names[v]} : {c}")
    print(f"Total Direct Cost Sum: {actual_sum}")
    print("=" * 70)


if __name__ == "__main__":
    main()
