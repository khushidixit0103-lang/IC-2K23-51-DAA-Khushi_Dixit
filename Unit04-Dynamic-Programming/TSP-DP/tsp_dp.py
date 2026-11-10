"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 04: Dynamic Programming
Experiment: Travelling Salesperson Problem (TSP) using Held-Karp Dynamic Programming

Problem Statement:
Given N cities and a distance matrix representing pairwise travel costs, find the
minimum-cost Hamiltonian cycle visiting every city exactly once and returning to the origin.
Uses the Held-Karp algorithm with bitmask state representation:
    C(S, j) = min_{i in S, i != j} { C(S - {j}, i) + dist(i, j) }
Reduces time complexity from O(n!) brute-force to O(n^2 * 2^n) dynamic programming.
"""

def tsp_held_karp(distance_matrix):
    """
    Solves TSP using the Held-Karp DP algorithm with bitmasking.
    
    Parameters:
        distance_matrix (list of lists): N x N distance matrix.
        
    Returns:
        tuple: (min_tour_cost, tour_sequence)
    """
    n = len(distance_matrix)
    INF = float("inf")
    
    # Memoization table: memo[(mask, curr)] = min_cost
    # parent table: parent[(mask, curr)] = previous_city
    memo = {}
    parent = {}
    
    # Base case: Starting at city 0 with mask containing only city 0 (1 << 0 = 1)
    # memo[(mask, curr)]: min cost to visit set of cities in 'mask' ending at 'curr'
    memo[(1, 0)] = 0
    
    # Iterate through all subset sizes from 2 to n
    for size in range(2, n + 1):
        # Generate all masks with 'size' bits set and bit 0 always set
        for mask in range(1 << n):
            if bin(mask).count("1") != size:
                continue
            if not (mask & 1):  # City 0 must be included
                continue
                
            for j in range(1, n):
                if not (mask & (1 << j)):
                    continue
                prev_mask = mask ^ (1 << j)
                
                min_cost = INF
                best_prev = -1
                
                for i in range(n):
                    if i != j and (prev_mask & (1 << i)):
                        cost_via_i = memo.get((prev_mask, i), INF) + distance_matrix[i][j]
                        if cost_via_i < min_cost:
                            min_cost = cost_via_i
                            best_prev = i
                            
                memo[(mask, j)] = min_cost
                parent[(mask, j)] = best_prev
                
    # Complete the tour by returning to origin (city 0)
    final_mask = (1 << n) - 1
    min_tour_cost = INF
    last_city = -1
    
    for j in range(1, n):
        cost_to_origin = memo.get((final_mask, j), INF) + distance_matrix[j][0]
        if cost_to_origin < min_tour_cost:
            min_tour_cost = cost_to_origin
            last_city = j
            
    # Reconstruct tour backwards
    tour = [0]
    curr_mask = final_mask
    curr_city = last_city
    rev_tour = []
    
    while curr_city != 0 and curr_city != -1:
        rev_tour.append(curr_city)
        prev_city = parent.get((curr_mask, curr_city), 0)
        curr_mask = curr_mask ^ (1 << curr_city)
        curr_city = prev_city
        
    rev_tour.reverse()
    tour.extend(rev_tour)
    tour.append(0)  # Return to origin
    
    return min_tour_cost, tour


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 4 - TSP USING DYNAMIC PROGRAMMING (HELD-KARP)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    city_names = ["City 0", "City 1", "City 2", "City 3"]
    n = len(city_names)
    
    # 4-city cost matrix
    dist_matrix = [
        [0,  10, 15, 20],
        [10,  0, 35, 25],
        [15, 35,  0, 30],
        [20, 25, 30,  0]
    ]
    
    print(f"Number of Cities (N): {n}")
    print("Distance Matrix:")
    for i, row in enumerate(dist_matrix):
        print(f"  {city_names[i]}: {row}")
        
    min_cost, tour = tsp_held_karp(dist_matrix)
    
    print("\n--- Optimal Hamiltonian Cycle ---")
    tour_str = " -> ".join(city_names[i] for i in tour)
    print(f"  Tour Sequence: {tour_str}")
    print(f"  Minimum Tour Cost: {min_cost}")
    
    # Step-by-step breakdown
    print("\nLeg-by-Leg Cost Breakdown:")
    for k in range(len(tour) - 1):
        u, v = tour[k], tour[k + 1]
        print(f"  {city_names[u]} -> {city_names[v]} : Cost = {dist_matrix[u][v]}")
        
    print("=" * 70)


if __name__ == "__main__":
    main()
