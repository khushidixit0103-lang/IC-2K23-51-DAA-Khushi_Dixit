"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 01: Introduction to Algorithms and Performance Analysis
Experiment: Recursive Binary Search

Problem Statement:
Given a sorted array of N elements and a search key, find the position of the key
using Recursive Binary Search. If the key is not present, report not found.
"""

import sys

def binary_search_recursive(arr, low, high, key, comparisons_holder=None):
    """
    Perform recursive binary search on a sorted array.
    
    Parameters:
        arr (list): Sorted list of comparable elements.
        low (int): Lower index boundary.
        high (int): Upper index boundary.
        key: Target value to find.
        comparisons_holder (list): Single-element list [count] tracking comparisons.
        
    Returns:
        tuple: (index, total_comparisons)
    """
    if comparisons_holder is None:
        comparisons_holder = [0]
        
    if low > high:
        return -1, comparisons_holder[0]
        
    mid = low + (high - low) // 2
    comparisons_holder[0] += 1
    
    if arr[mid] == key:
        return mid, comparisons_holder[0]
    elif arr[mid] < key:
        return binary_search_recursive(arr, mid + 1, high, key, comparisons_holder)
    else:
        return binary_search_recursive(arr, low, mid - 1, key, comparisons_holder)


def demonstrate_cases():
    print("=" * 65)
    print("  IC-709 B: DAA LAB - UNIT 1: RECURSIVE BINARY SEARCH")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)
    
    sample_arr = [10, 23, 35, 42, 56, 68, 71, 85, 92, 99]
    n = len(sample_arr)
    print(f"Sorted Array: {sample_arr}")
    print(f"Array Size (N): {n}")
    print("-" * 65)
    
    # Best-case: Mid element
    mid_idx = (n - 1) // 2
    best_key = sample_arr[mid_idx]
    idx, comps = binary_search_recursive(sample_arr, 0, n - 1, best_key)
    print(f"[BEST CASE] Search Key = {best_key} (Element at mid):")
    print(f"  Result: Found at index {idx} in {comps} recursive step(s)")
    print(f"  Theoretical Complexity: O(1) time, O(1) stack space")
    print("-" * 65)
    
    # Average-case
    avg_key = 23
    idx, comps = binary_search_recursive(sample_arr, 0, n - 1, avg_key)
    print(f"[AVERAGE CASE] Search Key = {avg_key}:")
    print(f"  Result: Found at index {idx} in {comps} recursive step(s)")
    print(f"  Theoretical Complexity: O(log n) time, O(log n) stack space")
    print("-" * 65)
    
    # Worst-case (present at leaf)
    worst_key = 99
    idx, comps = binary_search_recursive(sample_arr, 0, n - 1, worst_key)
    print(f"[WORST CASE (Present)] Search Key = {worst_key}:")
    print(f"  Result: Found at index {idx} in {comps} recursive step(s)")
    print(f"  Theoretical Complexity: O(log n) time, O(log n) stack space")
    print("-" * 65)
    
    # Worst-case (absent)
    absent_key = 50
    idx, comps = binary_search_recursive(sample_arr, 0, n - 1, absent_key)
    print(f"[WORST CASE (Not Found)] Search Key = {absent_key}:")
    print(f"  Result: Not found (index {idx}) after {comps} recursive step(s)")
    print(f"  Theoretical Complexity: O(log n) time, O(log n) stack space")
    print("=" * 65)


if __name__ == "__main__":
    demonstrate_cases()
