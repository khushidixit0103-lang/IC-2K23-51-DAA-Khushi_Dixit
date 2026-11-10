# Binary Search using Divide and Conquer

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 02:** Divide and Conquer  

---

## 1. Aim
To formulate and implement Binary Search using the three canonical phases of the Divide-and-Conquer algorithmic design technique: Divide, Conquer, and Combine.

---

## 2. Problem Statement
Given an array $A[0 \dots n-1]$ sorted in ascending order and a target value $x$, find an index $i$ such that $A[i] = x$, or conclude that $x$ does not belong to $A$.

---

## 3. Divide-and-Conquer Formulation
1. **Divide:** Compute midpoint $mid = low + \lfloor(high - low) / 2\rfloor$. The problem of size $n$ is split into two subproblems of size $\lfloor n/2 \rfloor$.
2. **Conquer:**
   - If $A[mid] == x$, the search succeeds immediately.
   - If $x < A[mid]$, solve the left subproblem $A[low \dots mid-1]$.
   - If $x > A[mid]$, solve the right subproblem $A[mid+1 \dots high]$.
3. **Combine:** The subproblem solution directly yields the overall search result without additional merging.

---

## 4. Recurrence Relation & Master Theorem
$$T(n) = \begin{cases} \Theta(1) & \text{if } n \le 1 \\ T(n/2) + \Theta(1) & \text{if } n > 1 \end{cases}$$

Here $a = 1, b = 2, f(n) = \Theta(1) = \Theta(n^{\log_2 1})$.  
By Case 2 of Master Theorem:
$$T(n) = \Theta(\log n)$$

---

## 5. Complexity Summary

| Metric | Complexity |
| :--- | :--- |
| **Best Case Time** | $\Omega(1)$ (Element at initial midpoint) |
| **Average Case Time** | $\Theta(\log n)$ |
| **Worst Case Time** | $O(\log n)$ |
| **Space Complexity** | $O(\log n)$ recursion stack frames |

---

## 6. Execution Command
```bash
python binary_search_dc.py
```
