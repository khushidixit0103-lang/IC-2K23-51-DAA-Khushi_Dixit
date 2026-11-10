"""
Program: array_1d_operations.py
Description: Interactive program for 1D array operations:
             - Insert value at index
             - Delete value at index
             - Linear search with index or not-found message
             - Rotate left by k positions
             - Rotate right by k positions
             Displays the array after every operation with input validation.
Student: Khushi Dixit | Roll No: IC-2K23-51
Lab: DAA Offline Lab 2 (Section C.1)
"""

def display_array(arr, message="Current Array"):
    print(f"{message}: {arr} (Length: {len(arr)})")


def insert_element(arr, index, value):
    if index < 0 or index > len(arr):
        print(f"Error: Invalid index {index}. Valid range is 0 to {len(arr)}.")
        return False
    arr.insert(index, value)
    print(f"Success: Inserted value {value} at index {index}.")
    return True


def delete_element(arr, index):
    if not arr:
        print("Error: Cannot delete from an empty array.")
        return False
    if index < 0 or index >= len(arr):
        print(f"Error: Invalid index {index}. Valid range is 0 to {len(arr) - 1}.")
        return False
    removed = arr.pop(index)
    print(f"Success: Deleted value {removed} from index {index}.")
    return True


def linear_search(arr, target):
    if not arr:
        print("Array is empty. Target not found.")
        return -1
    for i, val in enumerate(arr):
        if val == target:
            print(f"Success: Element {target} found at index {i}.")
            return i
    print(f"Notice: Element {target} was NOT found in the array.")
    return -1


def rotate_left(arr, k):
    n = len(arr)
    if n == 0:
        print("Notice: Array is empty, rotation has no effect.")
        return
    k = k % n
    if k == 0:
        print("Rotated by 0 positions (no change).")
        return
    # In-place slice or list reconstruction
    arr[:] = arr[k:] + arr[:k]
    print(f"Success: Rotated array left by {k} positions.")


def rotate_right(arr, k):
    n = len(arr)
    if n == 0:
        print("Notice: Array is empty, rotation has no effect.")
        return
    k = k % n
    if k == 0:
        print("Rotated by 0 positions (no change).")
        return
    arr[:] = arr[-k:] + arr[:-k]
    print(f"Success: Rotated array right by {k} positions.")


def run_interactive_or_demo():
    print("=" * 60)
    print("  DAA OFFLINE LAB 2: 1D ARRAY OPERATIONS")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 60)
    
    # Initialize with sample array or allow custom input
    arr = [10, 20, 30, 40, 50]
    display_array(arr, "Initial Array")
    
    while True:
        print("\n--- 1D Array Menu ---")
        print("1. Insert element at index")
        print("2. Delete element at index")
        print("3. Linear search for value")
        print("4. Rotate left by k positions")
        print("5. Rotate right by k positions")
        print("6. Run Automated Comprehensive Test Cases (including boundaries)")
        print("7. Exit")
        
        choice = input("Enter choice (1-7): ").strip()
        
        if choice == "1":
            try:
                idx = int(input("Enter index to insert: "))
                val = int(input("Enter integer value to insert: "))
                insert_element(arr, idx, val)
                display_array(arr)
            except ValueError:
                print("Error: Invalid numeric input.")
                
        elif choice == "2":
            try:
                idx = int(input("Enter index to delete: "))
                delete_element(arr, idx)
                display_array(arr)
            except ValueError:
                print("Error: Invalid numeric input.")
                
        elif choice == "3":
            try:
                val = int(input("Enter value to search: "))
                linear_search(arr, val)
            except ValueError:
                print("Error: Invalid numeric input.")
                
        elif choice == "4":
            try:
                k = int(input("Enter k positions to rotate left: "))
                rotate_left(arr, k)
                display_array(arr)
            except ValueError:
                print("Error: Invalid numeric input.")
                
        elif choice == "5":
            try:
                k = int(input("Enter k positions to rotate right: "))
                rotate_right(arr, k)
                display_array(arr)
            except ValueError:
                print("Error: Invalid numeric input.")
                
        elif choice == "6":
            print("\n>>> Running Automated Boundary & Functionality Tests <<<")
            test_arr = [10, 20, 30, 40, 50]
            display_array(test_arr, "Test Array")
            
            print("\n[Test 1] Insert 25 at index 2:")
            insert_element(test_arr, 2, 25)
            display_array(test_arr)
            
            print("\n[Test 2] Delete element at index 0:")
            delete_element(test_arr, 0)
            display_array(test_arr)
            
            print("\n[Test 3] Rotate left by 2 positions:")
            rotate_left(test_arr, 2)
            display_array(test_arr)
            
            print("\n[Test 4] Rotate right by 1 position:")
            rotate_right(test_arr, 1)
            display_array(test_arr)
            
            print("\n[Test 5] Boundary: Insert at out-of-bounds index 100:")
            insert_element(test_arr, 100, 999)
            
            print("\n[Test 6] Boundary: Delete from out-of-bounds index -5:")
            delete_element(test_arr, -5)
            
            print("\n[Test 7] Search present element 25:")
            linear_search(test_arr, 25)
            
            print("\n[Test 8] Search non-existent element 999:")
            linear_search(test_arr, 999)
            
            print("\n[Test 9] Boundary: Empty array operations:")
            empty = []
            delete_element(empty, 0)
            linear_search(empty, 10)
            rotate_left(empty, 3)
            print("Automated test cases finished.")
            
        elif choice == "7":
            print("Exiting 1D Array program.")
            break
        else:
            print("Invalid option. Please choose between 1 and 7.")


if __name__ == "__main__":
    run_interactive_or_demo()
