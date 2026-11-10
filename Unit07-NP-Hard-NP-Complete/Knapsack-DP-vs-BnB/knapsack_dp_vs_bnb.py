"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 07: NP-Hard and NP-Complete Problems
Experiment: Knapsack DP vs Branch and Bound Comparative Performance Analysis

Description:
Empirically benchmarks 0/1 Knapsack using Dynamic Programming (Tabulation)
versus Branch and Bound (LCBB with Fractional Knapsack Upper Bound).
Tests varying item counts (N = 10 to 40) and evaluates execution times,
memory footprint, and states explored.
Logs results to CSV and generates comparison plots using Matplotlib.
"""

import os
import sys
import time
import random
import heapq
import csv

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- 1. Dynamic Programming 0/1 Knapsack ---
def dp_knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        v = values[i - 1]
        w = weights[i - 1]
        for c in range(capacity + 1):
            if w <= c:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - w] + v)
            else:
                dp[i][c] = dp[i - 1][c]
    return dp[n][capacity], (n + 1) * (capacity + 1)

# --- 2. Branch and Bound 0/1 Knapsack ---
class Item:
    def __init__(self, idx, value, weight):
        self.idx = idx
        self.value = value
        self.weight = weight
        self.ratio = value / weight

class BnBNode:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound

    def __lt__(self, other):
        return self.bound > other.bound

def calc_bound(node, n, capacity, items):
    if node.weight >= capacity:
        return 0.0
    p_bound = float(node.profit)
    tot_w = node.weight
    j = node.level + 1
    while j < n and tot_w + items[j].weight <= capacity:
        tot_w += items[j].weight
        p_bound += items[j].value
        j += 1
    if j < n:
        p_bound += (capacity - tot_w) * items[j].ratio
    return p_bound

def bnb_knapsack(values, weights, capacity):
    n = len(values)
    items = [Item(i, values[i], weights[i]) for i in range(n)]
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    pq = []
    root = BnBNode(-1, 0, 0, 0.0)
    root.bound = calc_bound(root, n, capacity, items)
    heapq.heappush(pq, root)
    
    max_p = 0
    states_explored = 0
    
    while pq:
        curr = heapq.heappop(pq)
        states_explored += 1
        
        if curr.bound <= max_p:
            continue
            
        next_lvl = curr.level + 1
        if next_lvl >= n:
            continue
            
        it = items[next_lvl]
        
        # Include
        w_inc = curr.weight + it.weight
        p_inc = curr.profit + it.value
        if w_inc <= capacity:
            if p_inc > max_p:
                max_p = p_inc
            c1 = BnBNode(next_lvl, p_inc, w_inc, 0.0)
            c1.bound = calc_bound(c1, n, capacity, items)
            if c1.bound > max_p:
                heapq.heappush(pq, c1)
                
        # Exclude
        c2 = BnBNode(next_lvl, curr.profit, curr.weight, 0.0)
        c2.bound = calc_bound(c2, n, capacity, items)
        if c2.bound > max_p:
            heapq.heappush(pq, c2)
            
    return max_p, states_explored


def benchmark():
    print("=" * 75)
    print("  IC-709 B: UNIT 7 - KNAPSACK: DP VS BRANCH AND BOUND BENCHMARK")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 75)

    item_sizes = [10, 15, 20, 25, 30, 35]
    results = []

    print(f"{'N':<5} | {'Capacity':<10} | {'DP Profit':<10} | {'BnB Profit':<11} | {'DP Time (ms)':<14} | {'BnB Time (ms)':<14} | {'BnB States':<12}")
    print("-" * 85)

    for n in item_sizes:
        random.seed(50 + n)
        weights = [random.randint(5, 50) for _ in range(n)]
        values = [random.randint(10, 100) for _ in range(n)]
        cap = sum(weights) // 2

        # DP
        t0 = time.perf_counter()
        p_dp, dp_cells = dp_knapsack(values, weights, cap)
        t_dp = (time.perf_counter() - t0) * 1000.0

        # BnB
        t0 = time.perf_counter()
        p_bnb, bnb_states = bnb_knapsack(values, weights, cap)
        t_bnb = (time.perf_counter() - t0) * 1000.0

        assert p_dp == p_bnb, f"Mismatch at N={n}"

        results.append({
            "N": n,
            "capacity": cap,
            "profit": p_dp,
            "dp_ms": round(t_dp, 4),
            "bnb_ms": round(t_bnb, 4),
            "dp_cells": dp_cells,
            "bnb_states": bnb_states
        })

        print(f"{n:<5} | {cap:<10} | {p_dp:<10} | {p_bnb:<11} | {t_dp:<14.3f} | {t_bnb:<14.3f} | {bnb_states:<12}")

    # Save to CSV
    script_dir = os.path.dirname(os.path.abspath(__file__))
    docs_dir = os.path.join(script_dir, "..", "..", "docs", "performance-analysis")
    os.makedirs(docs_dir, exist_ok=True)

    csv_local = os.path.join(script_dir, "results.csv")
    csv_docs = os.path.join(docs_dir, "unit07_knapsack_dp_vs_bnb.csv")

    for path in [csv_local, csv_docs]:
        with open(path, "w", newline="", encoding="ascii") as f:
            writer = csv.DictWriter(f, fieldnames=["N", "capacity", "profit", "dp_ms", "bnb_ms", "dp_cells", "bnb_states"])
            writer.writeheader()
            writer.writerows(results)

    print(f"\n[INFO] CSV saved to: {csv_local}")
    print(f"[INFO] CSV saved to: {csv_docs}")

    # Plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    ns = [r["N"] for r in results]
    dp_t = [r["dp_ms"] for r in results]
    bnb_t = [r["bnb_ms"] for r in results]
    dp_cells = [r["dp_cells"] for r in results]
    bnb_states = [r["bnb_states"] for r in results]

    # Plot 1: Runtime
    ax1.plot(ns, dp_t, marker='o', color='#1f77b4', linewidth=2, label='Dynamic Programming (O(N*W))')
    ax1.plot(ns, bnb_t, marker='s', color='#2ca02c', linewidth=2, label='Branch and Bound (LCBB)')
    ax1.set_title('Execution Time Comparison (ms)', fontsize=11, fontweight='bold')
    ax1.set_xlabel('Number of Items (N)', fontsize=10)
    ax1.set_ylabel('Execution Time (milliseconds)', fontsize=10)
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend()

    # Plot 2: States / Memory Units
    ax2.plot(ns, dp_cells, marker='o', color='#1f77b4', linewidth=2, label='DP Matrix Cells Evaluated')
    ax2.plot(ns, bnb_states, marker='s', color='#2ca02c', linewidth=2, label='BnB Nodes Explored')
    ax2.set_yscale('log')
    ax2.set_title('Memory / States Explored (Log Scale)', fontsize=11, fontweight='bold')
    ax2.set_xlabel('Number of Items (N)', fontsize=10)
    ax2.set_ylabel('States / Table Cells (log scale)', fontsize=10)
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend()

    plt.suptitle('Unit 07: 0/1 Knapsack - Dynamic Programming vs Branch and Bound\nStudent: Khushi Dixit (Roll No: IC-2K23-51)', fontsize=12, fontweight='bold')
    plt.tight_layout()

    plot_local = os.path.join(script_dir, "knapsack_dp_vs_bnb.png")
    plot_docs = os.path.join(docs_dir, "unit07_knapsack_dp_vs_bnb_plot.png")

    fig.savefig(plot_local, dpi=300)
    fig.savefig(plot_docs, dpi=300)
    plt.close(fig)

    print(f"[INFO] Plot saved to: {plot_local}")
    print(f"[INFO] Plot saved to: {plot_docs}")
    print("=" * 75)


if __name__ == "__main__":
    benchmark()
