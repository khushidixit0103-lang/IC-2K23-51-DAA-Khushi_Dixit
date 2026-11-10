"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 06: Backtracking
Experiment: Sum of Subsets using Backtracking

Problem Statement:
Given a set of n positive integers W = {w1, w2, ..., wn} and a target sum M,
find all subsets whose elements sum to exactly M.
Uses a state-space binary tree with two powerful bounding functions:
1. Upper bound pruning: current_sum + w[k] > M
2. Lower bound pruning: current_sum + remaining_sum < M
"""

def sum_of_subsets(weights, target_sum):
    """
    Finds all subsets of 'weights' that sum to 'target_sum'.
    
    Returns:
        tuple: (solutions, nodes_explored)
    """
    # Sort weights in ascending order to enable early pruning
    sorted_weights = sorted(weights)
    n = len(sorted_weights)
    solutions = []
    nodes_explored = [0]
    
    # Precompute total remaining sum
    total_remaining = sum(sorted_weights)
    
    # Path tracking: current_subset contains included elements
    current_subset = []
    
    def backtrack(idx, current_sum, remaining):
        nodes_explored[0] += 1
        
        # Goal check
        if current_sum == target_sum:
            solutions.append(list(current_subset))
            return
            
        if idx >= n:
            return
            
        # Branch 1: Include sorted_weights[idx]
        w = sorted_weights[idx]
        if current_sum + w <= target_sum:
            # Bounding condition check
            if current_sum + w + (remaining - w) >= target_sum:
                current_subset.append(w)
                backtrack(idx + 1, current_sum + w, remaining - w)
                current_subset.pop()  # Backtrack
                
        # Branch 2: Exclude sorted_weights[idx]
        # Bounding condition: only explore if remaining elements can reach target
        if current_sum + (remaining - w) >= target_sum:
            backtrack(idx + 1, current_sum, remaining - w)
            
    backtrack(0, 0, total_remaining)
    return solutions, nodes_explored[0], sorted_weights


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 6 - SUM OF SUBSETS (BACKTRACKING)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    # Test dataset
    weights = [5, 10, 12, 13, 15, 18]
    target_sum = 30
    
    print(f"Given Set of Numbers: {weights}")
    print(f"Target Sum (M)      : {target_sum}\n")
    
    solutions, nodes, sorted_w = sum_of_subsets(weights, target_sum)
    
    print(f"Sorted Set for Optimal Pruning: {sorted_w}")
    print(f"Total Theoretical Subsets (2^N): {2**len(weights)}")
    print(f"State-Space Tree Nodes Explored : {nodes}")
    print(f"Number of Valid Subsets Found   : {len(solutions)}\n")
    
    print("--- Discovered Subsets with Sum = 30 ---")
    for idx, sol in enumerate(solutions, 1):
        sol_str = " + ".join(str(x) for x in sol)
        print(f"  Subset {idx}: {{{', '.join(str(x) for x in sol)}}} -> {sol_str} = {sum(sol)}")
        
    print("=" * 70)


if __name__ == "__main__":
    main()
