"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 02: Divide and Conquer
Experiment: Quick Sort

Problem Statement:
Sort an array using Quick Sort:
1. Divide: Partition the array A[low...high] around a pivot element such that all
   elements <= pivot precede it and all elements > pivot follow it.
2. Conquer: Recursively sort the two partitions A[low...pivot_idx-1] and A[pivot_idx+1...high].
3. Combine: In-place; no explicit combine step required.
"""

def partition(arr, low, high, stats):
    """
    Standard Lomuto partitioning scheme choosing arr[high] as pivot.
    """
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        stats["comparisons"] += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            stats["swaps"] += 1
            
    # Swap pivot into its correct sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    stats["swaps"] += 1
    return i + 1


def quick_sort(arr, low, high, stats=None):
    """Recursive Quick Sort function."""
    if stats is None:
        stats = {"comparisons": 0, "swaps": 0, "calls": 0}
        
    stats["calls"] += 1
    
    if low < high:
        pi = partition(arr, low, high, stats)
        quick_sort(arr, low, pi - 1, stats)
        quick_sort(arr, pi + 1, high, stats)
        
    return arr, stats


def main():
    print("=" * 65)
    print("  IC-709 B: UNIT 2 - QUICK SORT (DIVIDE AND CONQUER)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)
    
    test_cases = [
        [10, 80, 30, 90, 40, 50, 70],
        [64, 25, 12, 22, 11],
        [1, 2, 3, 4, 5],           # Already sorted (Worst-case for basic pivot)
        [5, 4, 3, 2, 1],           # Reverse sorted (Worst-case)
        [42]
    ]
    
    for idx, sample in enumerate(test_cases, 1):
        original = list(sample)
        stats = {"comparisons": 0, "swaps": 0, "calls": 0}
        sorted_arr, stats = quick_sort(sample, 0, len(sample) - 1, stats)
        
        is_sorted = sorted_arr == sorted(original)
        
        print(f"\nTest Case {idx}:")
        print(f"  Input Array       : {original}")
        print(f"  Sorted Output     : {sorted_arr}")
        print(f"  Verification Check: {'PASSED' if is_sorted else 'FAILED'}")
        print(f"  Comparisons Made  : {stats['comparisons']}")
        print(f"  Swaps Performed   : {stats['swaps']}")
        print(f"  Recursive Calls   : {stats['calls']}")
        
    print("\n" + "=" * 65)


if __name__ == "__main__":
    main()
