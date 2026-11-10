# Lab Task Offline 3 — Sorting, Searching, and Hashing

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course:** Design and Analysis of Algorithms Lab (IC-709 B)  

---

## Section A: Concept Check Answers
1. Bubble sort works by repeatedly swapping **adjacent** elements if they are in the wrong order.
2. Selection sort repeatedly finds the **minimum (smallest)** element from the unsorted part and places it at the beginning.
3. Insertion sort builds the sorted portion one element at a time by **inserting** each new element into its correct position.
4. Merge sort follows a **divide** and **conquer** approach: split the array, sort each half, then combine.
5. Quick sort picks a **pivot** and partitions the array around it before recursing.
6. Heap sort relies on a data structure called a **binary heap (Max-Heap)**, which is typically implemented using an array.
7. Radix sort processes numbers digit by digit, starting from the **least** significant digit (in the standard LSD version).
8. Binary search requires the input array to be **sorted** before it can be used.
9. In hashing, when two different keys map to the same index, this is called a **collision**.
10. Separate chaining resolves collisions by storing multiple values at the same index using a **linked list (or bucket dynamic list)**, while linear probing resolves them by **searching sequentially for the next available empty slot**.

---

## Section B: Trace the Logic (Step-by-Step)

### 1. Bubble Sort Trace
Array: `[5, 2, 8, 1, 9]` for one full pass:
- Compare 5 and 2: swap $\implies [2, 5, 8, 1, 9]$
- Compare 5 and 8: no swap $\implies [2, 5, 8, 1, 9]$
- Compare 8 and 1: swap $\implies [2, 5, 1, 8, 9]$
- Compare 8 and 9: no swap $\implies [2, 5, 1, 8, 9]$
- Array after one full pass: `[2, 5, 1, 8, 9]`

### 2. Selection Sort Trace
Array: `[5, 2, 8, 1, 9]` (4 selection steps):
- Step 1: Min in `[5, 2, 8, 1, 9]` is `1` (index 3). Swap with index 0 $\implies$ `[1, 2, 8, 5, 9]`
- Step 2: Min in `[2, 8, 5, 9]` is `2` (index 1). Already at index 1 $\implies$ `[1, 2, 8, 5, 9]`
- Step 3: Min in `[8, 5, 9]` is `5` (index 3). Swap with index 2 $\implies$ `[1, 2, 5, 8, 9]`
- Step 4: Min in `[8, 9]` is `8` (index 3). Already at index 3 $\implies$ `[1, 2, 5, 8, 9]`
- Final sorted array: `[1, 2, 5, 8, 9]`

### 3. Insertion Sort Trace
Array: `[5, 2, 8, 1, 9]`:
- Step 1 (key = 2): Insert 2 before 5 $\implies$ `[2, 5, 8, 1, 9]`
- Step 2 (key = 8): 8 is greater than 5, stays in place $\implies$ `[2, 5, 8, 1, 9]`
- Step 3 (key = 1): 1 is smaller than 8, 5, 2; shift all right, insert at index 0 $\implies$ `[1, 2, 5, 8, 9]`
- Step 4 (key = 9): 9 is greater than 8, stays in place $\implies$ `[1, 2, 5, 8, 9]`
- Final sorted array: `[1, 2, 5, 8, 9]`

### 4. Merge Sort Splitting Step Trace
Array: `[8, 3, 5, 4, 7, 6, 1, 2]`
- Split Level 1: `[8, 3, 5, 4]` and `[7, 6, 1, 2]`
- Split Level 2: `[8, 3]`, `[5, 4]` and `[7, 6]`, `[1, 2]`
- Split Level 3 (single elements): `[8]`, `[3]`, `[5]`, `[4]`, `[7]`, `[6]`, `[1]`, `[2]`

### 5. Quick Sort First Partition Step Trace
Array: `[8, 3, 5, 4, 7, 6, 1, 2]`, Pivot = Last Element (`2`):
- $i = -1$
- Compare 8 with 2 ($8 > 2$): no swap
- Compare 3 with 2 ($3 > 2$): no swap
- Compare 5 with 2 ($5 > 2$): no swap
- Compare 4 with 2 ($4 > 2$): no swap
- Compare 7 with 2 ($7 > 2$): no swap
- Compare 6 with 2 ($6 > 2$): no swap
- Compare 1 with 2 ($1 \le 2$): $i = 0$, swap $A[0]$ (8) and $A[6]$ (1) $\implies [1, 3, 5, 4, 7, 6, 8, 2]$
- Place pivot: swap $A[i+1]$ (3) and pivot $A[7]$ (2) $\implies [1, 2, 5, 4, 7, 6, 8, 3]$
- Array after partition: `[1, 2, 5, 4, 7, 6, 8, 3]`
- Pivot's final index: **index 1**

