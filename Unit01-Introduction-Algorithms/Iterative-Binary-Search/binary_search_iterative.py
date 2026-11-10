"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 01: Introduction to Algorithms and Performance Analysis
Experiment: Iterative Binary Search

Problem Statement:
Given a sorted array of N elements and a search key, find the position of the key
using Iterative Binary Search. If the key is not present, report not found.
"""

import sys
import time

def binary_search_iterative(arr, key):
    """
    Perform iterative binary search on a sorted array.
    
    Parameters:
        arr (list): Sorted list of comparable elements.
        key: Element to search for.
        
    Returns:
        tuple: (index, comparisons)
               index: 0-based index if found, else -1
               comparisons: Total number of key comparisons made
    """
    low = 0
    high = len(arr) - 1
    comparisons = 0
    
    while low <= high:
        mid = low + (high - low) // 2
        comparisons += 1
        
        if arr[mid] == key:
            return mid, comparisons
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1, comparisons


def demonstrate_cases():
    print("=" * 65)
    print("  IC-709 B: DAA LAB - UNIT 1: ITERATIVE BINARY SEARCH")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)
    
    sample_arr = [10, 23, 35, 42, 56, 68, 71, 85, 92, 99]
    print(f"Sorted Array: {sample_arr}")
    print(f"Array Size (N): {len(sample_arr)}")
    print("-" * 65)
    
    # Best-case: Element at middle index
    mid_idx = (len(sample_arr) - 1) // 2
    best_key = sample_arr[mid_idx]
    idx, comps = binary_search_iterative(sample_arr, best_key)
    print(f"[BEST CASE] Search Key = {best_key} (Element at mid):")
    print(f"  Result: Found at index {idx} in {comps} comparison(s)")
    print(f"  Theoretical Complexity: O(1)")
    print("-" * 65)
    
    # Average-case: Arbitrary element
    avg_key = 23
    idx, comps = binary_search_iterative(sample_arr, avg_key)
    print(f"[AVERAGE CASE] Search Key = {avg_key}:")
    print(f"  Result: Found at index {idx} in {comps} comparison(s)")
    print(f"  Theoretical Complexity: O(log n)")
    print("-" * 65)
    
    # Worst-case: Element not present or at leaf level of decision tree
    worst_key = 99
    idx, comps = binary_search_iterative(sample_arr, worst_key)
    print(f"[WORST CASE (Present)] Search Key = {worst_key}:")
    print(f"  Result: Found at index {idx} in {comps} comparison(s)")
    print(f"  Theoretical Complexity: O(log n)")
    print("-" * 65)
    
    not_found_key = 50
    idx, comps = binary_search_iterative(sample_arr, not_found_key)
    print(f"[WORST CASE (Not Found)] Search Key = {not_found_key}:")
    print(f"  Result: Not found (index {idx}) after {comps} comparison(s)")
    print(f"  Theoretical Complexity: O(log n)")
    print("=" * 65)


if __name__ == "__main__":
    demonstrate_cases()
