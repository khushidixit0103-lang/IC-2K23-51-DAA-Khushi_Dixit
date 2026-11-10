# Lab Task Offline 2 — Array Operations and Sparse Matrices

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course:** Design and Analysis of Algorithms Lab (IC-709 B)  

---

## Section A: Concept Check Answers
1. In Python, a 1D array is commonly implemented using a **list**.
2. Inserting an element at the beginning of a list requires shifting **all $n$** elements, making it an **$O(n)$** operation.
3. Deleting an element from the middle of a list requires shifting all elements **after (to the right of)** it, to fill the gap.
4. A left rotation by $k$ positions moves the first $k$ elements to the **end (back)** of the array.
5. Linear search checks elements **sequentially (one by one)**, while binary search requires the array to be **sorted** first.
6. A sparse matrix stores only **non-zero** elements, along with their **row indices** and **column indices**.
7. The standard triple format for a sparse matrix entry is **(row, column, value)**.

---

## Section B: Trace the Logic (Step-by-Step)

### Question 1: Array Operations Trace
Given array: `[10, 20, 30, 40, 50]`
1. **Inserting 25 at index 2:**
   - Elements at indices 2, 3, 4 shift right:
   - `[10, 20, 25, 30, 40, 50]`
2. **Deleting element at index 0:**
   - Element `10` is removed; all subsequent elements shift left:
   - `[20, 25, 30, 40, 50]`
3. **Rotating resulting array left by 2 positions:**
   - First 2 elements (`[20, 25]`) move to the back:
   - `[30, 40, 50, 20, 25]`

### Question 2: Linear Search Trace
Target value = `19` on array `[5, 12, 8, 19, 3, 27]`:
- Step 1: Check index 0 $\implies A[0] = 5 \neq 19$
- Step 2: Check index 1 $\implies A[1] = 12 \neq 19$
- Step 3: Check index 2 $\implies A[2] = 8 \neq 19$
- Step 4: Check index 3 $\implies A[3] = 19 = 19 \implies$ **Found at index 3**.

### Question 3: Binary Search Trace
Target value = `15` on sorted array `[2, 4, 7, 10, 15, 20, 22]`:
- Step 1: `low = 0`, `high = 6`, `mid = (0 + 6) // 2 = 3` $\implies A[3] = 10 < 15 \implies low = mid + 1 = 4$
- Step 2: `low = 4`, `high = 6`, `mid = (4 + 6) // 2 = 5` $\implies A[5] = 20 > 15 \implies high = mid - 1 = 4$
- Step 3: `low = 4`, `high = 4`, `mid = (4 + 4) // 2 = 4` $\implies A[4] = 15 == 15 \implies$ **Found at index 4**.

### Question 4: Sparse Triple Representation
Given matrix $D$:
```
D = [[0, 0, 5],
     [0, 8, 0],
     [3, 0, 0],
     [0, 0, 0]]
```
Non-zero entries in row-major order:
1. Row 0, Col 2: `5` $\implies (0, 2, 5)$
2. Row 1, Col 1: `8` $\implies (1, 1, 8)$
3. Row 2, Col 0: `3` $\implies (2, 0, 3)$

Sparse Triples list:
`[(0, 2, 5), (1, 1, 8), (2, 0, 3)]`

### Question 5: Values Stored Comparison
- **Full 2D representation:** $4 \times 3 = 12$ values stored.
- **Sparse representation (triples only):** 3 non-zero entries $\times 3$ components = **9 values** stored.

---

## Section C & E: Program Details and Documentation

### 1. `array_1d_operations.py`
- **Aim:** Implement and validate fundamental 1D array operations including insertion, deletion, linear search, and circular rotations (left and right).
- **Logic:** Insertion uses element shifting to preserve contiguous memory; deletion shifts trailing elements to fill gaps; linear search checks values sequentially in $O(n)$ time; rotation uses modular slice indexing to cycle elements by $k$ offsets.
- **Sample Input / Output:**
  - Initial array: `[10, 20, 30, 40, 50]`
  - Insert 25 at index 2 $\implies [10, 20, 25, 30, 40, 50]$
  - Delete at index 0 $\implies [20, 25, 30, 40, 50]$
  - Rotate left by 2 $\implies [30, 40, 50, 20, 25]$
  - Boundary Test: Insert at index 100 $\implies$ *"Error: Invalid index 100. Valid range is 0 to 5."*
  - Boundary Test: Search 999 $\implies$ *"Notice: Element 999 was NOT found in the array."*