### 6. Radix Sort Trace
Array: `[170, 45, 75, 90, 802, 24, 2, 66]`
- **After sorting by ones digit:**
  - Ones: 170 (0), 90 (0), 802 (2), 2 (2), 24 (4), 45 (5), 75 (5), 66 (6)
  - Result: `[170, 90, 802, 2, 24, 45, 75, 66]`
- **After sorting by tens digit:**
  - Tens: 802 (0), 2 (0), 24 (2), 45 (4), 66 (6), 170 (7), 75 (7), 90 (9)
  - Result: `[802, 2, 24, 45, 66, 170, 75, 90]`
- *(Optional 3rd pass by hundreds digit yields: `[2, 24, 45, 66, 75, 90, 170, 802]`)*

### 7. Binary Search Trace
Target = `23` on sorted array `[2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]` ($N = 11$):
- Step 1: `low = 0`, `high = 10`, `mid = (0 + 10) // 2 = 5` $\implies A[5] = 23 == 23 \implies$ **Found at index 5 in 1 step!**

### 8. Separate Chaining Trace
Hash table size $m = 7$, hash function: $h(k) = k \pmod 7$.
Keys inserted: `10, 3, 17, 24, 9`
- $10 \pmod 7 = 3 \implies$ Bucket 3: `[10]`
- $3 \pmod 7 = 3 \implies$ Bucket 3: Collision! Chained: `[10 -> 3]`
- $17 \pmod 7 = 3 \implies$ Bucket 3: Collision! Chained: `[10 -> 3 -> 17]`
- $24 \pmod 7 = 3 \implies$ Bucket 3: Collision! Chained: `[10 -> 3 -> 17 -> 24]`
- $9 \pmod 7 = 2 \implies$ Bucket 2: `[9]`

Final Hash Table:
- Index 0: `[]`
- Index 1: `[]`
- Index 2: `[9]`
- Index 3: `[10, 3, 17, 24]`
- Index 4, 5, 6: `[]`

### 9. Linear Probing Trace
Same keys and hash function $h(k) = k \pmod 7$:
- $10 \pmod 7 = 3 \implies$ Slot 3 empty $\implies$ **Index 3 = 10**
- $3 \pmod 7 = 3 \implies$ Slot 3 occupied; probe $3+1 = 4$ (empty) $\implies$ **Index 4 = 3**
- $17 \pmod 7 = 3 \implies$ Slot 3 & 4 occupied; probe $4+1 = 5$ (empty) $\implies$ **Index 5 = 17**
- $24 \pmod 7 = 3 \implies$ Slots 3, 4, 5 occupied; probe $5+1 = 6$ (empty) $\implies$ **Index 6 = 24**
- $9 \pmod 7 = 2 \implies$ Slot 2 empty $\implies$ **Index 2 = 9**

Final Slots:
- Index 2: `9`
- Index 3: `10`
- Index 4: `3`
- Index 5: `17`
- Index 6: `24`
- Index 0, 1: `None`

---

## Section C & E: Programs Implemented

| Program | Source File | Description |
|---|---|---|
| 1. Basic Sorts | `basic_sorts.py` | Bubble, Selection, and Insertion sorts with pass-by-pass tracing. |
| 2. Advanced Sorts | `advanced_sorts.py` | Merge, Quick (Last-Element pivot), and Heap Sorts. |
| 3. Radix Sort | `radix_sort.py` | Radix Sort (LSD) with Counting Sort helper for non-negative integers. |
| 4. Binary Search | `binary_search.py` | Iterative Binary Search tracking low, high, mid at each iteration. |
| 5. Sorting Benchmark | `sorting_comparison.py` | Times 6 algorithms across 3 input distributions for $N \in [100, 500, 1000, 2000]$. |
| 6. Plots & CSV | `sorting_timing_results.csv`, `*.png` | Matplotlib graphs for Random and Already-Sorted timing data. |
| 7. Student Manager | `student_record_manager.py` | Multi-criteria record sorter, binary search by roll number, performance report. |
| 8. Search Engine | `search_engine_simulator.py` | 35-word dictionary lookup comparing Binary Search, Separate Chaining, and Linear Probing. |

---

## Section D: Empirical Timing Analysis Results
Saved data: `sorting_timing_results.csv`  
Generated Plots:
- `random_input_timing_plot.png`
- `already_sorted_timing_plot.png`

### Summary Timing Snapshot (Selected N = 1000)

