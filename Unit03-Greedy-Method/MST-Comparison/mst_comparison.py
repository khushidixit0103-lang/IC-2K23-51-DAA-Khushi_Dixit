"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 03: Greedy Method
Experiment: Comparative Performance Analysis of Prim's vs Kruskal's Algorithm

Description:
Empirically benchmarks Prim's and Kruskal's MST algorithms across random graphs
with varying vertex counts (|V| = 10 to 100) and edge densities (sparse vs dense).
Saves benchmark metrics to CSV and generates comparison plots using Matplotlib.
"""

import os
import sys
import time
import random
import csv

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- DSU Implementation for Kruskal ---
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False

# --- Kruskal's Algorithm ---
def run_kruskal(n, edges):
    sorted_edges = sorted(edges, key=lambda e: e[2])
    dsu = DSU(n)
    cost = 0
    count = 0
    for u, v, w in sorted_edges:
        if dsu.union(u, v):
            cost += w
            count += 1
            if count == n - 1:
                break
    return cost

# --- Prim's Algorithm (Adjacency Matrix) ---
def run_prim(n, adj_matrix):
    INF = float("inf")
    key = [INF] * n
    in_mst = [False] * n
    key[0] = 0
    total_cost = 0

    for _ in range(n):
        min_k = INF
        u = -1
        for v in range(n):
            if not in_mst[v] and key[v] < min_k:
                min_k = key[v]
                u = v
        if u == -1:
            break
        in_mst[u] = True
        total_cost += min_k

        for v in range(n):
            w = adj_matrix[u][v]
            if w > 0 and not in_mst[v] and w < key[v]:
                key[v] = w

    return total_cost

def generate_connected_graph(n, density):
    """
    Generates a connected random undirected graph with given edge density.
    Returns: (edge_list, adj_matrix)
    """
    adj = [[0] * n for _ in range(n)]
    edges = []

    # Ensure connectivity via a random spanning tree
    nodes = list(range(n))
    random.shuffle(nodes)
    for i in range(1, n):
        u = nodes[i]
        v = random.choice(nodes[:i])
        w = random.randint(1, 100)
        adj[u][v] = w
        adj[v][u] = w
        edges.append((u, v, w))

    # Add random extra edges based on density
    max_edges = (n * (n - 1)) // 2
    target_edges = int(max_edges * density)
    while len(edges) < target_edges:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v and adj[u][v] == 0:
            w = random.randint(1, 100)
            adj[u][v] = w
            adj[v][u] = w
            edges.append((u, v, w))

    return edges, adj

def benchmark_mst():
    print("=" * 75)
    print("  IC-709 B: UNIT 3 - PRIM'S VS KRUSKAL'S MST COMPARISON")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 75)

    vertex_counts = [10, 20, 35, 50, 75, 100]
    densities = [("Sparse (15% edges)", 0.15), ("Dense (70% edges)", 0.70)]
    results = []

    for desc, d in densities:
        print(f"\n--- Graph Type: {desc} ---")
        print(f"{'|V|':<6} | {'|E|':<8} | {'Prim Time (ms)':<16} | {'Kruskal Time (ms)':<18} | {'Prim Cost':<10} | {'Kruskal Cost':<12}")
        print("-" * 75)
        for n in vertex_counts:
            edges, adj = generate_connected_graph(n, d)

            # Warm-up / trials
            num_trials = 5
            t0 = time.perf_counter()
            for _ in range(num_trials):
                cost_p = run_prim(n, adj)
            t_prim = (time.perf_counter() - t0) / num_trials * 1000.0

            t0 = time.perf_counter()
            for _ in range(num_trials):
                cost_k = run_kruskal(n, edges)
            t_kruskal = (time.perf_counter() - t0) / num_trials * 1000.0

            results.append({
                "density_type": desc,
                "V": n,
                "E": len(edges),
                "prim_ms": round(t_prim, 4),
                "kruskal_ms": round(t_kruskal, 4),
                "cost_match": cost_p == cost_k
            })

            print(f"{n:<6} | {len(edges):<8} | {t_prim:<16.3f} | {t_kruskal:<18.3f} | {cost_p:<10} | {cost_k:<12}")

    # Save to CSV
    script_dir = os.path.dirname(os.path.abspath(__file__))
    docs_dir = os.path.join(script_dir, "..", "..", "docs", "performance-analysis")
    os.makedirs(docs_dir, exist_ok=True)

    csv_local = os.path.join(script_dir, "results.csv")
    csv_docs = os.path.join(docs_dir, "unit03_mst_comparison.csv")

    for path in [csv_local, csv_docs]:
        with open(path, "w", newline="", encoding="ascii") as f:
            writer = csv.DictWriter(f, fieldnames=["density_type", "V", "E", "prim_ms", "kruskal_ms", "cost_match"])
            writer.writeheader()
            writer.writerows(results)

    print(f"\n[INFO] CSV saved to: {csv_local}")
    print(f"[INFO] CSV saved to: {csv_docs}")

    # Plot Comparison Curves
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Sparse
    sparse_res = [r for r in results if "Sparse" in r["density_type"]]
    v_s = [r["V"] for r in sparse_res]
    p_s = [r["prim_ms"] for r in sparse_res]
    k_s = [r["kruskal_ms"] for r in sparse_res]

    ax1.plot(v_s, p_s, marker='o', color='#1f77b4', linewidth=2, label="Prim's Algorithm (Matrix)")
    ax1.plot(v_s, k_s, marker='s', color='#2ca02c', linewidth=2, label="Kruskal's Algorithm (DSU)")
    ax1.set_title("Sparse Graphs (15% edge density)", fontsize=11, fontweight='bold')
    ax1.set_xlabel("Number of Vertices (|V|)", fontsize=10)
    ax1.set_ylabel("Execution Time (milliseconds)", fontsize=10)
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend()

    # Dense
    dense_res = [r for r in results if "Dense" in r["density_type"]]
    v_d = [r["V"] for r in dense_res]
    p_d = [r["prim_ms"] for r in dense_res]
    k_d = [r["kruskal_ms"] for r in dense_res]

    ax2.plot(v_d, p_d, marker='o', color='#1f77b4', linewidth=2, label="Prim's Algorithm (Matrix)")
    ax2.plot(v_d, k_d, marker='s', color='#2ca02c', linewidth=2, label="Kruskal's Algorithm (DSU)")
    ax2.set_title("Dense Graphs (70% edge density)", fontsize=11, fontweight='bold')
    ax2.set_xlabel("Number of Vertices (|V|)", fontsize=10)
    ax2.set_ylabel("Execution Time (milliseconds)", fontsize=10)
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend()

    plt.suptitle("Unit 03: Prim's vs Kruskal's MST Execution Time Comparison\nStudent: Khushi Dixit (Roll No: IC-2K23-51)", fontsize=12, fontweight='bold')
    plt.tight_layout()

    plot_local = os.path.join(script_dir, "mst_comparison.png")
    plot_docs = os.path.join(docs_dir, "unit03_mst_comparison_plot.png")

    fig.savefig(plot_local, dpi=300)
    fig.savefig(plot_docs, dpi=300)
    plt.close(fig)

    print(f"[INFO] Plot saved to: {plot_local}")
    print(f"[INFO] Plot saved to: {plot_docs}")
    print("=" * 75)

if __name__ == "__main__":
    benchmark_mst()
