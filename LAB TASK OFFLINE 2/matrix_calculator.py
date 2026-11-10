"""
Program: matrix_calculator.py
Description: Menu-driven Matrix Calculator:
             - Add two matrices (with dimension compatibility check)
             - Multiply two matrices (columns of A == rows of B check)
             - Transpose a matrix
             - Find determinant of a square matrix (2x2, 3x3, and recursive nxn)
             - Clear input validation and readable row-by-row matrix display
Student: Khushi Dixit | Roll No: IC-2K23-51
Lab: DAA Offline Lab 2 (Section C.4)
"""

def print_matrix(mat, name="Matrix"):
    print(f"\n{name}:")
    if not mat:
        print("  []")
        return
    for row in mat:
        print("  [ " + " ".join(f"{val:>6}" for val in row) + " ]")


def input_matrix(name="Matrix"):
    print(f"\n--- Input for {name} ---")
    try:
        r = int(input(f"Enter number of rows for {name}: "))
        c = int(input(f"Enter number of columns for {name}: "))
        if r <= 0 or c <= 0:
            print("Error: Dimensions must be positive integers.")
            return None
        
        mat = []
        print(f"Enter elements row by row ({c} space-separated numbers per row):")
        for i in range(r):
            row_raw = input(f"  Row {i}: ").strip()
            row_vals = [float(x) for x in row_raw.split()]
            if len(row_vals) != c:
                print(f"Error: Expected {c} values, got {len(row_vals)}.")
                return None
            mat.append(row_vals)
        return mat
    except ValueError:
        print("Error: Invalid numeric input.")
        return None


def add_matrices(mat_a, mat_b):
    if len(mat_a) != len(mat_b) or len(mat_a[0]) != len(mat_b[0]):
        print(f"Error: Incompatible dimensions for addition. "
              f"Matrix A is ({len(mat_a)}x{len(mat_a[0])}) while "
              f"Matrix B is ({len(mat_b)}x{len(mat_b[0])}).")
        return None
        
    rows = len(mat_a)
    cols = len(mat_a[0])
    result = [[mat_a[r][c] + mat_b[r][c] for c in range(cols)] for r in range(rows)]
    return result


def multiply_matrices(mat_a, mat_b):
    rows_a = len(mat_a)
    cols_a = len(mat_a[0])
    rows_b = len(mat_b)
    cols_b = len(mat_b[0])
    
    if cols_a != rows_b:
        print(f"Error: Incompatible dimensions for multiplication. "
              f"Columns of A ({cols_a}) must equal Rows of B ({rows_b}).")
        return None
        
    result = [[0.0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            result[i][j] = sum(mat_a[i][k] * mat_b[k][j] for k in range(cols_a))
    return result


def transpose_matrix(mat):
    if not mat:
        return []
    rows = len(mat)
    cols = len(mat[0])
    trans = [[mat[r][c] for r in range(rows)] for c in range(cols)]
    return trans


def get_submatrix(mat, skip_row, skip_col):
    return [[mat[r][c] for c in range(len(mat[r])) if c != skip_col]
            for r in range(len(mat)) if r != skip_row]


def determinant(mat):
    rows = len(mat)
    cols = len(mat[0])
    if rows != cols:
        print(f"Error: Matrix is not square ({rows}x{cols}). Determinant cannot be computed.")
        return None
        
    # Base cases
    if rows == 1:
        return mat[0][0]
    if rows == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    if rows == 3:
        # Standard Sarrus / 3x3 expansion
        a, b, c = mat[0][0], mat[0][1], mat[0][2]
        d_1 = a * (mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1])
        d_2 = b * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0])
        d_3 = c * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0])
        return d_1 - d_2 + d_3
        
    # Recursive cofactor expansion for n x n
    det_val = 0.0
    for col in range(cols):
        sign = 1 if col % 2 == 0 else -1
        submat = get_submatrix(mat, 0, col)
        det_val += sign * mat[0][col] * determinant(submat)
    return det_val


def run_automated_demo():
    print("\n>>> RUNNING AUTOMATED COMPREHENSIVE TESTS <<<")
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    print_matrix(m1, "Matrix 1 (2x2)")
    print_matrix(m2, "Matrix 2 (2x2)")
    
    print("\n[Test 1] Addition:")
    res_add = add_matrices(m1, m2)
    print_matrix(res_add, "Matrix 1 + Matrix 2")
    
    print("\n[Test 2] Multiplication:")
    res_mul = multiply_matrices(m1, m2)
    print_matrix(res_mul, "Matrix 1 x Matrix 2")
    
    print("\n[Test 3] Transpose:")
    m3 = [[1, 2, 3], [4, 5, 6]]
    print_matrix(m3, "Matrix 3 (2x3)")
    res_trans = transpose_matrix(m3)
    print_matrix(res_trans, "Transpose of Matrix 3 (3x2)")
    
    print("\n[Test 4] Determinant 2x2:")
    d2 = determinant(m1)
    print(f"det(Matrix 1) = {d2} (Expected: 1*4 - 2*3 = -2)")
    
    print("\n[Test 5] Determinant 3x3:")
    m_3x3 = [
        [6, 1, 1],
        [4, -2, 5],
        [2, 8, 7]
    ]
    print_matrix(m_3x3, "Matrix (3x3)")
    d3 = determinant(m_3x3)
    print(f"det(Matrix 3x3) = {d3} (Expected: -306)")
    
    print("\n[Test 6] Boundary: Incompatible addition dimensions:")
    add_matrices(m1, m3)
    
    print("\n[Test 7] Boundary: Incompatible multiplication dimensions:")
    m4 = [[1, 2], [3, 4], [5, 6]]
    multiply_matrices(m1, m4)
    
    print("\n[Test 8] Boundary: Determinant of non-square matrix:")
    determinant(m3)
    print(">>> Finished Automated Tests <<<\n")


def main():
    print("=" * 60)
    print("  DAA OFFLINE LAB 2: MATRIX CALCULATOR")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 60)
    
    while True:
        print("\n--- Matrix Calculator Menu ---")
        print("1. Add two matrices")
        print("2. Multiply two matrices")
        print("3. Transpose a matrix")
        print("4. Find the determinant of a matrix")
        print("5. Run automated demonstration test suite")
        print("6. Exit")
        
        choice = input("Enter option (1-6): ").strip()
        
        if choice == "1":
            print("\nEnter Matrix A:")
            a = input_matrix("A")
            if a:
                print("\nEnter Matrix B:")
                b = input_matrix("B")
                if b:
                    res = add_matrices(a, b)
                    if res is not None:
                        print_matrix(res, "Result: Matrix A + Matrix B")
                        
        elif choice == "2":
            print("\nEnter Matrix A:")
            a = input_matrix("A")
            if a:
                print("\nEnter Matrix B:")
                b = input_matrix("B")
                if b:
                    res = multiply_matrices(a, b)
                    if res is not None:
                        print_matrix(res, "Result: Matrix A x Matrix B")
                        
        elif choice == "3":
            a = input_matrix("Target Matrix")
            if a:
                res = transpose_matrix(a)
                print_matrix(res, "Result: Transposed Matrix")
                
        elif choice == "4":
            a = input_matrix("Target Matrix")
            if a:
                det = determinant(a)
                if det is not None:
                    print(f"\n=> Determinant of the matrix = {det}")
                    
        elif choice == "5":
            run_automated_demo()
            
        elif choice == "6":
            print("Exiting Matrix Calculator.")
            break
        else:
            print("Invalid option. Please choose between 1 and 6.")


if __name__ == "__main__":
    main()
