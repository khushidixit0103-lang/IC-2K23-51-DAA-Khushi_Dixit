"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 07: NP-Hard and NP-Complete Problems
Experiment: Exhaustive Search on NP-Hard Problems

Problem Statement:
Implement and analyze pure Exhaustive Search (Brute-Force Enumeration) on canonical
NP-Hard combinatorial problems (Exact Subset Sum / 0-1 Knapsack).
Demonstrates the combinatorial explosion of the search space (2^N states),
verifying the boundaries of polynomial-time computability (P vs NP).
"""

import time
import itertools

def exhaustive_subset_sum(weights, target):
    """
    Exhaustively tests all 2^n binary candidate combinations.
    """
    n = len(weights)
    valid_subsets = []
    total_states_examined = 0
    
    for r in range(n + 1):
        for combo in itertools.combinations(weights, r):
            total_states_examined += 1
            if sum(combo) == target:
                valid_subsets.append(combo)
                
    return valid_subsets, total_states_examined


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 7 - EXHAUSTIVE SEARCH (NP-HARD EXPLOSION)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    weights = [3, 7, 11, 14, 18, 21, 25, 29]
    target = 43
    
    print(f"Given Set of Numbers: {weights}")
    print(f"Set Cardinality (N) : {len(weights)}")
    print(f"Target Sum (M)      : {target}\n")
    
    t0 = time.perf_counter()
    sols, states = exhaustive_subset_sum(weights, target)
    dt = (time.perf_counter() - t0) * 1000.0
    
    print(f"Total Candidate States Evaluated (2^N): {states}")
    print(f"Valid Subsets Found                  : {len(sols)}")
    print(f"Execution Time                       : {dt:.4f} ms\n")
    
    print("Discovered Exact Solutions:")
    for idx, s in enumerate(sols, 1):
        print(f"  Solution {idx}: {s} -> Sum = {sum(s)}")
        
    print("\n--- Theoretical Combinatorial Explosion Projection (2^N) ---")
    print(f"{'N':<5} | {'Search Space (2^N)':<25} | {'Projected Time @ 10^7 states/sec':<35}")
    print("-" * 70)
    projections = [10, 20, 30, 40, 50, 60]
    for n in projections:
        states_count = 2 ** n
        sec = states_count / 1e7
        if sec < 60:
            time_str = f"{sec:.4f} seconds"
        elif sec < 3600:
            time_str = f"{sec / 60:.2f} minutes"
        elif sec < 86400:
            time_str = f"{sec / 3600:.2f} hours"
        elif sec < 31536000:
            time_str = f"{sec / 86400:.2f} days"
        else:
            time_str = f"{sec / 31536000:.2e} years"
        print(f"{n:<5} | {states_count:<25} | {time_str:<35}")
        
    print("=" * 70)


if __name__ == "__main__":
    main()
