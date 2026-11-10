"""
Program: student_record_manager.py
Description: Student Record Manager application:
             - Stores records with roll number, name, and marks
             - Sorts by roll number, name, or marks using user-selected algorithm
             - Searches for a student by roll number using iterative Binary Search
             - Compares sorting algorithms and generates performance report
Student: Khushi Dixit | Roll No: IC-2K23-51
Lab: DAA Offline Lab 3 (Section E.7)
"""

import time
import copy

# Sorting algorithms adaptable by key extractor function

def bubble_sort(arr, key_fn):
    a = copy.deepcopy(arr)
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if key_fn(a[j]) > key_fn(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def selection_sort(arr, key_fn):
    a = copy.deepcopy(arr)
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if key_fn(a[j]) < key_fn(a[min_idx]):
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a


def insertion_sort(arr, key_fn):
    a = copy.deepcopy(arr)
    n = len(a)
    for i in range(1, n):
        key_item = a[i]
        key_val = key_fn(key_item)
        j = i - 1
        while j >= 0 and key_fn(a[j]) > key_val:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key_item
    return a


def merge_sort(arr, key_fn):
    if len(arr) <= 1:
        return copy.deepcopy(arr)
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key_fn)
    right = merge_sort(arr[mid:], key_fn)
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key_fn(left[i]) <= key_fn(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(arr, key_fn):
    a = copy.deepcopy(arr)
    def _qs(low, high):
        if low < high:
            pivot_val = key_fn(a[high])
            i = low - 1
            for j in range(low, high):
                if key_fn(a[j]) <= pivot_val:
                    i += 1
                    a[i], a[j] = a[j], a[i]
            a[i + 1], a[high] = a[high], a[i + 1]
            p_idx = i + 1
            _qs(low, p_idx - 1)
            _qs(p_idx + 1, high)
    _qs(0, len(a) - 1)
    return a


def heap_sort(arr, key_fn):
    a = copy.deepcopy(arr)
    n = len(a)
    def heapify(size, root):
        largest = root
        l = 2 * root + 1
        r = 2 * root + 2
        if l < size and key_fn(a[l]) > key_fn(a[largest]):
            largest = l
        if r < size and key_fn(a[r]) > key_fn(a[largest]):
            largest = r
        if largest != root:
            a[root], a[largest] = a[largest], a[root]
            heapify(size, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(i, 0)
    return a


def binary_search_by_roll(records_sorted_by_roll, target_roll):
    """
    Binary search for student record by roll number on sorted records.
    """
    low = 0
    high = len(records_sorted_by_roll) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        mid_roll = records_sorted_by_roll[mid]["roll_no"]
        if mid_roll == target_roll:
            return records_sorted_by_roll[mid], steps
        elif mid_roll < target_roll:
            low = mid + 1
        else:
            high = mid - 1
    return None, steps


def display_records(records, title="Student Records"):
    print(f"\n{title}:")
    print(f"  {'Roll No':<10} | {'Name':<22} | {'Marks':<6}")
    print("  " + "-" * 44)
    for r in records:
        print(f"  {r['roll_no']:<10} | {r['name']:<22} | {r['marks']:<6.1f}")


def run_comparative_performance_report(records):
    print("\n" + "=" * 65)
    print("COMPARATIVE SORTING PERFORMANCE REPORT ON STUDENT DATASET")
    print("=" * 65)
    algos = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort)
    ]
    
    # Sort by marks descending/ascending
    key_fn = lambda x: x["marks"]
    timings = {}
    
    # Expand dataset to 500 records to measure distinct timings
    benchmark_dataset = records * 25  # 20 * 25 = 500 records
    
    for name, func in algos:
        t0 = time.perf_counter()
        _ = func(benchmark_dataset, key_fn)
        elapsed_ms = (time.perf_counter() - t0) * 1000.0
        timings[name] = elapsed_ms
        print(f"  {name:<16} : {elapsed_ms:>8.3f} ms")
        
    fastest = min(timings.items(), key=lambda x: x[1])
    slowest = max(timings.items(), key=lambda x: x[1])
    diff = slowest[1] - fastest[1]
    factor = slowest[1] / fastest[1] if fastest[1] > 0 else 1.0
    
    print("-" * 65)
    print(f"Fastest Algorithm : {fastest[0]} ({fastest[1]:.3f} ms)")
    print(f"Slowest Algorithm : {slowest[0]} ({slowest[1]:.3f} ms)")
    print(f"Difference        : {diff:.3f} ms ({factor:.1f}x speed difference)")
    print("=" * 65)


