# Maximum and Minimum using Divide and Conquer

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 02:** Divide and Conquer  

---

## 1. Aim
To find both the minimum and maximum elements in an array using the Divide-and-Conquer tournament strategy and verify that it requires only $\frac{3n}{2} - 2$ element comparisons instead of $2n - 2$ required by straightforward linear scan.

---

## 2. Problem Statement
Given an unsorted sequence of numbers $A[0 \dots n-1]$, find a pair $(min, max)$ such that:
$$\forall x \in A, \quad min \le x \le max$$
using minimum number of pairwise comparisons.

---

## 3. Algorithm (Tournament Method)
1. **Base Case 1 ($n = 1$):**
   If $low == high$, return $(A[low], A[low])$ (0 comparisons).
2. **Base Case 2 ($n = 2$):**
   If $high == low + 1$:
   - If $A[low] < A[high]$, return $(A[low], A[high])$ (1 comparison).
   - Else return $(A[high], A[low])$ (1 comparison).
3. **Divide:**
   Partition $A[low \dots high]$ at $mid = \lfloor (low + high) / 2 \rfloor$.
4. **Conquer:**
   - Recursively find $(min_1, max_1) = \text{MaxMin}(A, low, mid)$.
   - Recursively find $(min_2, max_2) = \text{MaxMin}(A, mid + 1, high)$.
5. **Combine:**
   - $min = \min(min_1, min_2)$ (1 comparison).
   - $max = \max(max_1, max_2)$ (1 comparison).
   - Return $(min, max)$.

---

## 4. Recurrence Relation for Comparisons
$$T(n) = \begin{cases} 
0 & n = 1 \\ 
1 & n = 2 \\ 
2 T(n/2) + 2 & n > 2 
\end{cases}$$

For $n$ being a power of $2$ ($n = 2^k$):
$$T(n) = 2 T(n/2) + 2 = 2(2 T(n/4) + 2) + 2 = \dots = 2^{k-1} T(2) + \sum_{i=1}^{k-1} 2^i$$
$$T(n) = \frac{n}{2}(1) + 2(2^{k-1} - 1) = \frac{n}{2} + n - 2 = \frac{3n}{2} - 2$$

---

## 5. Comparison: Divide & Conquer vs Linear Scan

| Method | Best Case Comparisons | Worst Case Comparisons | Auxiliary Space |
| :--- | :--- | :--- | :--- |
| **Linear Sequential Scan** | $n - 1$ (if sorted ascending) | $2n - 2$ | $O(1)$ |
| **Divide and Conquer** | $\frac{3n}{2} - 2$ | $\frac{3n}{2} - 2$ | $O(\log n)$ stack |

Savings: Saves $25\%$ of total comparisons in worst case.

---

## 6. Execution Command
```bash
python max_min.py
```
