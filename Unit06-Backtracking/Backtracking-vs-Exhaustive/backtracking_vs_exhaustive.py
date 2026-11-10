"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 06: Backtracking
Experiment: Backtracking vs Exhaustive Search Empirical Benchmark

Description:
Empirically benchmarks Backtracking versus Exhaustive Search on the N-Queens problem
across board sizes N = 4 to 10.
Measures state-space nodes visited and execution times, saves data to CSV,
and generates comparison plots illustrating exponential search-space pruning.
"""

import os
import sys
import time
import csv

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def is_safe_partial(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

# --- 1. Backtracking Solver ---
def solve_backtracking(n):
    board = [-1] * n
    nodes = [0]
    solutions = [0]
    
    def bt(row):
        nodes[0] += 1
        if row == n:
            solutions[0] += 1
            return
        for col in range(n):
            if is_safe_partial(board, row, col):
                board[row] = col
                bt(row + 1)
                board[row] = -1
                
    t0 = time.perf_counter()
    bt(0)
    elapsed_ms = (time.perf_counter() - t0) * 1000.0
    return solutions[0], nodes[0], elapsed_ms

# --- 2. Exhaustive Search Solver (Generates full candidates, validates at leaf) ---
def solve_exhaustive(n):
    """
    Exhaustive search on row-permutation search space of size N!
    (A pure brute-force N^N is astronomical for N>=9, so we compare against N!
    candidate permutation generator to showcase pruning).
    """
    board = list(range(n))
    nodes = [0]
    solutions = [0]
    
    def check_all_diagonals(b):
        for i in range(n):
            for j in range(i + 1, n):
                if abs(b[i] - b[j]) == abs(i - j):
                    return False
        return True
        
    def permute(l):
        nodes[0] += 1
        if l == n:
            if check_all_diagonals(board):
                solutions[0] += 1
            return
        for i in range(l, n):
            board[l], board[i] = board[i], board[l]
            permute(l + 1)
            board[l], board[i] = board[i], board[l]
            
    t0 = time.perf_counter()
    permute(0)
    elapsed_ms = (time.perf_counter() - t0) * 1000.0
    return solutions[0], nodes[0], elapsed_ms


def benchmark():
    print("=" * 75)
    print("  IC-709 B: UNIT 6 - BACKTRACKING VS EXHAUSTIVE SEARCH BENCHMARK")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 75)
    
    # Test up to N=9 for exhaustive search feasibility
    sizes = [4, 5, 6, 7, 8, 9]
    results = []
    
    print(f"{'N':<4} | {'Solutions':<10} | {'BT Nodes':<12} | {'Exhaust Nodes':<15} | {'BT Time (ms)':<14} | {'Exh Time (ms)':<14} | {'Node Pruning (%)':<16}")
    print("-" * 85)
    
    for n in sizes:
        s_bt, n_bt, t_bt = solve_backtracking(n)
        s_ex, n_ex, t_ex = solve_exhaustive(n)
        
        assert s_bt == s_ex, f"Mismatch at N={n}"
        prune_pct = (1.0 - (n_bt / n_ex)) * 100.0
        
        results.append({
            "N": n,
            "solutions": s_bt,
            "bt_nodes": n_bt,
            "exh_nodes": n_ex,
            "bt_time_ms": round(t_bt, 4),
            "exh_time_ms": round(t_ex, 4),
            "pruning_pct": round(prune_pct, 2)
        })
        
        print(f"{n:<4} | {s_bt:<10} | {n_bt:<12} | {n_ex:<15} | {t_bt:<14.3f} | {t_ex:<14.3f} | {prune_pct:<16.2f}%")
        
    # Save to CSV
    script_dir = os.path.dirname(os.path.abspath(__file__))
    docs_dir = os.path.join(script_dir, "..", "..", "docs", "performance-analysis")
    os.makedirs(docs_dir, exist_ok=True)
    
    csv_local = os.path.join(script_dir, "results.csv")
    csv_docs = os.path.join(docs_dir, "unit06_backtracking_vs_exhaustive.csv")
    
    for path in [csv_local, csv_docs]:
        with open(path, "w", newline="", encoding="ascii") as f:
            writer = csv.DictWriter(f, fieldnames=["N", "solutions", "bt_nodes", "exh_nodes", "bt_time_ms", "exh_time_ms", "pruning_pct"])
            writer.writeheader()
            writer.writerows(results)
            
    print(f"\n[INFO] CSV saved to: {csv_local}")
    print(f"[INFO] CSV saved to: {csv_docs}")
    
    # Generate visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    ns = [r["N"] for r in results]
    bt_nodes = [r["bt_nodes"] for r in results]
    exh_nodes = [r["exh_nodes"] for r in results]
    bt_times = [r["bt_time_ms"] for r in results]
    exh_times = [r["exh_time_ms"] for r in results]
    
    # Plot 1: Nodes Explored (Log scale)
    ax1.plot(ns, exh_nodes, marker='s', color='#d62728', linewidth=2, label='Exhaustive Search (No Pruning)')
    ax1.plot(ns, bt_nodes, marker='o', color='#2ca02c', linewidth=2, label='Backtracking (With Bounding Pruning)')
    ax1.set_yscale('log')
    ax1.set_title('State-Space Nodes Explored (Log Scale)', fontsize=11, fontweight='bold')
    ax1.set_xlabel('Board Dimension (N)', fontsize=10)
    ax1.set_ylabel('Total Nodes Explored (log scale)', fontsize=10)
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend()
    
    # Plot 2: Execution Time (ms)
    ax2.plot(ns, exh_times, marker='s', color='#d62728', linewidth=2, label='Exhaustive Search Time')
    ax2.plot(ns, bt_times, marker='o', color='#2ca02c', linewidth=2, label='Backtracking Time')
    ax2.set_title('Execution Time Comparison (ms)', fontsize=11, fontweight='bold')
    ax2.set_xlabel('Board Dimension (N)', fontsize=10)
    ax2.set_ylabel('Execution Time (milliseconds)', fontsize=10)
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend()
    
    plt.suptitle('Unit 06: Backtracking vs Exhaustive Search Benchmark\nStudent: Khushi Dixit (Roll No: IC-2K23-51)', fontsize=12, fontweight='bold')
    plt.tight_layout()
    
    plot_local = os.path.join(script_dir, "backtracking_vs_exhaustive.png")
    plot_docs = os.path.join(docs_dir, "unit06_backtracking_vs_exhaustive_plot.png")
    
    fig.savefig(plot_local, dpi=300)
    fig.savefig(plot_docs, dpi=300)
    plt.close(fig)
    
    print(f"[INFO] Plot saved to: {plot_local}")
    print(f"[INFO] Plot saved to: {plot_docs}")
    print("=" * 75)


if __name__ == "__main__":
    benchmark()
