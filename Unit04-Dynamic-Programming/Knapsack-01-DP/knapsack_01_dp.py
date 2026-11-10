"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 04: Dynamic Programming
Experiment: 0/1 Knapsack using Dynamic Programming

Problem Statement:
Given N items, each with weight w_i and profit p_i, and a knapsack of capacity W.
Select a subset of items to maximize total profit such that total weight <= W.
Items cannot be divided (0/1 choice).
Solves via 2D Dynamic Programming table and reconstructs optimal item subset.
"""

def knapsack_01_dp(values, weights, capacity):
    """
    Computes optimal profit and selected items for 0/1 Knapsack.
    
    Returns:
        tuple: (max_profit, selected_indices, dp_table)
    """
    n = len(values)
    # DP table of dimensions (n + 1) x (capacity + 1)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build table bottom-up
    for i in range(1, n + 1):
        v = values[i - 1]
        w = weights[i - 1]
        for c in range(capacity + 1):
            if w <= c:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - w] + v)
            else:
                dp[i][c] = dp[i - 1][c]
                
    max_profit = dp[n][capacity]
    
    # Backtrack to find chosen items
    selected_indices = []
    curr_c = capacity
    for i in range(n, 0, -1):
        # If value differs from the cell above, item i-1 was included
        if dp[i][curr_c] != dp[i - 1][curr_c]:
            selected_indices.append(i - 1)
            curr_c -= weights[i - 1]
            
    selected_indices.reverse()
    return max_profit, selected_indices, dp


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 4 - 0/1 KNAPSACK (DYNAMIC PROGRAMMING)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    # Sample items
    item_names = ["Laptop", "Camera", "Drone", "Watch", "Tablet"]
    values = [500, 300, 400, 200, 150]
    weights = [3, 2, 4, 1, 2]
    capacity = 6
    
    print(f"Knapsack Total Capacity: W = {capacity} kg")
    print("Available Inventory:")
    for name, v, w in zip(item_names, values, weights):
        print(f"  {name:<10} | Value: ${v:<4} | Weight: {w} kg")
        
    max_profit, selected, dp = knapsack_01_dp(values, weights, capacity)
    
    print("\n--- DP Table (Rows: Items 0..N, Cols: Capacities 0..W) ---")
    header = "Cap: " + " ".join(f"{c:5d}" for c in range(capacity + 1))
    print(header)
    print("-" * len(header))
    for i in range(len(values) + 1):
        row_label = f"i={i}: "
        print(row_label + " ".join(f"{dp[i][c]:5d}" for c in range(capacity + 1)))
        
    print("\n--- Optimal Selection Result ---")
    total_w = 0
    total_v = 0
    for idx in selected:
        print(f"  Selected: {item_names[idx]:<10} (Weight: {weights[idx]} kg, Value: ${values[idx]})")
        total_w += weights[idx]
        total_v += values[idx]
        
    print("-" * 70)
    print(f"  Total Packed Weight : {total_w} / {capacity} kg")
    print(f"  Maximum Profit      : ${total_v}")
    print("=" * 70)


if __name__ == "__main__":
    main()
