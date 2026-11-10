"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 02: Divide and Conquer
Experiment: Empirical Performance Comparison of Merge Sort, Quick Sort, and Heap Sort

Description:
Empirically benchmarks execution times of Merge Sort, Quick Sort, and Heap Sort
on random integer arrays across input sizes N = [500, 1000, 2500, 5000, 10000, 20000].
Records elapsed time, verifies correctness, saves data to CSV, and generates
visual comparison plots using Matplotlib.
"""

import os
import sys
import time
import random
import csv

# Increase recursion depth for deep quicksort calls on large inputs
sys.setrecursionlimit(30000)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- 1. Merge Sort Implementation ---
def merge(arr, low, mid, high):
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]
    i = 0
    j = 0
    k = low
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort_core(arr, low, high):
    if low < high:
        mid = low + (high - low) // 2
        merge_sort_core(arr, low, mid)
        merge_sort_core(arr, mid + 1, high)
        merge(arr, low, mid, high)

def run_merge_sort(arr):
    a = list(arr)
    merge_sort_core(a, 0, len(a) - 1)
    return a

# --- 2. Quick Sort Implementation ---
def partition(arr, low, high):
    # Median-of-three or middle pivot to avoid worst-case recursion degradation
    mid = low + (high - low) // 2
    arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_core(arr, low, high):
    while low < high:
        pi = partition(arr, low, high)
        # Tail-call optimization: recurse on smaller partition first
        if pi - low < high - pi:
            quick_sort_core(arr, low, pi - 1)
            low = pi + 1
        else:
            quick_sort_core(arr, pi + 1, high)
            high = pi - 1

def run_quick_sort(arr):
    a = list(arr)
    quick_sort_core(a, 0, len(a) - 1)
    return a

# --- 3. Heap Sort Implementation ---
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def run_heap_sort(arr):
    a = list(arr)
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)
    return a

# --- Benchmarking Function ---
def benchmark_sorting_algorithms():
    print("=" * 75)
    print("  IC-709 B: UNIT 2 - SORTING ALGORITHMS PERFORMANCE COMPARISON")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 75)
    
    input_sizes = [500, 1000, 2500, 5000, 10000, 20000]
    num_runs = 3
    results = []

    print(f"{'Size (N)':<10} | {'Merge Sort (ms)':<18} | {'Quick Sort (ms)':<18} | {'Heap Sort (ms)':<18} | {'Status':<10}")
    print("-" * 80)

    for n in input_sizes:
        # Generate random array of size N
        random.seed(42 + n)
        arr = [random.randint(1, 100000) for _ in range(n)]
        expected = sorted(arr)

        # Merge Sort
        t0 = time.perf_counter()
        for _ in range(num_runs):
            res_m = run_merge_sort(arr)
        t_merge = (time.perf_counter() - t0) / num_runs * 1000.0  # ms

        # Quick Sort
        t0 = time.perf_counter()
        for _ in range(num_runs):
            res_q = run_quick_sort(arr)
        t_quick = (time.perf_counter() - t0) / num_runs * 1000.0  # ms

        # Heap Sort
        t0 = time.perf_counter()
        for _ in range(num_runs):
            res_h = run_heap_sort(arr)
        t_heap = (time.perf_counter() - t0) / num_runs * 1000.0  # ms

        # Verify correctness
        valid = (res_m == expected) and (res_q == expected) and (res_h == expected)
        status_str = "PASSED" if valid else "FAILED"

        results.append({
            "size": n,
            "merge_sort_ms": round(t_merge, 4),
            "quick_sort_ms": round(t_quick, 4),
            "heap_sort_ms": round(t_heap, 4),
            "verified": status_str
        })

        print(f"{n:<10} | {t_merge:<18.3f} | {t_quick:<18.3f} | {t_heap:<18.3f} | {status_str:<10}")

    # Save to CSV
    script_dir = os.path.dirname(os.path.abspath(__file__))
    docs_dir = os.path.join(script_dir, "..", "..", "docs", "performance-analysis")
    os.makedirs(docs_dir, exist_ok=True)

    csv_local = os.path.join(script_dir, "results.csv")
    csv_docs = os.path.join(docs_dir, "unit02_sorting_performance.csv")

    for path in [csv_local, csv_docs]:
        with open(path, "w", newline="", encoding="ascii") as f:
            writer = csv.DictWriter(f, fieldnames=["size", "merge_sort_ms", "quick_sort_ms", "heap_sort_ms", "verified"])
            writer.writeheader()
            writer.writerows(results)

    print(f"\n[INFO] CSV saved to: {csv_local}")
    print(f"[INFO] CSV saved to: {csv_docs}")

    # Plot Comparison Curves
    sizes = [r["size"] for r in results]
    merge_times = [r["merge_sort_ms"] for r in results]
    quick_times = [r["quick_sort_ms"] for r in results]
    heap_times = [r["heap_sort_ms"] for r in results]

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, merge_times, marker='o', color='#1f77b4', linewidth=2, label='Merge Sort (Divide & Conquer)')
    plt.plot(sizes, quick_times, marker='s', color='#2ca02c', linewidth=2, label='Quick Sort (Partitioning)')
    plt.plot(sizes, heap_times, marker='^', color='#d62728', linewidth=2, label='Heap Sort (Binary Max-Heap)')

    plt.title('Unit 02: Sorting Algorithm Execution Time Comparison (N = 500 to 20,000)\nStudent: Khushi Dixit (Roll No: IC-2K23-51)', fontsize=12, fontweight='bold')
    plt.xlabel('Array Size (N)', fontsize=11)
    plt.ylabel('Execution Time (milliseconds)', fontsize=11)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(fontsize=11)
    plt.tight_layout()

    plot_local = os.path.join(script_dir, "sorting_performance.png")
    plot_docs = os.path.join(docs_dir, "unit02_sorting_plot.png")

    plt.savefig(plot_local, dpi=300)
    plt.savefig(plot_docs, dpi=300)
    plt.close()

    print(f"[INFO] Plot saved to: {plot_local}")
    print(f"[INFO] Plot saved to: {plot_docs}")
    print("=" * 75)


if __name__ == "__main__":
    benchmark_sorting_algorithms()
