"""
Program: sparse_matrix.py
Description: Demonstrates Sparse Matrix Representation and Operations:
             - Converts full 2D matrix into sparse triple representation (row, col, value)
             - Reconstructs full 2D matrix from sparse triples
             - Adds two matrices directly in sparse triple form without converting to full
             - Displays and compares sparse form vs reconstructed full form
             - Performs Space Optimization Analysis (Section D questions)
Student: Khushi Dixit | Roll No: IC-2K23-51
Lab: DAA Offline Lab 2 (Section C.3 & Section D)
"""

def matrix_to_sparse(matrix):
    """
    Converts full 2D matrix into sparse representation.
    Header: [total_rows, total_cols, total_non_zero_elements]
    Entries: [[r, c, val], ...]
    """
    if not matrix or len(matrix) == 0:
        return {'rows': 0, 'cols': 0, 'non_zero': 0, 'triples': []}
        
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    triples = []
    
    for r in range(num_rows):
        for c in range(num_cols):
            val = matrix[r][c]
            if val != 0:
                triples.append([r, c, val])
                
    return {
        'rows': num_rows,
        'cols': num_cols,
        'non_zero': len(triples),
        'triples': triples
    }


def sparse_to_matrix(sparse_dict):
    """
    Reconstructs full 2D matrix from sparse representation.
    """
    num_rows = sparse_dict['rows']
    num_cols = sparse_dict['cols']
    
    # Initialize zero matrix
    matrix = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    
    for r, c, val in sparse_dict['triples']:
        if 0 <= r < num_rows and 0 <= c < num_cols:
            matrix[r][c] = val
            
    return matrix


def add_sparse_matrices(sparse_a, sparse_b):
    """
    Adds two sparse matrices directly in sparse triple form.
    Does NOT convert either operand to a full matrix.
    Both input sparse matrices must have matching row and column dimensions.
    """
    if sparse_a['rows'] != sparse_b['rows'] or sparse_a['cols'] != sparse_b['cols']:
        print("Error: Matrix dimensions incompatible for addition.")
        return None
        
    triples_a = sparse_a['triples']
    triples_b = sparse_b['triples']
    
    i = 0
    j = 0
    result_triples = []
    
    while i < len(triples_a) and j < len(triples_b):
        r1, c1, val1 = triples_a[i]
        r2, c2, val2 = triples_b[j]
        
        # Compare row-major ordering
        if r1 < r2 or (r1 == r2 and c1 < c2):
            result_triples.append([r1, c1, val1])
            i += 1
        elif r2 < r1 or (r1 == r2 and c2 < c1):
            result_triples.append([r2, c2, val2])
            j += 1
        else:
            # Same position (r1 == r2 and c1 == c2): add values
            sum_val = val1 + val2
            if sum_val != 0:
                result_triples.append([r1, c1, sum_val])
            i += 1
            j += 1
            
    # Append remaining elements
    while i < len(triples_a):
        result_triples.append(triples_a[i])
        i += 1
    while j < len(triples_b):
        result_triples.append(triples_b[j])
        j += 1
        
    return {
        'rows': sparse_a['rows'],
        'cols': sparse_a['cols'],
        'non_zero': len(result_triples),
        'triples': result_triples
    }


def display_sparse(sparse_dict, name="Sparse Matrix"):
    print(f"\n{name} (Sparse Triple Format):")
    print(f"  Dimensions: {sparse_dict['rows']} x {sparse_dict['cols']} | Non-zero Count: {sparse_dict['non_zero']}")
    print(f"  {'Row':<6} | {'Column':<8} | {'Value':<8}")
    print("  " + "-" * 28)
    for r, c, val in sparse_dict['triples']:
        print(f"  {r:<6} | {c:<8} | {val:<8}")
    if not sparse_dict['triples']:
        print("  (All elements are zero)")


def display_full_matrix(mat, name="Full 2D Matrix"):
    print(f"\n{name}:")
    if not mat:
        print("  []")
        return
    for row in mat:
        print("  [ " + " ".join(f"{x:>4}" for x in row) + " ]")