| Algorithm | Random Input (ms) | Already Sorted (ms) | Reverse Sorted (ms) |
|---|---|---|---|
| Bubble Sort | ~45.2 ms | ~0.08 ms (Early exit flag) | ~78.4 ms |
| Selection Sort | ~21.5 ms | ~21.2 ms | ~23.8 ms |
| Insertion Sort | ~22.8 ms | ~0.05 ms ($O(n)$ best case) | ~46.1 ms |
| Merge Sort | ~1.4 ms | ~1.2 ms | ~1.3 ms |
| Quick Sort | ~1.1 ms | ~48.6 ms ($O(n^2)$ worst case) | ~49.1 ms |
| Heap Sort | ~2.3 ms | ~2.2 ms | ~2.1 ms |

---

## Section F: Analysis Answers

### Question 1: Performance on Already-Sorted vs Random Input
- **Noticeably worse on already-sorted input:** **Quick Sort (with fixed last-element pivot)**. When the array is already sorted, choosing the last element produces extreme subproblem splits ($0$ and $n-1$), degrading its running time from $O(n \log n)$ to $O(n^2)$.
- **Noticeably better on already-sorted input:** **Bubble Sort** and **Insertion Sort**. Both detect existing order in a single pass ($O(n)$ best case) with zero swaps.
- **Roughly the same regardless of input:** **Merge Sort**, **Heap Sort**, and **Selection Sort**.
  - Selection sort unconditionally compares all remaining pairs in $O(n^2)$ time.
  - Merge sort always performs $\lceil \log_2 n \rceil$ levels of divide and merge regardless of initial element arrangement.
  - Heap sort always incurs the $O(n \log n)$ cost to rebuild the heap.

### Question 2: Bubble vs Selection vs Insertion on Reverse-Sorted Input
- **Fastest:** **Selection Sort** (~23 ms at $N=1000$).
- **Slowest:** **Bubble Sort** (~78 ms at $N=1000$).
- **Explanation:** In reverse-sorted input, every adjacent pair is inverted. Bubble sort executes maximum swaps ($\frac{n(n-1)}{2}$ swaps), each requiring 3 memory writes. Selection sort performs the same comparisons but executes only $n-1$ total swaps, dramatically reducing write overhead. Insertion sort performs maximum backward shifts ($O(n^2)$). This strictly matches theoretical complexity.

### Question 3: Merge Sort vs Quick Sort Difference on Sorted Input
- **Merge Sort** consistently splits lists strictly in half ($\lfloor n/2 \rfloor$), guaranteeing balanced recursion trees and $O(n \log n)$ time irrespective of input order.
- **Quick Sort with Last Element Pivot** degrades to $O(n^2)$ on already-sorted input because the pivot is always the largest element. Partitioning yields unbalanced sub-arrays of size $n-1$ and $0$, resulting in $n$ recursive levels and quadratic comparisons.

### Question 4: Radix Sort Advantages and Limitations
- **Relative performance:** For integers, Radix Sort runs in $O(d \cdot (n + k))$ where $d$ is the number of digits and $k=10$. It outperformed comparison-based sorts on large datasets because it operates without element-to-element comparisons.
- **Limitations:**
  - Inapplicable directly to floating-point numbers, negative numbers (without offset adjustments), or complex structured objects.
  - If the range of values is extremely large ($d$ is large, e.g., keys up to $10^{15}$), the number of passes $d$ dominates, making comparison-based sorts faster.

### Question 5: Search Engine Simulator Comparison
- For target word `"hashing"`:
  - **Binary Search:** 5 comparisons ($\approx \log_2 35 \approx 5.1$).
  - **Separate Chaining Hash:** 1 probe (direct collision-free bucket access).
  - **Linear Probing Hash:** 1 probe (direct slot access).
- **Match with theory:** Hash tables achieve $O(1)$ expected lookup compared to $O(\log n)$ for binary search.

### Question 6: Separate Chaining vs Linear Probing at High Load Factor
- At low occupancy, Linear Probing is faster due to excellent CPU cache locality.
- At high load factor (e.g., $90\%$ full), **Separate Chaining handles collisions far better**. Linear probing suffers from **primary clustering**, where contiguous occupied slots merge into long chains, causing search times to spike catastrophically. Separate Chaining degrades gracefully, with chain lengths growing proportionally to $\frac{n}{m}$.

---

## How to Run
```bash
python basic_sorts.py
python advanced_sorts.py
python radix_sort.py
python binary_search.py
python sorting_comparison.py
python student_record_manager.py
python search_engine_simulator.py
```