### 2. `array_2d_operations.py`
- **Aim:** Provide full manipulation of 2D matrix arrays including row insertion, row deletion, global coordinate value search, and 90-degree clockwise matrix rotation.
- **Logic:** Row insertion and deletion validate dimension consistency with existing columns; search traverses row and column coordinates in $O(m \times n)$; 90-degree rotation maps element at `(r, c)` to `(c, total_rows - 1 - r)`.
- **Sample Input / Output:**
  - Initial $3 \times 3$: `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
  - Rotate 90° clockwise $\implies$ `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]`
  - Search 5 $\implies$ Found at Row 1, Column 1.
  - Boundary Test: Incompatible row length `[1, 2]` for $3 \times 3$ $\implies$ *"Error: Incompatible row length 2. Matrix expects 3 columns."*

### 3. `sparse_matrix.py`
- **Aim:** Convert between full 2D matrices and sparse triple format $(r, c, v)$, add two matrices directly in sparse form without full-matrix expansion, and benchmark space efficiency.
- **Logic:** Triple conversion scans the matrix and records non-zero tuples; sparse addition uses two-pointer merge traversal over row-major triples, summing values at identical $(r, c)$ coordinates; space analysis calculates empirical memory thresholds.
- **Sample Input / Output:**
  - Matrix D: `[[0, 0, 5], [0, 8, 0], [3, 0, 0], [0, 0, 0]]` $\implies$ Triples: `[(0, 2, 5), (1, 1, 8), (2, 0, 3)]`
  - Matrix E: `[[1, 0, 2], [0, 3, 0], [4, 0, 0], [0, 0, 7]]` $\implies$ Triples: `[(0, 0, 1), (0, 2, 2), (1, 1, 3), (2, 0, 4), (3, 2, 7)]`
  - Direct Sparse Sum (D + E) $\implies$ `[(0, 0, 1), (0, 2, 7), (1, 1, 11), (2, 0, 7), (3, 2, 7)]`
  - Full 2D Reconstructed: `[[1, 0, 7], [0, 11, 0], [7, 0, 0], [0, 0, 7]]`

### 4. `matrix_calculator.py`
- **Aim:** Provide a menu-driven matrix calculator supporting addition, multiplication, transposition, and determinant calculation with dimension checks.
- **Logic:** Validates matching dimensions for addition; requires $col(A) == row(B)$ for matrix product; computes transpose by swapping row/column indices; evaluates determinants for $2 \times 2$ via $ad - bc$ and $n \times n$ via recursive cofactor expansion.
- **Sample Input / Output:**
  - $A = [[1, 2], [3, 4]]$, $B = [[5, 6], [7, 8]]$
  - $A + B = [[6, 8], [10, 12]]$
  - $A \times B = [[19, 22], [43, 50]]$
  - $\det(A) = 1(4) - 2(3) = -2.0$
  - Boundary Test: $\det([[1, 2, 3], [4, 5, 6]])$ $\implies$ *"Error: Matrix is not square (2x3). Determinant cannot be computed."*

---

## Section D: Space Optimization Analysis Answers

1. **Space equations for $m \times n$ matrix with $k$ non-zero elements:**
   - **Full 2D representation:** Space $= m \times n$ storage units.
   - **Sparse triple representation:** Space $= 3 \times k$ storage units (or $3k + 3$ including the header).

2. **Empirical 6x6 Matrix Test:**
   - **Matrix 1 (~80% zeros):**
     - Dimensions: $6 \times 6 = 36$ elements.
     - Non-zero count $k = 7$ (zero percentage = $80.6\%$).
     - Full 2D storage: **36 slots**.
     - Sparse storage ($3k$): **21 slots**.
     - Space Saved: **15 slots (41.7% savings)**.
   - **Matrix 2 (<20% zeros — dense matrix):**
     - Dimensions: $6 \times 6 = 36$ elements.
     - Non-zero count $k = 30$ (zero percentage = $16.7\%$).
     - Full 2D storage: **36 slots**.
     - Sparse storage ($3k$): **90 slots**.
     - Space Penalty: **54 extra slots (150% memory overhead)**.

3. **Break-even percentage:**
   $$3k = m \times n \implies \frac{k}{m \times n} = \frac{1}{3} \approx 33.33\%$$
   The sparse triple representation stops saving space when non-zero elements exceed **$\approx 33.33\%$** of the total matrix capacity. Above this threshold, storing two coordinate indices alongside each value consumes more total memory than simply retaining zero cells in a contiguous 2D grid.

4. **Real-world example:**
   - **Web graph adjacency matrix / Social Network Friendship Matrix:** In a network with millions of users, any individual user is connected to only a few hundred friends. Over $99.99\%$ of the matrix entries are zero because users are connected to an infinitesimal fraction of the global user base. Storing this as a sparse structure saves terabytes of RAM.

---

## How to Run
```bash
python array_1d_operations.py
python array_2d_operations.py
python sparse_matrix.py
python matrix_calculator.py
```
