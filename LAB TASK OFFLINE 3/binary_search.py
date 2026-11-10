"""
Program: binary_search.py
Description: Implements iterative Binary Search returning index or -1 if not found.
             Tests on a sorted array with an existing and a non-existing value.
Student: Khushi Dixit | Roll No: IC-2K23-51
Lab: DAA Offline Lab 3 (Section C.4)
"""

def binary_search(arr, target):
    """
    Iterative Binary Search on a sorted array.
    Returns: index of target if found, else -1.
    """
    low = 0
    high = len(arr) - 1
    step = 1
    
    print(f"\nSearching for target value: {target}")
    print(f"{'Step':<6} | {'Low':<6} | {'High':<6} | {'Mid':<6} | {'A[Mid]':<8} | {'Decision / Next Sub-range'}")
    print("-" * 65)
    
    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]
        
        if mid_val == target:
            print(f"{step:<6} | {low:<6} | {high:<6} | {mid:<6} | {mid_val:<8} | TARGET FOUND at index {mid}!")
            return mid
        elif mid_val < target:
            print(f"{step:<6} | {low:<6} | {high:<6} | {mid:<6} | {mid_val:<8} | {mid_val} < {target} -> Search right: low = {mid + 1}")
            low = mid + 1
        else:
            print(f"{step:<6} | {low:<6} | {high:<6} | {mid:<6} | {mid_val:<8} | {mid_val} > {target} -> Search left: high = {mid - 1}")
            high = mid - 1
        step += 1
        
    print(f"Target {target} NOT FOUND in array (low > high).")
    return -1


def main():
    print("=" * 65)
    print("  DAA OFFLINE LAB 3: ITERATIVE BINARY SEARCH")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)
    
    # PDF Section B Question 7 sample: [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
    sorted_array = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
    print(f"Sorted Array: {sorted_array} (Length: {len(sorted_array)})")
    
    # 1. Test with an existing target (23)
    target_exist = 23
    idx1 = binary_search(sorted_array, target_exist)
    print(f"=> Result for {target_exist}: Found at index {idx1}")
    
    # 2. Test with a non-existent target (50)
    target_missing = 50
    idx2 = binary_search(sorted_array, target_missing)
    print(f"=> Result for {target_missing}: Returned {idx2} (Not Found)")
    print("=" * 65)


if __name__ == "__main__":
    main()
