"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 07: NP-Hard and NP-Complete Problems
Experiment: 0/1 Knapsack using Branch and Bound (LCBB)

Problem Statement:
Solve the 0/1 Knapsack problem using Least-Cost / Best-First Branch and Bound (LCBB).
Nodes in the state-space tree are prioritized using an optimistic upper bound
calculated via Fractional Knapsack.
Branches whose upper bound cannot exceed the best currently known feasible solution
are pruned immediately.
"""

import heapq

class Item:
    def __init__(self, idx, value, weight):
        self.idx = idx
        self.value = value
        self.weight = weight
        self.ratio = value / weight


class Node:
    def __init__(self, level, profit, weight, bound, items_taken):
        self.level = level          # Item index being considered (0..n-1)
        self.profit = profit        # Accumulated integer profit
        self.weight = weight        # Accumulated integer weight
        self.bound = bound          # Optimistic fractional upper bound
        self.items_taken = items_taken

    def __lt__(self, other):
        # Priority Queue max-heap: highest bound has highest priority
        return self.bound > other.bound


def calculate_upper_bound(node, n, capacity, items):
    """
    Computes upper bound on profit using Fractional Knapsack on remaining capacity.
    """
    if node.weight >= capacity:
        return 0.0
        
    profit_bound = float(node.profit)
    tot_weight = node.weight
    j = node.level + 1
    
    # Greedily pack whole items
    while j < n and tot_weight + items[j].weight <= capacity:
        tot_weight += items[j].weight
        profit_bound += items[j].value
        j += 1
        
    # Include fractional part of next item if capacity remains
    if j < n:
        profit_bound += (capacity - tot_weight) * items[j].ratio
        
    return profit_bound


def knapsack_branch_and_bound(values, weights, capacity):
    """
    Solves 0/1 Knapsack using Best-First Branch and Bound.
    
    Returns:
        tuple: (max_profit, best_items, nodes_expanded, nodes_pruned)
    """
    n = len(values)
    items = [Item(i, values[i], weights[i]) for i in range(n)]
    # Sort items by value-to-weight ratio descending
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    pq = []
    
    # Root node (level -1: no items considered yet)
    root = Node(level=-1, profit=0, weight=0, bound=0.0, items_taken=[])
    root.bound = calculate_upper_bound(root, n, capacity, items)
    
    heapq.heappush(pq, root)
    
    max_profit = 0
    best_selection = []
    nodes_expanded = 0
    nodes_pruned = 0
    
    while pq:
        curr = heapq.heappop(pq)
        nodes_expanded += 1
        
        # If upper bound is strictly less than best known profit, prune it
        if curr.bound <= max_profit:
            nodes_pruned += 1
            continue
            
        next_level = curr.level + 1
        if next_level >= n:
            continue
            
        next_item = items[next_level]
        
        # --- Child 1: Include item next_level ---
        w_inc = curr.weight + next_item.weight
        p_inc = curr.profit + next_item.value
        
        if w_inc <= capacity:
            if p_inc > max_profit:
                max_profit = p_inc
                best_selection = curr.items_taken + [next_item.idx]
                
            inc_node = Node(level=next_level, profit=p_inc, weight=w_inc, bound=0.0,
                            items_taken=curr.items_taken + [next_item.idx])
            inc_node.bound = calculate_upper_bound(inc_node, n, capacity, items)
            
            if inc_node.bound > max_profit:
                heapq.heappush(pq, inc_node)
            else:
                nodes_pruned += 1
                
        # --- Child 2: Exclude item next_level ---
        exc_node = Node(level=next_level, profit=curr.profit, weight=curr.weight, bound=0.0,
                        items_taken=list(curr.items_taken))
        exc_node.bound = calculate_upper_bound(exc_node, n, capacity, items)
        
        if exc_node.bound > max_profit:
            heapq.heappush(pq, exc_node)
        else:
            nodes_pruned += 1
            
    best_selection.sort()
    return max_profit, best_selection, nodes_expanded, nodes_pruned


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 7 - 0/1 KNAPSACK (BRANCH AND BOUND / LCBB)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    item_names = ["Item A", "Item B", "Item C", "Item D", "Item E"]
    values = [40, 50, 100, 95, 30]
    weights = [2, 3.14, 5, 5, 2]
    # Use integers for weight:
    weights = [2, 3, 5, 5, 2]
    capacity = 10
    
    print(f"Knapsack Total Capacity (W): {capacity} kg")
    print("Available Inventory:")
    for i in range(len(values)):
        print(f"  {item_names[i]}: Value = ${values[i]}, Weight = {weights[i]} kg, Ratio = {values[i]/weights[i]:.2f}")
        
    max_p, best_items, expanded, pruned = knapsack_branch_and_bound(values, weights, capacity)
    
    print("\n--- Branch and Bound Execution Summary ---")
    print(f"  Nodes Expanded from Priority Queue: {expanded}")
    print(f"  Branches Pruned by Upper Bounding : {pruned}")
    print(f"  Total Tree States Generated       : {expanded + pruned}")
    print(f"  Maximum Achieved Profit           : ${max_p}")
    
    print("\nOptimal Item Selection:")
    tot_w = 0
    for idx in best_items:
        print(f"  Packed: {item_names[idx]} (Weight: {weights[idx]} kg, Value: ${values[idx]})")
        tot_w += weights[idx]
        
    print(f"Total Packed Weight: {tot_w} / {capacity} kg")
    print("=" * 70)


if __name__ == "__main__":
    main()
