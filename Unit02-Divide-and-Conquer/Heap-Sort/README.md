# Heap Sort

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 02:** Divide and Conquer  

---

## 1. Aim
To design, implement, and analyze the Heap Sort algorithm using a complete binary tree max-heap, establishing linear-time heap construction and $O(n \log n)$ in-place sorting.

---

## 2. Problem Statement
Given an array $A[0 \dots n-1]$, convert it into a Max-Heap structure where $A[i] \ge A[2i+1]$ and $A[i] \ge A[2i+2]$, then repeatedly swap the maximum element with the last element and restore heap order.

---

## 3. Algorithm
1. **Build Max-Heap:**
   - For $i = \lfloor n/2 \rfloor - 1$ down to $0$:
     - Call `MAX_HEAPIFY(A, n, i)`.
   - Running time for building heap is $\sum_{h=0}^{\lfloor \log n \rfloor} \lceil \frac{n}{2^{h+1}} \rceil O(h) = O(n)$.
2. **Sort Phase:**
   - For $i = n - 1$ down to $1$:
     - Swap root $A[0]$ with $A[i]$.
     - Reduce heap size to $i$.
     - Call `MAX_HEAPIFY(A, i, 0)`.

---

## 4. Complexity Table

| Case | Time Complexity | Auxiliary Space | In-Place? | Stable? |
| :--- | :--- | :--- | :--- | :--- |
| **Build Heap** | $\Theta(n)$ | $O(1)$ | Yes | No |
| **Best Case Sort** | $\Omega(n \log n)$ | $O(1)$ | Yes | No |
| **Average Case Sort** | $\Theta(n \log n)$ | $O(1)$ | Yes | No |
| **Worst Case Sort** | $O(n \log n)$ | $O(1)$ | Yes | No |

---

## 5. Execution Command
```bash
python heap_sort.py
```
