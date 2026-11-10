# Unit 02: Divide and Conquer

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Outcome:** CO1 — Ability to apply divide-and-conquer strategy, establish recurrence relations, and analyze time/space trade-offs.

---

## Unit Overview
The Divide-and-Conquer paradigm breaks a complex problem into two or more independent subproblems of the same or related type until they become simple enough to be solved directly (base case). The solutions to the subproblems are then combined to give a solution to the original problem. This unit explores foundational search, optimization, sorting, and matrix operations under this paradigm.

---

## Experiments

| Exp No. | Experiment Title | Directory | Key Concepts Covered |
| :---: | :--- | :--- | :--- |
| **1** | [Binary Search (D&C)](./Binary-Search/) | `Binary-Search/` | Divide, conquer, and combine steps; recurrence $T(n) = T(n/2) + \Theta(1)$ |
| **2** | [Maximum and Minimum](./Maximum-Minimum/) | `Maximum-Minimum/` | Tournament method; optimal $\frac{3n}{2} - 2$ comparison bound |
| **3** | [Merge Sort](./Merge-Sort/) | `Merge-Sort/` | Two-way merge; stable $O(n \log n)$ worst-case; $O(n)$ auxiliary space |
| **4** | [Quick Sort](./Quick-Sort/) | `Quick-Sort/` | Lomuto/Hoare partitioning; in-place sorting; worst-case vs average-case |
| **5** | [Heap Sort](./Heap-Sort/) | `Heap-Sort/` | Complete binary max-heap; linear heap construction; $O(1)$ space sorting |
| **6** | [Strassen's Matrix Mult](./Strassen-Matrix-Multiplication/) | `Strassen-Matrix-Multiplication/` | 7 recursive multiplications; $O(n^{2.807})$ time; zero-padding for non-powers of 2 |
| **7** | [Sorting Performance Analysis](./Sorting-Performance-Analysis/) | `Sorting-Performance-Analysis/` | Empirical runtime scaling, CSV logging, Matplotlib comparative graphs |

---

## Comparative Performance Summary

| Algorithm | Paradigm | Best Case | Average Case | Worst Case | Auxiliary Space | Stable? |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Binary Search (D&C)** | D&C | $\Omega(1)$ | $\Theta(\log n)$ | $O(\log n)$ | $O(\log n)$ stack | N/A |
| **Max-Min (D&C)** | D&C (Tournament) | $\frac{3n}{2}-2$ comps | $\frac{3n}{2}-2$ comps | $\frac{3n}{2}-2$ comps | $O(\log n)$ stack | N/A |
| **Merge Sort** | D&C (Merging) | $\Omega(n \log n)$ | $\Theta(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes |
| **Quick Sort** | D&C (Partition) | $\Omega(n \log n)$ | $\Theta(n \log n)$ | $O(n^2)$ | $O(\log n)$ stack | No |
| **Heap Sort** | Max-Heap Selection | $\Omega(n \log n)$ | $\Theta(n \log n)$ | $O(n \log n)$ | $O(1)$ | No |
| **Strassen's Mult** | D&C (Submatrices) | $\Theta(n^{2.807})$ | $\Theta(n^{2.807})$ | $\Theta(n^{2.807})$ | $O(n^2)$ | N/A |

---

## Execution Instructions
Navigate into the respective directory and run:
```bash
# Exp 1: Binary Search
python Unit02-Divide-and-Conquer/Binary-Search/binary_search_dc.py

# Exp 2: Maximum and Minimum
python Unit02-Divide-and-Conquer/Maximum-Minimum/max_min.py

# Exp 3: Merge Sort
python Unit02-Divide-and-Conquer/Merge-Sort/merge_sort.py

# Exp 4: Quick Sort
python Unit02-Divide-and-Conquer/Quick-Sort/quick_sort.py

# Exp 5: Heap Sort
python Unit02-Divide-and-Conquer/Heap-Sort/heap_sort.py

# Exp 6: Strassen's Matrix Multiplication
python Unit02-Divide-and-Conquer/Strassen-Matrix-Multiplication/strassen_matrix_mult.py

# Exp 7: Sorting Performance Benchmarking
python Unit02-Divide-and-Conquer/Sorting-Performance-Analysis/sorting_performance_analysis.py
```