def get_default_students():
    return [
        {"roll_no": 105, "name": "Khushi Dixit",    "marks": 94.5},
        {"roll_no": 101, "name": "Aarav Sharma",    "marks": 82.0},
        {"roll_no": 118, "name": "Zoya Khan",       "marks": 91.0},
        {"roll_no": 103, "name": "Bhavya Patel",    "marks": 76.5},
        {"roll_no": 112, "name": "Rohan Verma",     "marks": 88.0},
        {"roll_no": 107, "name": "Isha Sen",        "marks": 95.0},
        {"roll_no": 120, "name": "Vikram Singh",    "marks": 69.0},
        {"roll_no": 109, "name": "Meera Joshi",     "marks": 84.5},
        {"roll_no": 115, "name": "Tanmay Roy",      "marks": 79.0},
        {"roll_no": 102, "name": "Ananya Gupta",    "marks": 92.5},
        {"roll_no": 114, "name": "Siddharth Rao",   "marks": 86.0},
        {"roll_no": 108, "name": "Karan Malhotra",  "marks": 74.0},
        {"roll_no": 116, "name": "Urvi Choudhury",  "marks": 89.5},
        {"roll_no": 104, "name": "Chirag Sethi",    "marks": 81.0},
        {"roll_no": 110, "name": "Nikhil Kapoor",   "marks": 78.5},
        {"roll_no": 117, "name": "Vidhi Mehta",     "marks": 90.0},
        {"roll_no": 106, "name": "Devansh Nair",    "marks": 87.0},
        {"roll_no": 111, "name": "Pooja Hegde",     "marks": 83.5},
        {"roll_no": 119, "name": "Yashwant Das",    "marks": 77.0},
        {"roll_no": 113, "name": "Sneha Iyer",      "marks": 96.0}
    ]


def main():
    print("=" * 65)
    print("  DAA OFFLINE LAB 3: STUDENT RECORD MANAGER")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)
    
    records = get_default_students()
    display_records(records, "Loaded Student Records (Unsorted)")
    
    # Store records sorted by roll number for binary search
    records_by_roll = merge_sort(records, lambda x: x["roll_no"])
    
    while True:
        print("\n--- Student Record Manager Menu ---")
        print("1. Display All Student Records")
        print("2. Sort Records (by Roll Number / Name / Marks)")
        print("3. Search Student by Roll Number (Binary Search)")
        print("4. Comparative Sorting Performance Report")
        print("5. Run Automated Comprehensive Test")
        print("6. Exit")
        
        choice = input("Enter option (1-6): ").strip()
        
        if choice == "1":
            display_records(records)
            
        elif choice == "2":
            print("\nSelect Attribute to Sort By:")
            print("  1. Roll Number")
            print("  2. Name")
            print("  3. Marks")
            attr_c = input("Choice (1-3): ").strip()
            if attr_c == "1":
                key_fn = lambda x: x["roll_no"]
                attr_name = "Roll Number"
            elif attr_c == "2":
                key_fn = lambda x: x["name"]
                attr_name = "Name"
            elif attr_c == "3":
                key_fn = lambda x: x["marks"]
                attr_name = "Marks"
            else:
                print("Invalid attribute selection.")
                continue
                
            print("\nSelect Algorithm:")
            print("  1. Bubble Sort    2. Selection Sort    3. Insertion Sort")
            print("  4. Merge Sort     5. Quick Sort        6. Heap Sort")
            algo_c = input("Choice (1-6): ").strip()
            
            algo_dict = {
                "1": ("Bubble Sort", bubble_sort),
                "2": ("Selection Sort", selection_sort),
                "3": ("Insertion Sort", insertion_sort),
                "4": ("Merge Sort", merge_sort),
                "5": ("Quick Sort", quick_sort),
                "6": ("Heap Sort", heap_sort)
            }
            if algo_c in algo_dict:
                name, algo_func = algo_dict[algo_c]
                t0 = time.perf_counter()
                sorted_res = algo_func(records, key_fn)
                elapsed_ms = (time.perf_counter() - t0) * 1000.0
                display_records(sorted_res, f"Records Sorted by {attr_name} using {name} ({elapsed_ms:.3f} ms)")
            else:
                print("Invalid algorithm choice.")
                
        elif choice == "3":
            try:
                target_r = int(input("Enter Roll Number to search: "))
                rec, steps = binary_search_by_roll(records_by_roll, target_r)
                if rec:
                    print(f"\n=> Student Found in {steps} step(s):")
                    print(f"   Roll No: {rec['roll_no']} | Name: {rec['name']} | Marks: {rec['marks']}")
                else:
                    print(f"\n=> Roll No {target_r} not found (searched {steps} steps).")
            except ValueError:
                print("Error: Roll number must be an integer.")
                
        elif choice == "4":
            run_comparative_performance_report(records)
            
        elif choice == "5":
            print("\n>>> Running Automated Demonstration <<<")
            # 1. Sort by marks using Quick Sort
            s_marks = quick_sort(records, lambda x: x["marks"])
            display_records(s_marks[:5], "Top 5 Records Sorted by Marks (Quick Sort)")
            
            # 2. Binary search test
            target = 105  # Khushi Dixit
            found, steps = binary_search_by_roll(records_by_roll, target)
            print(f"\nBinary Search for Roll No {target}: Found: {found['name']} in {steps} steps.")
            
            # 3. Missing search test
            missing_target = 999
            not_found, steps = binary_search_by_roll(records_by_roll, missing_target)
            print(f"Binary Search for Roll No {missing_target}: Result: {not_found} in {steps} steps.")
            
            # 4. Run benchmark
            run_comparative_performance_report(records)
            print(">>> Automated Demonstration Completed <<<")
            
        elif choice == "6":
            print("Exiting Student Record Manager.")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
