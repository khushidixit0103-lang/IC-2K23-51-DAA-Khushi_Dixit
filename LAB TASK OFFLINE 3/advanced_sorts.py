"""
Program: advanced_sorts.py
Description: Implements Merge Sort, Quick Sort (with clear pivot comment),
             and Heap Sort as standalone functions, printing traces.
Student: Khushi Dixit | Roll No: IC-2K23-51
Lab: DAA Offline Lab 3 (Section C.2)
"""

# ==========================================
# 1. Merge Sort
# ==========================================
def merge_sort(arr):
    """
    Merge Sort: Divide and Conquer. Recursively splits array into halves,
    sorts each half, and merges them in sorted order.
    Returns: a new sorted list.
    """
    if len(arr) <= 1:
        return list(arr)
        
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge step
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


# ==========================================
# 2. Quick Sort
# ==========================================
# PIVOT SELECTION STRATEGY: Last Element (Lomuto Partition Scheme)
# We choose the LAST element of the current sub-array (arr[high]) as the pivot.
# All elements smaller than or equal to the pivot are partitioned to its left,
# and all elements strictly greater are placed to its right.
# ==========================================
def quick_sort(arr):
    """
    Quick Sort with LAST-ELEMENT pivot strategy.
    Returns: a new sorted list.
    """
    a = list(arr)
    
    def _quick_sort(low, high):
        if low < high:
            pivot_idx = _partition(low, high)
            _quick_sort(low, pivot_idx - 1)
            _quick_sort(pivot_idx + 1, high)
            
    def _partition(low, high):
        pivot = a[high]  # Pivot choice: LAST ELEMENT
        i = low - 1
        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1

    _quick_sort(0, len(a) - 1)
    return a


# ==========================================
# 3. Heap Sort
# ==========================================
def heap_sort(arr):
    """
    Heap Sort: Transforms the array into a Max-Heap in O(n) time,
    then repeatedly swaps root with the end of the heap and sifts down.
    Returns: a new sorted list.
    """
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

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]  # Move current root to end
        heapify(i, 0)

    return a


def main():
    print("=" * 65)
    print("  DAA OFFLINE LAB 3: MERGE SORT, QUICK SORT & HEAP SORT")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)
    
    # PDF Section B sample: [8, 3, 5, 4, 7, 6, 1, 2]
    sample = [8, 3, 5, 4, 7, 6, 1, 2]
    print(f"Sample Test Array: {sample}")
    
    m_res = merge_sort(sample)
    q_res = quick_sort(sample)
    h_res = heap_sort(sample)
    
    print("\nSorting Results:")
    print(f"  Merge Sort : {m_res}")
    print(f"  Quick Sort : {q_res} (Pivot: Last Element)")
    print(f"  Heap Sort  : {h_res}")
    print("=" * 65)


if __name__ == "__main__":
    main()
