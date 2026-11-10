"""
Program: basic_sorts.py
Description: Implements and visualizes Bubble Sort, Selection Sort, and Insertion Sort.
             Prints the array after every pass or step so the sorting process
             is clearly visible.
Student: Khushi Dixit | Roll No: IC-2K23-51
Lab: DAA Offline Lab 3 (Section C.1)
"""

def bubble_sort(arr):
    """
    Bubble sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order.
    Returns: a new sorted list (does not mutate original).
    """
    a = list(arr)
    n = len(a)
    print(f"\n--- Bubble Sort Trace on {a} ---")
    step = 0
    for i in range(n):
        swapped = False
        print(f"Pass {i + 1}:")
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                step += 1
                swapped = True
                print(f"  Step {step}: Swapped indices {j} and {j+1} -> {a}")
        if not swapped:
            print("  No swaps this pass; array is now sorted early!")
            break
    print(f"Final Sorted Result: {a}")
    return a


def selection_sort(arr):
    """
    Selection sort divides the array into sorted and unsorted regions.
    It repeatedly selects the minimum element from the unsorted region and
    swaps it with the first unsorted element.
    Returns: a new sorted list.
    """
    a = list(arr)
    n = len(a)
    print(f"\n--- Selection Sort Trace on {a} ---")
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            print(f"  Pass {i + 1}: Min element {a[i]} swapped into index {i} -> {a}")
        else:
            print(f"  Pass {i + 1}: Element {a[i]} already at correct index {i} -> {a}")
    print(f"Final Sorted Result: {a}")
    return a


def insertion_sort(arr):
    """
    Insertion sort builds the sorted list one element at a time by repeatedly
    taking the next element and shifting larger sorted elements to the right.
    Returns: a new sorted list.
    """
    a = list(arr)
    n = len(a)
    print(f"\n--- Insertion Sort Trace on {a} ---")
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        print(f"  Step {i}: Inserted key {key} at index {j + 1} -> {a}")
    print(f"Final Sorted Result: {a}")
    return a


def main():
    print("=" * 65)
    print("  DAA OFFLINE LAB 3: BUBBLE, SELECTION & INSERTION SORTS")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)
    
    # PDF Section B sample array: [5, 2, 8, 1, 9]
    sample = [5, 2, 8, 1, 9]
    print(f"Initial Test Array: {sample}")
    
    bubble_res = bubble_sort(sample)
    selection_res = selection_sort(sample)
    insertion_res = insertion_sort(sample)
    
    print("\n" + "=" * 65)
    print("Verification Summary:")
    print(f"  Original Input : {sample}")
    print(f"  Bubble Sort    : {bubble_res}")
    print(f"  Selection Sort : {selection_res}")
    print(f"  Insertion Sort : {insertion_res}")
    print("=" * 65)


if __name__ == "__main__":
    main()
