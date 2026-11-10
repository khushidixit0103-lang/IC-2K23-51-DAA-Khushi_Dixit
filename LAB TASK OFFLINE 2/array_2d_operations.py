"""
Program: array_2d_operations.py
Description: Interactive program for 2D array operations:
             - Insert a new row at given position
             - Delete a row at given position
             - Search for a value across entire 2D array (returns row and col or not-found)
             - Rotate the entire 2D array 90 degrees clockwise
             Displays array in clean row-by-row matrix format after every operation.
Student: Khushi Dixit | Roll No: IC-2K23-51
Lab: DAA Offline Lab 2 (Section C.2)
"""

def display_matrix(mat, message="Current 2D Array"):
    print(f"\n{message}:")
    if not mat or len(mat) == 0:
        print("  [Empty Matrix []]")
        return
    num_rows = len(mat)
    num_cols = len(mat[0]) if num_rows > 0 else 0
    print(f"  Dimensions: {num_rows} x {num_cols}")
    for r_idx, row in enumerate(mat):
        formatted_row = " ".join(f"{val:>4}" for val in row)
        print(f"  Row {r_idx}: [ {formatted_row} ]")


def insert_row(mat, position, new_row):
    if not mat:
        # Inserting into empty matrix
        mat.append(list(new_row))
        print(f"Success: Inserted row at index 0 in empty matrix.")
        return True
    
    expected_cols = len(mat[0])
    if len(new_row) != expected_cols:
        print(f"Error: Incompatible row length {len(new_row)}. Matrix expects {expected_cols} columns.")
        return False
        
    if position < 0 or position > len(mat):
        print(f"Error: Invalid row position {position}. Valid range is 0 to {len(mat)}.")
        return False
        
    mat.insert(position, list(new_row))
    print(f"Success: Inserted new row at index {position}.")
    return True


def delete_row(mat, position):
    if not mat:
        print("Error: Cannot delete row from an empty matrix.")
        return False
    if position < 0 or position >= len(mat):
        print(f"Error: Invalid row position {position}. Valid range is 0 to {len(mat) - 1}.")
        return False
    removed = mat.pop(position)
    print(f"Success: Deleted row {position}: {removed}.")
    return True


def search_2d(mat, target):
    if not mat:
        print(f"Notice: Matrix is empty. Target {target} not found.")
        return None
        
    found_locations = []
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if mat[r][c] == target:
                found_locations.append((r, c))
                
    if found_locations:
        print(f"Success: Element {target} found at {len(found_locations)} location(s):")
        for r, c in found_locations:
            print(f"  -> Row {r}, Column {c} (0-indexed)")
        return found_locations
    else:
        print(f"Notice: Element {target} was NOT found anywhere in the 2D array.")
        return None


def rotate_90_clockwise(mat):
    if not mat or len(mat) == 0:
        print("Notice: Matrix is empty. Rotation skipped.")
        return []
    
    rows = len(mat)
    cols = len(mat[0])
    
    # Check rectangular / regular shape
    for r in mat:
        if len(r) != cols:
            print("Error: Irregular 2D array cannot be rotated.")
            return mat

    # Clockwise rotation: new row i is reverse of old col i
    rotated = [[mat[rows - 1 - r][c] for r in range(rows)] for c in range(cols)]
    
    # Update mat in-place
    mat.clear()
    mat.extend(rotated)
    print(f"Success: Rotated 2D array 90 degrees clockwise (New dimensions: {cols} x {rows}).")
    return mat


def run_interactive_or_demo():
    print("=" * 60)
    print("  DAA OFFLINE LAB 2: 2D ARRAY OPERATIONS")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 60)
    
    # Initialize 3x3 sample matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    display_matrix(matrix, "Initial 2D Array")
    
    while True:
        print("\n--- 2D Array Menu ---")
        print("1. Insert a new row at given position")
        print("2. Delete a row at given position")
        print("3. Search for a value across 2D array")
        print("4. Rotate entire 2D array 90 degrees clockwise")
        print("5. Run Automated Comprehensive Test Cases (including boundaries)")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == "1":
            try:
                pos = int(input("Enter row index to insert at: "))
                expected = len(matrix[0]) if matrix else "any"
                raw = input(f"Enter row elements separated by space (expecting {expected} items): ")
                row_vals = [int(x) for x in raw.split()]
                insert_row(matrix, pos, row_vals)
                display_matrix(matrix)
            except ValueError:
                print("Error: Invalid numeric input.")
                
        elif choice == "2":
            try:
                pos = int(input("Enter row index to delete: "))
                delete_row(matrix, pos)
                display_matrix(matrix)
            except ValueError:
                print("Error: Invalid numeric input.")
                
        elif choice == "3":
            try:
                val = int(input("Enter integer value to search: "))
                search_2d(matrix, val)
            except ValueError:
                print("Error: Invalid numeric input.")
                
        elif choice == "4":
            rotate_90_clockwise(matrix)
            display_matrix(matrix)
            
        elif choice == "5":
            print("\n>>> Running Automated Boundary & Functionality Tests <<<")
            test_m = [
                [10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]
            ]
            display_matrix(test_m, "Starting Test Matrix")
            
            print("\n[Test 1] Search existing element 50:")
            search_2d(test_m, 50)
            
            print("\n[Test 2] Search non-existent element 999:")
            search_2d(test_m, 999)
            
            print("\n[Test 3] Insert row [15, 25, 35] at index 1:")
            insert_row(test_m, 1, [15, 25, 35])
            display_matrix(test_m)
            
            print("\n[Test 4] Boundary: Incompatible row length [1, 2]:")
            insert_row(test_m, 0, [1, 2])
            
            print("\n[Test 5] Boundary: Out of range row insertion index 50:")
            insert_row(test_m, 50, [1, 2, 3])
            
            print("\n[Test 6] Delete row at index 2:")
            delete_row(test_m, 2)
            display_matrix(test_m)
            
            print("\n[Test 7] Boundary: Out of range delete row index 99:")
            delete_row(test_m, 99)
            
            print("\n[Test 8] Rotate 90 degrees clockwise:")
            rotate_90_clockwise(test_m)
            display_matrix(test_m)
            
            print("\n[Test 9] Boundary: Empty matrix operations:")
            empty = []
            display_matrix(empty, "Empty Matrix")
            delete_row(empty, 0)
            search_2d(empty, 5)
            rotate_90_clockwise(empty)
            print("Automated test cases finished.")
            
        elif choice == "6":
            print("Exiting 2D Array program.")
            break
        else:
            print("Invalid option. Please choose between 1 and 6.")


if __name__ == "__main__":
    run_interactive_or_demo()
