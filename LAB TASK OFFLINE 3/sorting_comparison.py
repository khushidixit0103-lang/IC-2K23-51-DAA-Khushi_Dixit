"""
Program: sorting_comparison.py
Description: Empirical timing analysis of the six sorting algorithms:
             - Bubble Sort, Selection Sort, Insertion Sort
             - Merge Sort, Quick Sort (Last Element Pivot), Heap Sort
             Across 3 input distributions: Random, Already Sorted, Reverse Sorted
             For N in [100, 500, 1000, 2000].
             Generates results table, saves CSV, and creates Matplotlib comparison plots.
Student: Khushi Dixit | Roll No: IC-2K23-51
Lab: DAA Offline Lab 3 (Section D.5 & D.6)
"""

import os
import sys
import time
import random
import csv

# Set Matplotlib headless backend
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Increase recursion depth for worst-case quick sort on already-sorted arrays
sys.setrecursionlimit(50000)

# --- Sorting Algorithms ---

def bubble_sort(arr):
    a = list(arr)
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def selection_sort(arr):
    a = list(arr)
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a


def insertion_sort(arr):
    a = list(arr)
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr):
    if len(arr) <= 1:
        return list(arr)
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(arr):
    a = list(arr)
    def _quick_sort(low, high):
        if low < high:
            pivot = a[high]
            i = low - 1
            for j in range(low, high):
                if a[j] <= pivot:
                    i += 1
                    a[i], a[j] = a[j], a[i]
            a[i + 1], a[high] = a[high], a[i + 1]
            p_idx = i + 1
            _quick_sort(low, p_idx - 1)
            _quick_sort(p_idx + 1, high)
    _quick_sort(0, len(a) - 1)
    return a


def heap_sort(arr):
    a = list(arr)
    n = len(a)
    def heapify(size, root_idx):
        largest = root_idx
        left = 2 * root_idx + 1
        right = 2 * root_idx + 2
        if left < size and a[left] > a[largest]:
            largest = left
        if right < size and a[right] > a[largest]:
            largest = right
        if largest != root_idx:
            a[root_idx], a[largest] = a[largest], a[root_idx]
            heapify(size, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(i, 0)
    return a


# --- Empirical Benchmark ---

def run_benchmarks():
    print("=" * 75)
    print("  DAA OFFLINE LAB 3: EMPIRICAL TIMING ANALYSIS OF 6 SORTING ALGORITHMS")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 75)
    
    sizes = [100, 500, 1000, 2000]
    input_types = ["random", "already_sorted", "reverse_sorted"]
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort)
    ]
    
    results = []
    
    print(f"\n{'Algorithm':<16} | {'Input Type':<15} | {'N':<6} | {'Time (ms)':<10}")
    print("-" * 55)
    
    random.seed(42)
    for n in sizes:
        base_rand = [random.randint(1, 100000) for _ in range(n)]
        base_sorted = list(range(1, n + 1))
        base_reverse = list(range(n, 0, -1))
        
        datasets = {
            "random": base_rand,
            "already_sorted": base_sorted,
            "reverse_sorted": base_reverse
        }
        
        for itype in input_types:
            arr_to_sort = datasets[itype]
            for name, func in algorithms:
                # Measure execution time
                t0 = time.perf_counter()
                res = func(arr_to_sort)
                t_elapsed_ms = (time.perf_counter() - t0) * 1000.0
                
                results.append({
                    "algorithm": name,
                    "input_type": itype,
                    "n": n,
                    "time_ms": round(t_elapsed_ms, 4)
                })
                print(f"{name:<16} | {itype:<15} | {n:<6} | {t_elapsed_ms:<10.3f}")

    # Save to CSV
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(script_dir, "sorting_timing_results.csv")
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["algorithm", "input_type", "n", "time_ms"])
        writer.writeheader()
        writer.writerows(results)
    print(f"\n[INFO] Raw timing results successfully saved to: {csv_file}")
    
    # --- Generate Plots ---
    plot1_path = os.path.join(script_dir, "random_input_timing_plot.png")
    plot2_path = os.path.join(script_dir, "already_sorted_timing_plot.png")
    
    # Plot 1: Input size vs Time on Random Input
    plt.figure(figsize=(9, 6))
    for name, _ in algorithms:
        subset = [r for r in results if r["algorithm"] == name and r["input_type"] == "random"]
        xs = [r["n"] for r in subset]
        ys = [r["time_ms"] for r in subset]
        plt.plot(xs, ys, marker='o', label=name, linewidth=2)
        
    plt.title("Sorting Algorithms Performance on RANDOM Input Data\nStudent: Khushi Dixit (IC-2K23-51)", fontsize=11, fontweight='bold')
    plt.xlabel("Input Size (n)", fontsize=10)
    plt.ylabel("Execution Time (milliseconds)", fontsize=10)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(plot1_path, dpi=300)
    plt.close()
    print(f"[INFO] Plot 1 (Random Data) saved to: {plot1_path}")
    
    # Plot 2: Input size vs Time on Already Sorted Input
    plt.figure(figsize=(9, 6))
    for name, _ in algorithms:
        subset = [r for r in results if r["algorithm"] == name and r["input_type"] == "already_sorted"]
        xs = [r["n"] for r in subset]
        ys = [r["time_ms"] for r in subset]
        plt.plot(xs, ys, marker='s', label=name, linewidth=2)
        
    plt.title("Sorting Algorithms Performance on ALREADY-SORTED Input Data\nStudent: Khushi Dixit (IC-2K23-51)", fontsize=11, fontweight='bold')
    plt.xlabel("Input Size (n)", fontsize=10)
    plt.ylabel("Execution Time (milliseconds)", fontsize=10)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(plot2_path, dpi=300)
    plt.close()
    print(f"[INFO] Plot 2 (Already Sorted) saved to: {plot2_path}")
    print("=" * 75)


if __name__ == "__main__":
    run_benchmarks()
