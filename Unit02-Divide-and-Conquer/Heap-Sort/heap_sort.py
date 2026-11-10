"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 02: Divide and Conquer
Experiment: Heap Sort

Problem Statement:
Sort an array of N elements using the Heap Sort algorithm:
1. Build a Max-Heap from the input array in O(n) time.
2. Repeatedly extract the maximum element (root), swap it with the last element,
   reduce heap size, and restore the max-heap property using heapify in O(log n) time.
"""

def heapify(arr, n, i, stats):
    """
    Maintains the max-heap property for subtree rooted at index i.
    arr: List of elements
    n: Size of the heap
    i: Root index of current subtree
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check left child
    if left < n:
        stats["comparisons"] += 1
        if arr[left] > arr[largest]:
            largest = left
            
    # Check right child
    if right < n:
        stats["comparisons"] += 1
        if arr[right] > arr[largest]:
            largest = right
            
    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        stats["swaps"] += 1
        # Recursively heapify the affected subtree
        heapify(arr, n, largest, stats)


def heap_sort(arr):
    """
    In-place Heap Sort algorithm.
    """
    n = len(arr)
    stats = {"comparisons": 0, "swaps": 0}
    
    # Step 1: Build max-heap (rearrange array)
    # Start from last non-leaf node down to root
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, stats)
        
    # Step 2: One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        stats["swaps"] += 1
        # Call max heapify on the reduced heap
        heapify(arr, i, 0, stats)
        
    return arr, stats


def main():
    print("=" * 65)
    print("  IC-709 B: UNIT 2 - HEAP SORT")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)
    
    test_cases = [
        [12, 11, 13, 5, 6, 7],
        [64, 34, 25, 12, 22, 11, 90],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [42]
    ]
    
    for idx, sample in enumerate(test_cases, 1):
        original = list(sample)
        sorted_arr, stats = heap_sort(sample)
        is_sorted = sorted_arr == sorted(original)
        
        print(f"\nTest Case {idx}:")
        print(f"  Input Array       : {original}")
        print(f"  Sorted Output     : {sorted_arr}")
        print(f"  Verification Check: {'PASSED' if is_sorted else 'FAILED'}")
        print(f"  Comparisons Made  : {stats['comparisons']}")
        print(f"  Swaps Performed   : {stats['swaps']}")
        
    print("\n" + "=" * 65)


if __name__ == "__main__":
    main()
