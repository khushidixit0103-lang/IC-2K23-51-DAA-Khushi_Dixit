"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 04: Dynamic Programming
Experiment: Greedy vs Dynamic Programming for 0/1 Knapsack

Problem Statement:
Compare the Greedy strategy against Dynamic Programming on the 0/1 Knapsack problem.
Demonstrates:
1. Greedy fails on 0/1 Knapsack because local ratio heuristics cannot backtrack.
2. Dynamic Programming systematically searches overlapping subproblems to guarantee
   the globally optimal solution.
Generates comparative metrics, logs CSV, and plots optimality differences.
"""

import os
import sys
import time
import random
import csv

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def greedy_01_knapsack(values, weights, capacity):
    """Greedy heuristic: sort by ratio v/w, take whole items that fit."""
    n = len(values)
    items = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)
    
    total_val = 0
    total_wt = 0
    selected = []
    
    for i in items:
        if total_wt + weights[i] <= capacity:
            total_wt += weights[i]
            total_val += values[i]
            selected.append(i)
            
    return total_val, total_wt, selected


def dp_01_knapsack(values, weights, capacity):
    """Dynamic programming: exact optimal solution via bottom-up tabulation."""
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
                
    max_val = dp[n][capacity]
    
    # Backtrack
    curr_c = capacity
    selected = []
    for i in range(n, 0, -1):
        if dp[i][curr_c] != dp[i - 1][curr_c]:
            selected.append(i - 1)
            curr_c -= weights[i - 1]
            
    selected.reverse()
    total_wt = sum(weights[i] for i in selected)
    return max_val, total_wt, selected


def run_comparison():
    print("=" * 75)
    print("  IC-709 B: UNIT 4 - GREEDY VS DYNAMIC PROGRAMMING (0/1 KNAPSACK)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 75)
    
    # Classic counterexample where Greedy yields suboptimal results:
    # Item 1: v=60, w=10 (ratio 6.0)
    # Item 2: v=100, w=20 (ratio 5.0)
    # Item 3: v=120, w=30 (ratio 4.0)
    # Capacity: W = 50
    # Greedy picks Item 1 (w=10), Item 2 (w=20) -> wt=30, profit=160 (remaining capacity 20 cannot fit Item 3)
    # DP picks Item 2 (w=20) + Item 3 (w=30) -> wt=50, profit=220! (Optimality gap: +$60)
    
    demo_v = [60, 100, 120]
    demo_w = [10, 20, 30]
    demo_cap = 50
    
    g_val, g_wt, g_sel = greedy_01_knapsack(demo_v, demo_w, demo_cap)
    dp_val, dp_wt, dp_sel = dp_01_knapsack(demo_v, demo_w, demo_cap)
    
    print("\n--- Canonical Demonstration Case ---")
    print(f"Capacity W = {demo_cap}")
    print("Items: (v=60, w=10, r=6.0), (v=100, w=20, r=5.0), (v=120, w=30, r=4.0)")
    print(f"Greedy Result : Profit = ${g_val:<4} (Weight = {g_wt} kg, Items = {g_sel})")
    print(f"DP Result     : Profit = ${dp_val:<4} (Weight = {dp_wt} kg, Items = {dp_sel})")
    print(f"Optimality Gap: DP achieved ${dp_val - g_val} higher profit than Greedy (+{(dp_val - g_val)/g_val*100:.1f}%)")
    
    # Benchmark across multiple problem sizes
    benchmark_sizes = [10, 25, 50, 75, 100, 150]
    results = []
    
    print("\n--- Empirical Benchmark Across Problem Sizes ---")
    print(f"{'N':<6} | {'Capacity':<10} | {'Greedy Val':<12} | {'DP Val':<10} | {'Greedy (ms)':<14} | {'DP (ms)':<12} | {'Gap (%)':<8}")
    print("-" * 80)
    
    for n in benchmark_sizes:
        random.seed(100 + n)
        weights = [random.randint(5, 50) for _ in range(n)]
        values = [random.randint(10, 200) for _ in range(n)]
        cap = sum(weights) // 3
        
        t0 = time.perf_counter()
        for _ in range(10):
            gv, gw, _ = greedy_01_knapsack(values, weights, cap)
        t_greedy = (time.perf_counter() - t0) / 10 * 1000.0
        
        t0 = time.perf_counter()
        for _ in range(10):
            dpv, dpw, _ = dp_01_knapsack(values, weights, cap)
        t_dp = (time.perf_counter() - t0) / 10 * 1000.0
        
        gap_pct = ((dpv - gv) / dpv * 100.0) if dpv > 0 else 0.0
        
        results.append({
            "N": n,
            "capacity": cap,
            "greedy_val": gv,
            "dp_val": dpv,
            "greedy_ms": round(t_greedy, 4),
            "dp_ms": round(t_dp, 4),
            "gap_pct": round(gap_pct, 2)
        })
        
        print(f"{n:<6} | {cap:<10} | {gv:<12} | {dpv:<10} | {t_greedy:<14.4f} | {t_dp:<12.4f} | {gap_pct:<8.2f}%")
        
    # Save to CSV
    script_dir = os.path.dirname(os.path.abspath(__file__))
    docs_dir = os.path.join(script_dir, "..", "..", "docs", "performance-analysis")
    os.makedirs(docs_dir, exist_ok=True)
    
    csv_local = os.path.join(script_dir, "results.csv")
    csv_docs = os.path.join(docs_dir, "unit04_greedy_vs_dp_comparison.csv")
    
    for path in [csv_local, csv_docs]:
        with open(path, "w", newline="", encoding="ascii") as f:
            writer = csv.DictWriter(f, fieldnames=["N", "capacity", "greedy_val", "dp_val", "greedy_ms", "dp_ms", "gap_pct"])
            writer.writeheader()
            writer.writerows(results)
            
    print(f"\n[INFO] CSV saved to: {csv_local}")
    print(f"[INFO] CSV saved to: {csv_docs}")
    
    # Generate visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    ns = [r["N"] for r in results]
    g_vals = [r["greedy_val"] for r in results]
    dp_vals = [r["dp_val"] for r in results]
    g_times = [r["greedy_ms"] for r in results]
    dp_times = [r["dp_ms"] for r in results]
    
    # Plot 1: Solution Value Comparison
    ax1.plot(ns, dp_vals, marker='o', color='#2ca02c', linewidth=2, label='Dynamic Programming (Optimal)')
    ax1.plot(ns, g_vals, marker='s', color='#d62728', linewidth=2, linestyle='--', label='Greedy Heuristic (Suboptimal)')
    ax1.set_title('Solution Value (Profit) vs Problem Size (N)', fontsize=11, fontweight='bold')
    ax1.set_xlabel('Number of Items (N)', fontsize=10)
    ax1.set_ylabel('Total Knapsack Profit', fontsize=10)
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend()
    
    # Plot 2: Execution Time Comparison
    ax2.plot(ns, dp_times, marker='o', color='#1f77b4', linewidth=2, label='Dynamic Programming O(N*W)')
    ax2.plot(ns, g_times, marker='^', color='#ff7f0e', linewidth=2, label='Greedy Method O(N log N)')
    ax2.set_title('Execution Time vs Problem Size (N)', fontsize=11, fontweight='bold')
    ax2.set_xlabel('Number of Items (N)', fontsize=10)
    ax2.set_ylabel('Execution Time (milliseconds)', fontsize=10)
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend()
    
    plt.suptitle('Unit 04: Greedy vs Dynamic Programming (0/1 Knapsack)\nStudent: Khushi Dixit (Roll No: IC-2K23-51)', fontsize=12, fontweight='bold')
    plt.tight_layout()
    
    plot_local = os.path.join(script_dir, "greedy_vs_dp.png")
    plot_docs = os.path.join(docs_dir, "unit04_greedy_vs_dp_plot.png")
    
    fig.savefig(plot_local, dpi=300)
    fig.savefig(plot_docs, dpi=300)
    plt.close(fig)
    
    print(f"[INFO] Plot saved to: {plot_local}")
    print(f"[INFO] Plot saved to: {plot_docs}")
    print("=" * 75)


if __name__ == "__main__":
    run_comparison()
