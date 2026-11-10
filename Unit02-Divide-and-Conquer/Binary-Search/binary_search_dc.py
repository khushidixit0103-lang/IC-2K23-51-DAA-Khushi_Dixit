"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 02: Divide and Conquer
Experiment: Binary Search using Divide and Conquer

Problem Statement:
Apply the Divide-and-Conquer paradigm to locate a key element in a sorted array:
1. Divide: Compute the midpoint index to partition the search domain into two halves.
2. Conquer: Recursively search the appropriate half where the key could reside.
3. Combine: Trivial step (return the found index or -1 if empty).
"""

import sys

def binary_search_dc(arr, low, high, key):
    """
    Locates 'key' in sorted array 'arr' between indices 'low' and 'high'
    using the formal Divide-and-Conquer technique.
    
    Returns:
        int: Index of key if found, else -1.
    """
    # Base condition: Empty subarray
    if low > high:
        return -1
        
    # Divide step
    mid = low + (high - low) // 2
    
    # Conquer step
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search_dc(arr, mid + 1, high, key)
    else:
        return binary_search_dc(arr, low, mid - 1, key)


def main():
    print("=" * 65)
    print("  IC-709 B: UNIT 2 - BINARY SEARCH (DIVIDE AND CONQUER)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)
    
    arr = [3, 9, 14, 19, 27, 33, 45, 52, 61, 78, 88, 95]
    print(f"Given Sorted Array: {arr}")
    print(f"Array Size (N): {len(arr)}\n")
    
    test_queries = [3, 45, 95, 20, 100]
    for q in test_queries:
        res = binary_search_dc(arr, 0, len(arr) - 1, q)
        if res != -1:
            print(f"Query key: {q:3d} -> Found at index: {res}")
        else:
            print(f"Query key: {q:3d} -> Not present in array (result = -1)")
            
    print("=" * 65)


if __name__ == "__main__":
    main()
