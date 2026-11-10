"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 05: Traversal and Search
Experiment: Comparative Performance Analysis of BFS vs DFS

Description:
Benchmarks Breadth-First Search and Depth-First Search on synthetic graphs with
varying vertex counts (|V| = 100 to 5,000) and edge densities.
Logs execution times to CSV and plots runtime scaling curves using Matplotlib.
"""

import os
import sys
import time
import random
import csv
from collections import deque

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.setrecursionlimit(50000)

def run_bfs(graph, n, start_node=0):
    visited = [False] * n
    queue = deque([start_node])
    visited[start_node] = True
    count = 0
    while queue:
        u = queue.popleft()
        count += 1
        for v in graph.get(u, []):
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    return count

def run_dfs(graph, n, start_node=0):
    visited = [False] * n
    stack = [start_node]
    count = 0
    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            count += 1
            for v in graph.get(u, []):
                if not visited[v]:
                    stack.append(v)
    return count

def generate_random_graph(n, edge_factor=4):
    """Generates a connected random graph where |E| approx n * edge_factor."""
    graph = {i: [] for i in range(n)}
    # Spanning tree
    for i in range(1, n):
        p = random.randint(0, i - 1)
        graph[i].append(p)
        graph[p].append(i)
    # Additional random edges
    extra_edges = n * (edge_factor - 1)
    for _ in range(extra_edges):
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:
            graph[u].append(v)
            graph[v].append(u)
    return graph

def benchmark_bfs_dfs():
    print("=" * 75)
    print("  IC-709 B: UNIT 5 - BFS VS DFS PERFORMANCE COMPARISON")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 75)

    graph_sizes = [100, 250, 500, 1000, 2500, 5000]
    num_trials = 10
    results = []

    print(f"{'|V|':<8} | {'Estimated |E|':<14} | {'BFS Time (ms)':<16} | {'DFS Time (ms)':<16} | {'All Visited?':<12}")
    print("-" * 75)

    for n in graph_sizes:
        graph = generate_random_graph(n, edge_factor=4)
        approx_e = sum(len(neighbors) for neighbors in graph.values()) // 2

        t0 = time.perf_counter()
        for _ in range(num_trials):
            bfs_cnt = run_bfs(graph, n, 0)
        t_bfs = (time.perf_counter() - t0) / num_trials * 1000.0

        t0 = time.perf_counter()
        for _ in range(num_trials):
            dfs_cnt = run_dfs(graph, n, 0)
        t_dfs = (time.perf_counter() - t0) / num_trials * 1000.0

        all_visited = (bfs_cnt == n) and (dfs_cnt == n)

        results.append({
            "V": n,
            "E": approx_e,
            "bfs_ms": round(t_bfs, 4),
            "dfs_ms": round(t_dfs, 4),
            "all_visited": all_visited
        })

        print(f"{n:<8} | {approx_e:<14} | {t_bfs:<16.3f} | {t_dfs:<16.3f} | {'YES' if all_visited else 'NO':<12}")

    # Save to CSV
    script_dir = os.path.dirname(os.path.abspath(__file__))
    docs_dir = os.path.join(script_dir, "..", "..", "docs", "performance-analysis")
    os.makedirs(docs_dir, exist_ok=True)

    csv_local = os.path.join(script_dir, "results.csv")
    csv_docs = os.path.join(docs_dir, "unit05_bfs_vs_dfs_comparison.csv")

    for path in [csv_local, csv_docs]:
        with open(path, "w", newline="", encoding="ascii") as f:
            writer = csv.DictWriter(f, fieldnames=["V", "E", "bfs_ms", "dfs_ms", "all_visited"])
            writer.writeheader()
            writer.writerows(results)

    print(f"\n[INFO] CSV saved to: {csv_local}")
    print(f"[INFO] CSV saved to: {csv_docs}")

    # Plot
    sizes = [r["V"] for r in results]
    bfs_times = [r["bfs_ms"] for r in results]
    dfs_times = [r["dfs_ms"] for r in results]

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, bfs_times, marker='o', color='#1f77b4', linewidth=2, label='Breadth-First Search (Queue / Level-order)')
    plt.plot(sizes, dfs_times, marker='s', color='#d62728', linewidth=2, label='Depth-First Search (Stack / Depth-first)')
    plt.title('Unit 05: BFS vs DFS Graph Traversal Benchmark (|V| = 100 to 5,000)\nStudent: Khushi Dixit (Roll No: IC-2K23-51)', fontsize=12, fontweight='bold')
    plt.xlabel('Number of Vertices (|V|)', fontsize=11)
    plt.ylabel('Execution Time (milliseconds)', fontsize=11)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(fontsize=11)
    plt.tight_layout()

    plot_local = os.path.join(script_dir, "bfs_vs_dfs.png")
    plot_docs = os.path.join(docs_dir, "unit05_bfs_vs_dfs_plot.png")

    plt.savefig(plot_local, dpi=300)
    plt.savefig(plot_docs, dpi=300)
    plt.close()

    print(f"[INFO] Plot saved to: {plot_local}")
    print(f"[INFO] Plot saved to: {plot_docs}")
    print("=" * 75)


if __name__ == "__main__":
    benchmark_bfs_dfs()
