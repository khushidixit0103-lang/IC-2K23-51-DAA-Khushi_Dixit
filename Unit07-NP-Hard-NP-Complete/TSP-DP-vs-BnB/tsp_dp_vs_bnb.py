"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 07: NP-Hard and NP-Complete Problems
Experiment: TSP - Dynamic Programming (Held-Karp) vs Branch and Bound (LCBB)

Description:
Empirically benchmarks Travelling Salesperson Problem using:
1. Dynamic Programming (Held-Karp Bitmask DP): O(n^2 * 2^n) time, O(n * 2^n) memory.
2. Branch and Bound (Reduced Cost Matrix LCBB): Min-Heap state expansion with
   initial Nearest-Neighbor upper bounding for aggressive branch pruning.
Tests varying city counts (N = 4 to 10), logging execution times, states explored,
and solution convergence to CSV and Matplotlib comparison plots.
"""

import os
import sys
import time
import random
import heapq
import copy
import csv

# Enable immediate stdout flushing
try:
    sys.stdout.reconfigure(line_buffering=True)
except Exception:
    pass

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

INF = float("inf")

# --- 1. Dynamic Programming (Held-Karp) ---
def held_karp_tsp(dist_matrix):
    n = len(dist_matrix)
    memo = {(1, 0): 0}
    
    for size in range(2, n + 1):
        for mask in range(1 << n):
            if bin(mask).count("1") != size or not (mask & 1):
                continue
            for j in range(1, n):
                if not (mask & (1 << j)):
                    continue
                prev_mask = mask ^ (1 << j)
                min_c = INF
                for i in range(n):
                    if i != j and (prev_mask & (1 << i)):
                        cost = memo.get((prev_mask, i), INF) + dist_matrix[i][j]
                        if cost < min_c:
                            min_c = cost
                memo[(mask, j)] = min_c
                
    final_mask = (1 << n) - 1
    min_tour = min(memo.get((final_mask, j), INF) + dist_matrix[j][0] for j in range(1, n))
    return min_tour, len(memo)

# --- 2. Branch and Bound with Nearest Neighbor Initial Bound ---
def nearest_neighbor_tour_cost(dist_matrix):
    n = len(dist_matrix)
    visited = [False] * n
    curr = 0
    visited[0] = True
    total_cost = 0
    for _ in range(n - 1):
        best_nxt = -1
        best_d = INF
        for nxt in range(n):
            if not visited[nxt] and dist_matrix[curr][nxt] < best_d:
                best_d = dist_matrix[curr][nxt]
                best_nxt = nxt
        if best_nxt == -1:
            return INF
        visited[best_nxt] = True
        total_cost += best_d
        curr = best_nxt
    total_cost += dist_matrix[curr][0]
    return total_cost

class TSPNode:
    def __init__(self, matrix, level, path, cost, vertex):
        self.matrix = matrix
        self.level = level
        self.path = path
        self.cost = cost
        self.vertex = vertex

    def __lt__(self, other):
        return self.cost < other.cost

def reduce_mat(mat, n):
    r_cost = 0
    for i in range(n):
        m = min(mat[i])
        if m != INF and m > 0:
            r_cost += m
            for j in range(n):
                if mat[i][j] != INF:
                    mat[i][j] -= m
    for j in range(n):
        m = min(mat[i][j] for i in range(n))
        if m != INF and m > 0:
            r_cost += m
            for i in range(n):
                if mat[i][j] != INF:
                    mat[i][j] -= m
    return r_cost

def bnb_tsp(dist_matrix):
    n = len(dist_matrix)
    mat = copy.deepcopy(dist_matrix)
    r_init = reduce_mat(mat, n)
    
    root = TSPNode(mat, 0, [0], r_init, 0)
    pq = [root]
    
    # Initialize with Nearest Neighbor upper bound to prune early
    min_tour = nearest_neighbor_tour_cost(dist_matrix)
    states_explored = 0
    
    while pq:
        curr = heapq.heappop(pq)
        states_explored += 1
        
        if curr.cost >= min_tour:
            continue
            
        if curr.level == n - 1:
            if curr.cost < min_tour:
                min_tour = curr.cost
            continue
            
        for nxt in range(n):
            if nxt not in curr.path and dist_matrix[curr.vertex][nxt] != INF:
                child_mat = copy.deepcopy(curr.matrix)
                for k in range(n):
                    child_mat[curr.vertex][k] = INF
                    child_mat[k][nxt] = INF
                child_mat[nxt][0] = INF
                
                r = reduce_mat(child_mat, n)
                child_cost = curr.cost + curr.matrix[curr.vertex][nxt] + r
                
                if child_cost < min_tour:
                    heapq.heappush(pq, TSPNode(child_mat, curr.level + 1, curr.path + [nxt], child_cost, nxt))
                    
    return min_tour, states_explored

def generate_symmetric_tsp_matrix(n, seed):
    random.seed(seed)
    mat = [[0 if i == j else INF for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = random.randint(10, 100)
            mat[i][j] = d
            mat[j][i] = d
    return mat

def benchmark():
    print("=" * 75)
    print("  IC-709 B: UNIT 7 - TSP: DP (HELD-KARP) VS BRANCH AND BOUND")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 75)

    city_sizes = [4, 6, 8, 10]
    results = []

    print(f"{'N':<4} | {'Tour Cost':<10} | {'DP Time (ms)':<14} | {'BnB Time (ms)':<14} | {'DP Memo States':<16} | {'BnB Explored':<14}")
    print("-" * 80)

    for n in city_sizes:
        matrix = generate_symmetric_tsp_matrix(n, seed=42 + n)

        # Held-Karp
        t0 = time.perf_counter()
        cost_dp, dp_states = held_karp_tsp(matrix)
        t_dp = (time.perf_counter() - t0) * 1000.0

        # Branch and Bound
        t0 = time.perf_counter()
        cost_bnb, bnb_states = bnb_tsp(matrix)
        t_bnb = (time.perf_counter() - t0) * 1000.0

        assert cost_dp == cost_bnb, f"Mismatch at N={n}"

        results.append({
            "N": n,
            "tour_cost": cost_dp,
            "dp_ms": round(t_dp, 4),
            "bnb_ms": round(t_bnb, 4),
            "dp_states": dp_states,
            "bnb_states": bnb_states
        })

        print(f"{n:<4} | {cost_dp:<10} | {t_dp:<14.3f} | {t_bnb:<14.3f} | {dp_states:<16} | {bnb_states:<14}")

    # Save to CSV
    script_dir = os.path.dirname(os.path.abspath(__file__))
    docs_dir = os.path.join(script_dir, "..", "..", "docs", "performance-analysis")
    os.makedirs(docs_dir, exist_ok=True)

    csv_local = os.path.join(script_dir, "results.csv")
    csv_docs = os.path.join(docs_dir, "unit07_tsp_dp_vs_bnb.csv")

    for path in [csv_local, csv_docs]:
        with open(path, "w", newline="", encoding="ascii") as f:
            writer = csv.DictWriter(f, fieldnames=["N", "tour_cost", "dp_ms", "bnb_ms", "dp_states", "bnb_states"])
            writer.writeheader()
            writer.writerows(results)

    print(f"\n[INFO] CSV saved to: {csv_local}")
    print(f"[INFO] CSV saved to: {csv_docs}")

    # Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    ns = [r["N"] for r in results]
    dp_t = [r["dp_ms"] for r in results]
    bnb_t = [r["bnb_ms"] for r in results]
    dp_s = [r["dp_states"] for r in results]
    bnb_s = [r["bnb_states"] for r in results]

    ax1.plot(ns, dp_t, marker='o', color='#1f77b4', linewidth=2, label='Held-Karp DP (O(N^2 * 2^N))')
    ax1.plot(ns, bnb_t, marker='s', color='#d62728', linewidth=2, label='Branch and Bound (LCBB)')
    ax1.set_title('Execution Time Comparison (ms)', fontsize=11, fontweight='bold')
    ax1.set_xlabel('Number of Cities (N)', fontsize=10)
    ax1.set_ylabel('Execution Time (milliseconds)', fontsize=10)
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend()

    ax2.plot(ns, dp_s, marker='o', color='#1f77b4', linewidth=2, label='DP Subproblem Table Entries')
    ax2.plot(ns, bnb_s, marker='s', color='#d62728', linewidth=2, label='BnB Nodes Explored')
    ax2.set_yscale('log')
    ax2.set_title('Memory / States Stored (Log Scale)', fontsize=11, fontweight='bold')
    ax2.set_xlabel('Number of Cities (N)', fontsize=10)
    ax2.set_ylabel('States Stored (log scale)', fontsize=10)
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend()

    plt.suptitle('Unit 07: TSP - Dynamic Programming vs Branch and Bound\nStudent: Khushi Dixit (Roll No: IC-2K23-51)', fontsize=12, fontweight='bold')
    plt.tight_layout()

    plot_local = os.path.join(script_dir, "tsp_dp_vs_bnb.png")
    plot_docs = os.path.join(docs_dir, "unit07_tsp_dp_vs_bnb_plot.png")

    fig.savefig(plot_local, dpi=300)
    fig.savefig(plot_docs, dpi=300)
    plt.close(fig)

    print(f"[INFO] Plot saved to: {plot_local}")
    print(f"[INFO] Plot saved to: {plot_docs}")
    print("=" * 75)


if __name__ == "__main__":
    benchmark()