def run_space_optimization_analysis():
    print("\n" + "=" * 65)
    print("SECTION D: SPACE OPTIMIZATION ANALYSIS EXPERIMENT")
    print("=" * 65)
    
    # 6x6 Matrix 1: ~80% zeros (roughly 7 non-zeros out of 36 elements -> ~80.5% zeros)
    mat_sparse_80 = [
        [0, 0, 5, 0, 0, 0],
        [0, 0, 0, 8, 0, 0],
        [3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 12],
        [0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0]
    ]
    
    # 6x6 Matrix 2: <20% zeros (dense: 30 non-zeros out of 36 elements -> ~16.7% zeros)
    mat_dense = [
        [1,  2,  3,  4,  5,  0],
        [7,  8,  9,  0, 11, 12],
        [13, 14, 0, 16, 17, 18],
        [19, 0, 21, 22, 23, 24],
        [0, 26, 27, 28, 29, 30],
        [31, 32, 33, 34, 0, 36]
    ]
    
    sp1 = matrix_to_sparse(mat_sparse_80)
    sp2 = matrix_to_sparse(mat_dense)
    
    print("\n1. Matrix 1 (~80% zeros):")
    total_elements_1 = 6 * 6
    k1 = sp1['non_zero']
    space_full_1 = total_elements_1
    space_sparse_1 = 3 * k1
    print(f"   - Dimensions: 6 x 6 = {total_elements_1} elements")
    print(f"   - Non-zero elements (k): {k1}")
    print(f"   - Zero percentage: {((total_elements_1 - k1) / total_elements_1) * 100:.1f}%")
    print(f"   - Full 2D storage: {space_full_1} integer slots")
    print(f"   - Sparse triple storage (3 * k): {space_sparse_1} integer slots")
    print(f"   - Space Saved: {space_full_1 - space_sparse_1} slots ({((space_full_1 - space_sparse_1)/space_full_1)*100:.1f}% savings)")
    
    print("\n2. Matrix 2 (<20% zeros - Dense Matrix):")
    total_elements_2 = 6 * 6
    k2 = sp2['non_zero']
    space_full_2 = total_elements_2
    space_sparse_2 = 3 * k2
    print(f"   - Dimensions: 6 x 6 = {total_elements_2} elements")
    print(f"   - Non-zero elements (k): {k2}")
    print(f"   - Zero percentage: {((total_elements_2 - k2) / total_elements_2) * 100:.1f}%")
    print(f"   - Full 2D storage: {space_full_2} integer slots")
    print(f"   - Sparse triple storage (3 * k): {space_sparse_2} integer slots")
    print(f"   - Space Overhead in Sparse: {space_sparse_2 - space_full_2} extra slots ({((space_sparse_2 - space_full_2)/space_full_2)*100:.1f}% penalty)")
    
    print("\n3. Space Optimization Threshold:")
    print("   Sparse storage requires 3 numbers per entry (row, col, value).")
    print("   Space equality equation: 3 * k = m * n  =>  k / (m * n) = 1/3 ~ 33.33%")
    print("   => Conclusion: When non-zero elements exceed ~33.3%, sparse representation")
    print("      consumes MORE memory than standard 2D representation due to index overhead.")


def main():
    print("=" * 65)
    print("  DAA OFFLINE LAB 2: SPARSE MATRIX REPRESENTATION & OPERATIONS")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)
    
    # PDF Matrix D
    matrix_d = [
        [0, 0, 5],
        [0, 8, 0],
        [3, 0, 0],
        [0, 0, 0]
    ]
    
    display_full_matrix(matrix_d, "Matrix D (Input Full 2D)")
    sparse_d = matrix_to_sparse(matrix_d)
    display_sparse(sparse_d, "Matrix D")
    
    reconstructed_d = sparse_to_matrix(sparse_d)
    display_full_matrix(reconstructed_d, "Matrix D (Reconstructed from Sparse Triples)")
    
    # Demonstrate Direct Sparse Addition
    print("\n" + "-" * 55)
    print("DIRECT SPARSE ADDITION DEMONSTRATION")
    print("-" * 55)
    matrix_e = [
        [1, 0, 2],
        [0, 3, 0],
        [4, 0, 0],
        [0, 0, 7]
    ]
    sparse_e = matrix_to_sparse(matrix_e)
    display_full_matrix(matrix_e, "Matrix E (Second Matrix)")
    display_sparse(sparse_e, "Matrix E")
    
    sparse_sum = add_sparse_matrices(sparse_d, sparse_e)
    display_sparse(sparse_sum, "Matrix Sum (D + E, Computed Directly in Sparse Form)")
    
    reconstructed_sum = sparse_to_matrix(sparse_sum)
    display_full_matrix(reconstructed_sum, "Matrix Sum (Reconstructed Full 2D)")
    
    # Run Section D Space Analysis
    run_space_optimization_analysis()
    print("=" * 65)


if __name__ == "__main__":
    main()
