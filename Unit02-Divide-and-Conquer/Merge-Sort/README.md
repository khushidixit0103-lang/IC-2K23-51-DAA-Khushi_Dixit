# Merge Sort

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 02:** Divide and Conquer  

---

## 1. Aim
To design, implement, and analyze the Merge Sort algorithm using the Divide-and-Conquer paradigm, proving its recurrence relation and stable $O(n \log n)$ complexity.

---

## 2. Problem Statement
Given an array $A[0 \dots n-1]$ of $n$ elements, sort the array in non-decreasing order such that:
$$A[i] \le A[j] \quad \forall 0 \le i < j < n$$

---

## 3. Algorithm
1. **Divide:** Compute midpoint $mid = \lfloor (low + high) / 2 \rfloor$.
2. **Conquer:**
   - Recursively sort the left subarray $A[low \dots mid]$.
   - Recursively sort the right subarray $A[mid+1 \dots high]$.
3. **Combine (Merge):**
   - Copy subarrays into temporary arrays $L$ and $R$.
   - Maintain two index pointers $i$ and $j$. Compare $L[i]$ and $R[j]$:
     - Place the smaller element back into $A[k]$.
     - Advance the corresponding pointer.
   - Copy any remaining elements of $L$ or $R$ into $A$.

---

## 4. Recurrence Relation & Master Theorem
$$T(n) = 2 T(n/2) + \Theta(n)$$

Parameters for Master Theorem: $a = 2, b = 2, f(n) = \Theta(n)$.
$$\log_b a = \log_2 2 = 1 \implies n^{\log_b a} = n^1 = n$$
Since $f(n) = \Theta(n^{\log_b a}) = \Theta(n)$, Master Theorem Case 2 applies:
$$T(n) = \Theta(n \log n)$$

---

## 5. Complexity Table

| Case | Time Complexity | Auxiliary Space | Stability |
| :--- | :--- | :--- | :--- |
| **Best Case** | $\Omega(n \log n)$ | $O(n)$ | Stable |
| **Average Case** | $\Theta(n \log n)$ | $O(n)$ | Stable |
| **Worst Case** | $O(n \log n)$ | $O(n)$ | Stable |

---

## 6. Execution Command
```bash
python merge_sort.py
```
