"""
Program: radix_sort.py
Description: Implements Radix Sort for non-negative integers using the
             Least Significant Digit (LSD) approach with Counting Sort helper.
Student: Khushi Dixit | Roll No: IC-2K23-51
Lab: DAA Offline Lab 3 (Section C.3)
"""

def counting_sort_by_digit(arr, exp):
    """
    Stable counting sort helper to sort elements based on the digit
    at place value `exp` (1s, 10s, 100s, etc.).
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Base 10 digits 0 to 9

    # Count occurrences of each digit
    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1

    # Transform count[i] to store actual positions (prefix sums)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array in reverse to ensure stability
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    return output


def radix_sort(arr):
    """
    Radix Sort (LSD) for non-negative integers.
    Returns: a new sorted list.
    """
    if not arr or len(arr) <= 1:
        return list(arr)
        
    a = list(arr)
    max_val = max(a)
    
    print(f"\n--- Radix Sort Trace on {a} ---")
    print(f"Maximum element: {max_val} (Determines maximum digit passes)")
    
    exp = 1
    pass_num = 1
    place_names = {1: "Ones (1s)", 10: "Tens (10s)", 100: "Hundreds (100s)", 1000: "Thousands (1000s)"}
    
    while max_val // exp > 0:
        place = place_names.get(exp, f"10^{pass_num-1}s")
        a = counting_sort_by_digit(a, exp)
        print(f"  Pass {pass_num} (Sorted by {place} digit): {a}")
        exp *= 10
        pass_num += 1
        
    return a


def main():
    print("=" * 65)
    print("  DAA OFFLINE LAB 3: RADIX SORT (LSD APPROACH)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)
    
    # PDF Section B Question 6 sample: [170, 45, 75, 90, 802, 24, 2, 66]
    sample = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"Sample Input Array: {sample}")
    
    sorted_res = radix_sort(sample)
    print(f"\nFinal Sorted Result: {sorted_res}")
    print("=" * 65)


if __name__ == "__main__":
    main()
