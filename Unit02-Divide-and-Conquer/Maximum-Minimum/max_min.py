"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 02: Divide and Conquer
Experiment: Maximum and Minimum using Divide and Conquer (Tournament Method)

Problem Statement:
Find both the maximum and minimum elements in an array using Divide and Conquer.
Achieves an optimal comparison count of 3n/2 - 2 compared to 2n - 2 for linear scan.
"""

def max_min_dc(arr, low, high, counter=None):
    """
    Recursively finds maximum and minimum in arr[low...high].
    
    Returns:
        tuple: (min_val, max_val)
    """
    if counter is None:
        counter = [0]
        
    # Case 1: Only one element
    if low == high:
        return arr[low], arr[low]
        
    # Case 2: Exactly two elements
    if high == low + 1:
        counter[0] += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
            
    # Case 3: More than two elements - Divide into two sub-problems
    mid = low + (high - low) // 2
    
    min1, max1 = max_min_dc(arr, low, mid, counter)
    min2, max2 = max_min_dc(arr, mid + 1, high, counter)
    
    # Combine step: 2 comparisons to determine global min and max
    counter[0] += 2
    global_min = min1 if min1 < min2 else min2
    global_max = max1 if max1 > max2 else max2
    
    return global_min, global_max


def linear_scan_max_min(arr):
    """Standard sequential scan for comparison verification."""
    comparisons = 0
    if not arr:
        return None, None, 0
    current_min = arr[0]
    current_max = arr[0]
    for x in arr[1:]:
        comparisons += 1
        if x < current_min:
            current_min = x
        else:
            comparisons += 1
            if x > current_max:
                current_max = x
    return current_min, current_max, comparisons


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 2 - MAXIMUM AND MINIMUM (DIVIDE AND CONQUER)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    test_arrays = [
        [22, 13, -5, 88, 90, 3, 44, 71],
        [100, 20, 300, 40, 50, 60, 70, 80, 90, 10],
        [42],
        [99, 11]
    ]
    
    for idx, arr in enumerate(test_arrays, 1):
        print(f"\nTest Array {idx}: {arr}")
        n = len(arr)
        counter = [0]
        min_val, max_val = max_min_dc(arr, 0, n - 1, counter)
        
        lin_min, lin_max, lin_comps = linear_scan_max_min(arr)
        
        # Theoretical formula: 3n/2 - 2 when n is power of 2
        theoretical_dc = (3 * n // 2) - 2 if n >= 2 else 0
        
        print(f"  Array Size (N)       : {n}")
        print(f"  Minimum Element      : {min_val}")
        print(f"  Maximum Element      : {max_val}")
        print(f"  D&C Comparisons Made : {counter[0]} (Theoretical ~ 3N/2 - 2: {theoretical_dc})")
        print(f"  Linear Comparisons   : {lin_comps} (Worst-case 2N - 2: {max(0, 2*n - 2)})")
        print(f"  Comparison Savings   : {lin_comps - counter[0]} fewer comparisons")
        
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
