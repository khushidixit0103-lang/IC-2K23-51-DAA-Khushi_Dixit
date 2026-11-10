"""
Program: part1_trace.py
Description: Finds the maximum element in a list while counting comparisons,
             and sorts the list from smallest to largest with step-by-step trace.
Student: Khushi Dixit | Roll No: IC-2K23-51
Lab: DAA Lab Task 1 (Part 1)
"""

def find_largest(arr):
    if not arr:
        print("List is empty!")
        return None, 0
    
    comparisons = 0
    max_val = arr[0]
    print(f"\nInitial maximum set to first element: {max_val}")
    print("-" * 55)
    print(f"{'Step (i)':<10} | {'Current Element A[i]':<22} | {'Current Max':<12} | {'Comparisons':<12}")
    print("-" * 55)
    
    for i in range(1, len(arr)):
        comparisons += 1
        curr = arr[i]
        if curr > max_val:
            max_val = curr
        print(f"i = {i:<6} | A[{i}] = {curr:<15} | max = {max_val:<8} | comparisons = {comparisons}")
        
    return max_val, comparisons


def trace_sort(arr):
    """
    Sorts list using step-by-step tracing (Bubble Sort / Exchange trace).
    """
    a = list(arr)
    n = len(a)
    print("\nSorting Steps (Smallest to Largest):")
    print(f"Initial Array: {a}")
    step = 1
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                print(f"  Step {step}: Swapped {a[j + 1]} and {a[j]} -> {a}")
                step += 1
                swapped = True
        if not swapped:
            break
    print(f"Final Sorted Array: {a}")
    return a


def main():
    print("=" * 60)
    print("  DAA LAB TASK 1: PART 1 - TRACE IT YOURSELF")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 60)
    
    # Pre-defined assignment input
    default_list = [8, 3, 15, 6, 2]
    
    print("\nChoose input mode:")
    print("1. Use PDF assignment list [8, 3, 15, 6, 2]")
    print("2. Enter custom numbers")
    choice = input("Enter choice (1/2, default=1): ").strip()
    
    if choice == "2":
        raw = input("Enter numbers separated by spaces: ").strip()
        if raw:
            nums = [int(x) for x in raw.split()]
        else:
            nums = default_list
    else:
        nums = default_list

    print(f"\nInput List: {nums}")
    
    # 1. Find largest with comparisons
    max_val, comparisons = find_largest(nums)
    print("-" * 55)
    print(f"Largest Number Found : {max_val}")
    print(f"Total Comparisons Made: {comparisons}")
    
    # 2. Sort with steps
    sorted_list = trace_sort(nums)
    print("=" * 60)


if __name__ == "__main__":
    main()
