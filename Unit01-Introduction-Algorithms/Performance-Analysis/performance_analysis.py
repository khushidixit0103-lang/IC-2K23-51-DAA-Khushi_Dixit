"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 01: Introduction to Algorithms and Performance Analysis
Experiment: Performance Analysis of Iterative vs Recursive Binary Search

Description:
Empirically benchmarks execution times of Iterative and Recursive Binary Search
across varying input array sizes (N = 1,000 to 500,000) under Best, Average,
and Worst cases. Saves measured data to CSV and renders comparison plots.
"""

import os
import sys
import time
import csv
import random

# Force headless Agg backend for matplotlib in CLI/sandbox environment
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Iterative implementation
def binary_search_iterative(arr, key):
    low = 0
    high = len(arr) - 1
    comps = 0
    while low <= high:
        mid = low + (high - low) // 2
        comps += 1
        if arr[mid] == key:
            return mid, comps
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comps

# Recursive implementation
def binary_search_recursive(arr, low, high, key):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search_recursive(arr, mid + 1, high, key)
    else:
        return binary_search_recursive(arr, low, mid - 1, key)

def benchmark():
    print("=" * 70)
    print("  IC-709 B: UNIT 1 - PERFORMANCE ANALYSIS (EMPIRICAL BENCHMARKING)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)

    input_sizes = [1000, 5000, 10000, 50000, 100000, 250000, 500000]
    num_trials = 200  # Repeat trials to get reliable microsecond timings

    results = []

    print(f"{'Size (N)':<10} | {'Iter Worst (us)':<16} | {'Rec Worst (us)':<16} | {'Iter Avg (us)':<16} | {'Rec Avg (us)':<16}")
    print("-" * 75)

    for n in input_sizes:
        arr = list(range(0, n * 2, 2))  # Even numbers from 0 to 2n-2

        # Best Case: Key is exactly in the middle
        best_key = arr[len(arr) // 2]
        
        # Worst Case: Key is an odd number (not present, forces traversal to leaf)
        worst_key = arr[-1] + 1

        # Average Case: Random key uniformly chosen from array
        avg_keys = [random.choice(arr) for _ in range(num_trials)]

        # --- Measure Iterative Worst Case ---
        t0 = time.perf_counter()
        for _ in range(num_trials):
            binary_search_iterative(arr, worst_key)
        t_iter_worst = (time.perf_counter() - t0) / num_trials * 1e6  # microseconds

        # --- Measure Recursive Worst Case ---
        t0 = time.perf_counter()
        for _ in range(num_trials):
            binary_search_recursive(arr, 0, n - 1, worst_key)
        t_rec_worst = (time.perf_counter() - t0) / num_trials * 1e6

        # --- Measure Iterative Average Case ---
        t0 = time.perf_counter()
        for k in avg_keys:
            binary_search_iterative(arr, k)
        t_iter_avg = (time.perf_counter() - t0) / num_trials * 1e6

        # --- Measure Recursive Average Case ---
        t0 = time.perf_counter()
        for k in avg_keys:
            binary_search_recursive(arr, 0, n - 1, k)
        t_rec_avg = (time.perf_counter() - t0) / num_trials * 1e6

        # --- Measure Best Case ---
        t0 = time.perf_counter()
        for _ in range(num_trials):
            binary_search_iterative(arr, best_key)
        t_iter_best = (time.perf_counter() - t0) / num_trials * 1e6

        t0 = time.perf_counter()
        for _ in range(num_trials):
            binary_search_recursive(arr, 0, n - 1, best_key)
        t_rec_best = (time.perf_counter() - t0) / num_trials * 1e6

        results.append({
            "size": n,
            "iter_best_us": round(t_iter_best, 4),
            "rec_best_us": round(t_rec_best, 4),
            "iter_avg_us": round(t_iter_avg, 4),
            "rec_avg_us": round(t_rec_avg, 4),
            "iter_worst_us": round(t_iter_worst, 4),
            "rec_worst_us": round(t_rec_worst, 4),
        })

        print(f"{n:<10} | {t_iter_worst:<16.3f} | {t_rec_worst:<16.3f} | {t_iter_avg:<16.3f} | {t_rec_avg:<16.3f}")

    # Output CSV files
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path_local = os.path.join(script_dir, "results.csv")
    docs_dir = os.path.join(script_dir, "..", "..", "docs", "performance-analysis")
    os.makedirs(docs_dir, exist_ok=True)
    csv_path_docs = os.path.join(docs_dir, "unit01_binary_search_performance.csv")

    for path in [csv_path_local, csv_path_docs]:
        with open(path, "w", newline="", encoding="ascii") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "size", "iter_best_us", "rec_best_us", "iter_avg_us", "rec_avg_us", "iter_worst_us", "rec_worst_us"
            ])
            writer.writeheader()
            writer.writerows(results)
    print(f"\n[INFO] Saved results to: {csv_path_local}")
    print(f"[INFO] Saved results to: {csv_path_docs}")

    # Generate Matplotlib plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    sizes = [r["size"] for r in results]
    iter_worst = [r["iter_worst_us"] for r in results]
    rec_worst = [r["rec_worst_us"] for r in results]
    iter_avg = [r["iter_avg_us"] for r in results]
    rec_avg = [r["rec_avg_us"] for r in results]

    # Plot 1: Worst-Case comparison
    ax1.plot(sizes, iter_worst, marker='o', color='#1f77b4', linewidth=2, label='Iterative Binary Search (Worst)')
    ax1.plot(sizes, rec_worst, marker='s', color='#d62728', linewidth=2, linestyle='--', label='Recursive Binary Search (Worst)')
    ax1.set_title('Worst-Case Execution Time vs Input Size (N)', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Array Size (N)', fontsize=11)
    ax1.set_ylabel('Execution Time (microseconds)', fontsize=11)
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend(loc='upper left')

    # Plot 2: Average-Case comparison
    ax2.plot(sizes, iter_avg, marker='^', color='#2ca02c', linewidth=2, label='Iterative Binary Search (Average)')
    ax2.plot(sizes, rec_avg, marker='d', color='#ff7f0e', linewidth=2, linestyle='--', label='Recursive Binary Search (Average)')
    ax2.set_title('Average-Case Execution Time vs Input Size (N)', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Array Size (N)', fontsize=11)
    ax2.set_ylabel('Execution Time (microseconds)', fontsize=11)
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend(loc='upper left')

    plt.suptitle('Unit 01: Iterative vs Recursive Binary Search Performance Analysis\nStudent: Khushi Dixit (Roll No: IC-2K23-51)', fontsize=13, fontweight='bold')
    plt.tight_layout()

    plot_path_local = os.path.join(script_dir, "binary_search_performance.png")
    plot_path_docs = os.path.join(docs_dir, "unit01_binary_search_plot.png")

    fig.savefig(plot_path_local, dpi=300)
    fig.savefig(plot_path_docs, dpi=300)
    plt.close(fig)

    print(f"[INFO] Performance plot generated at: {plot_path_local}")
    print(f"[INFO] Performance plot generated at: {plot_path_docs}")
    print("=" * 70)

if __name__ == "__main__":
    benchmark()
