# Quick Sort

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 02:** Divide and Conquer  

---

## 1. Aim
To design, implement, and analyze the Quick Sort algorithm using the Divide-and-Conquer strategy, exploring partition schemes and examining best, average, and worst-case running times.

---

## 2. Problem Statement
Given an unsorted array $A[low \dots high]$, rearrange elements in place such that all items less than or equal to a chosen pivot element precede it, and all items greater follow it, then sort the two sub-arrays recursively.

---

## 3. Algorithm (Lomuto Partition)
1. **Divide (Partition):**
   - Pick $A[high]$ as pivot $p$.
   - Maintain index $i = low - 1$.
   - For $j = low$ to $high - 1$:
     - If $A[j] \le p$, increment $i$ and swap $A[i]$ with $A[j]$.
   - Swap $A[i+1]$ with $A[high]$.
   - Return partition index $pi = i + 1$.
2. **Conquer:**
   - Recursively sort left partition: `QUICK_SORT(A, low, pi - 1)`.
   - Recursively sort right partition: `QUICK_SORT(A, pi + 1, high)`.
3. **Combine:**
   - Trivial, as sorting is performed in-place.

---

## 4. Complexity Analysis

| Case | Recurrence Relation | Solution | Condition |
| :--- | :--- | :--- | :--- |
| **Best Case** | $T(n) = 2T(n/2) + \Theta(n)$ | $\Omega(n \log n)$ | Pivot always splits array into equal halves |
| **Average Case** | $T(n) = \frac{2}{n}\sum_{k=0}^{n-1}T(k) + \Theta(n)$ | $\Theta(n \log n)$ | Balanced random partition splits |
| **Worst Case** | $T(n) = T(n-1) + \Theta(n)$ | $O(n^2)$ | Already sorted or reverse sorted with extreme pivot |
| **Space Complexity** | $O(\log n)$ best/avg, $O(n)$ worst | Stack space | In-place partition |

---

## 5. Execution Command
```bash
python quick_sort.py
```
