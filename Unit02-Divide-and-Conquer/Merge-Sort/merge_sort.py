"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 02: Divide and Conquer
Experiment: Merge Sort

Problem Statement:
Sort an array of N elements using the classic Merge Sort algorithm:
1. Divide the array into two equal halves.
2. Conquer by recursively sorting both subarrays.
3. Combine by merging the two sorted halves into a single sorted array.
"""

def merge(arr, low, mid, high, stats):
    """Merges two sorted subarrays arr[low...mid] and arr[mid+1...high]."""
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]
    
    i = 0
    j = 0
    k = low
    
    while i < len(left) and j < len(right):
        stats["comparisons"] += 1
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


def merge_sort(arr, low, high, stats=None):
    """Recursive divide-and-conquer Merge Sort."""
    if stats is None:
        stats = {"comparisons": 0, "calls": 0}
        
    stats["calls"] += 1
    
    if low < high:
        mid = low + (high - low) // 2
        merge_sort(arr, low, mid, stats)
        merge_sort(arr, mid + 1, high, stats)
        merge(arr, low, mid, high, stats)
        
    return arr, stats


def main():
    print("=" * 65)
    print("  IC-709 B: UNIT 2 - MERGE SORT (DIVIDE AND CONQUER)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)
    
    test_cases = [
        [38, 27, 43, 3, 9, 82, 10],
        [64, 34, 25, 12, 22, 11, 90],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [42]
    ]
    
    for idx, sample in enumerate(test_cases, 1):
        original = list(sample)
        stats = {"comparisons": 0, "calls": 0}
        sorted_arr, stats = merge_sort(sample, 0, len(sample) - 1, stats)
        
        is_sorted = sorted_arr == sorted(original)
        
        print(f"\nTest Case {idx}:")
        print(f"  Input Array       : {original}")
        print(f"  Sorted Output     : {sorted_arr}")
        print(f"  Verification Check: {'PASSED' if is_sorted else 'FAILED'}")
        print(f"  Total Comparisons : {stats['comparisons']}")
        print(f"  Recursive Calls   : {stats['calls']}")
        
    print("\n" + "=" * 65)


if __name__ == "__main__":
    main()
