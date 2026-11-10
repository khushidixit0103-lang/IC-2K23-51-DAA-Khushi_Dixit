"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 02: Divide and Conquer
Experiment: Strassen's Matrix Multiplication

Problem Statement:
Multiply two n x n square matrices using Strassen's Divide and Conquer algorithm.
Reduces scalar multiplications from 8 to 7, achieving O(n^2.807) time complexity.
Handles non-power-of-2 dimensions via zero-padding.
"""

def standard_matrix_multiply(A, B):
    """Conventional O(n^3) matrix multiplication for verification."""
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def matrix_add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def matrix_subtract(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def next_power_of_two(n):
    """Returns the smallest power of 2 >= n."""
    p = 1
    while p < n:
        p *= 2
    return p


def pad_matrix(M, target_size):
    """Pads matrix M with zeros to target_size x target_size."""
    orig_rows = len(M)
    orig_cols = len(M[0])
    padded = [[0] * target_size for _ in range(target_size)]
    for i in range(orig_rows):
        for j in range(orig_cols):
            padded[i][j] = M[i][j]
    return padded


def unpad_matrix(M, orig_rows, orig_cols):
    """Extracts original matrix dimensions from padded matrix."""
    return [[M[i][j] for j in range(orig_cols)] for i in range(orig_rows)]


def strassen_recursive(A, B):
    """Recursive Strassen multiplication for 2^k x 2^k matrices."""
    n = len(A)
    
    # Base case: 1x1 matrix or small threshold for performance
    if n <= 2:
        return standard_matrix_multiply(A, B)
        
    mid = n // 2
    
    # Partition matrices into 4 quadrants of size (n/2) x (n/2)
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]
    
    # Compute the 7 Strassen products:
    # M1 = (A11 + A22) * (B11 + B22)
    M1 = strassen_recursive(matrix_add(A11, A22), matrix_add(B11, B22))
    # M2 = (A21 + A22) * B11
    M2 = strassen_recursive(matrix_add(A21, A22), B11)
    # M3 = A11 * (B12 - B22)
    M3 = strassen_recursive(A11, matrix_subtract(B12, B22))
    # M4 = A22 * (B21 - B11)
    M4 = strassen_recursive(A22, matrix_subtract(B21, B11))
    # M5 = (A11 + A12) * B22
    M5 = strassen_recursive(matrix_add(A11, A12), B22)
    # M6 = (A21 - A11) * (B11 + B12)
    M6 = strassen_recursive(matrix_subtract(A21, A11), matrix_add(B11, B12))
    # M7 = (A12 - A22) * (B21 + B22)
    M7 = strassen_recursive(matrix_subtract(A12, A22), matrix_add(B21, B22))
    
    # Calculate quadrants of product matrix C:
    # C11 = M1 + M4 - M5 + M7
    C11 = matrix_add(matrix_subtract(matrix_add(M1, M4), M5), M7)
    # C12 = M3 + M5
    C12 = matrix_add(M3, M5)
    # C21 = M2 + M4
    C21 = matrix_add(M2, M4)
    # C22 = M1 - M2 + M3 + M6
    C22 = matrix_add(matrix_add(matrix_subtract(M1, M2), M3), M6)
    
    # Combine the 4 quadrants into single result matrix C
    C = [[0] * n for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]
            
    return C


def strassen_multiply(A, B):
    """
    Public entry point for Strassen's algorithm.
    Handles dimension checking and zero-padding.
    """
    n = len(A)
    p = next_power_of_two(n)
    
    if p != n:
        A_pad = pad_matrix(A, p)
        B_pad = pad_matrix(B, p)
        C_pad = strassen_recursive(A_pad, B_pad)
        return unpad_matrix(C_pad, n, n)
    else:
        return strassen_recursive(A, B)


def print_matrix(M, name=""):
    if name:
        print(f"Matrix {name}:")
    for row in M:
        print("  [" + ", ".join(f"{val:4d}" for val in row) + "]")


def main():
    print("=" * 65)
    print("  IC-709 B: UNIT 2 - STRASSEN'S MATRIX MULTIPLICATION")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)
    
    # Test 1: 4x4 matrix (power of 2)
    A1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 1, 2, 3],
        [4, 5, 6, 7]
    ]
    B1 = [
        [7, 6, 5, 4],
        [3, 2, 1, 0],
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
    
    print("\n--- Test 1: 4x4 Matrix (Power of 2) ---")
    print_matrix(A1, "A (4x4)")
    print_matrix(B1, "B (4x4)")
    
    C_strassen1 = strassen_multiply(A1, B1)
    C_std1 = standard_matrix_multiply(A1, B1)
    
    print_matrix(C_strassen1, "C (Strassen Result)")
    is_correct1 = (C_strassen1 == C_std1)
    print(f"Correctness vs Standard O(n^3): {'PASSED' if is_correct1 else 'FAILED'}")
    
    # Test 2: 3x3 matrix (requires zero-padding to 4x4)
    A2 = [
        [2, 3, 1],
        [4, 0, 5],
        [1, 6, 2]
    ]
    B2 = [
        [1, 2, 4],
        [3, 1, 0],
        [5, 2, 3]
    ]
    
    print("\n--- Test 2: 3x3 Matrix (Padded to 4x4) ---")
    print_matrix(A2, "A (3x3)")
    print_matrix(B2, "B (3x3)")
    
    C_strassen2 = strassen_multiply(A2, B2)
    C_std2 = standard_matrix_multiply(A2, B2)
    
    print_matrix(C_strassen2, "C (Strassen Result)")
    is_correct2 = (C_strassen2 == C_std2)
    print(f"Correctness vs Standard O(n^3): {'PASSED' if is_correct2 else 'FAILED'}")
    
    print("\n" + "=" * 65)


if __name__ == "__main__":
    main()
