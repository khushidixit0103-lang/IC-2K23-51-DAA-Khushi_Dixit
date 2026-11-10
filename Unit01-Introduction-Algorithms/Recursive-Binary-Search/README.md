# Recursive Binary Search

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 01:** Introduction to Algorithms and Performance Analysis  

---

## 1. Aim
To formulate, implement, and analyze the Recursive Binary Search algorithm using the divide-and-conquer paradigm, establishing recurrence relations and evaluating stack frame overhead.

---

## 2. Problem Statement
Given a sorted sequence $A = \langle a_0, a_1, \dots, a_{n-1} \rangle$ where $a_0 \le a_1 \le \dots \le a_{n-1}$, and a target element $K$, recursively partition the search interval $[low, high]$ into sub-problems until either $A[mid] = K$ or the base case $low > high$ is reached.

---

## 3. Algorithm
1. **Base Case 1:** If $low > high$, key does not exist; return `-1`.
2. Compute pivot: $mid = low + \lfloor (high - low) / 2 \rfloor$.
3. **Base Case 2:** If $arr[mid] == key$, key is found; return $mid$.
4. **Divide & Recur:**
   - If $arr[mid] < key$, recurse on right sub-array: `BINARY_SEARCH_RECURSIVE(arr, mid + 1, high, key)`.
   - If $arr[mid] > key$, recurse on left sub-array: `BINARY_SEARCH_RECURSIVE(arr, low, mid - 1, key)`.

---

## 4. Recurrence Relation
- **Divide:** Compute midpoint in $\Theta(1)$ operations.
- **Conquer:** Solve 1 subproblem of size $n/2$.
- **Combine:** Empty ($\Theta(1)$).

$$T(n) = T(n/2) + \Theta(1)$$

By the Master Theorem ($a = 1, b = 2, f(n) = \Theta(1)$):
$$\log_b a = \log_2 1 = 0 \implies n^{\log_b a} = n^0 = 1 = \Theta(f(n))$$
$$\therefore T(n) = \Theta(\log n)$$

---

## 5. Complexity Summary

| Metric | Best Case | Average Case | Worst Case |
| :--- | :--- | :--- | :--- |
| **Time Complexity** | $\Omega(1)$ | $\Theta(\log n)$ | $O(\log n)$ |
| **Space Complexity (Stack)** | $O(1)$ | $O(\log n)$ | $O(\log n)$ |

---

## 6. Comparison: Iterative vs Recursive Binary Search

| Feature | Iterative Binary Search | Recursive Binary Search |
| :--- | :--- | :--- |
| **Control Structure** | While loop | Function self-invocation |
| **Space Complexity** | $O(1)$ auxiliary | $O(\log n)$ call-stack space |
| **Function Call Overhead** | None | Yes (frame push/pop) |
| **Readability** | Imperative, straightforward | Natural divide-and-conquer formulation |

---

## 7. Sample Execution
- **Sorted Input:** `[10, 23, 35, 42, 56, 68, 71, 85, 92, 99]`
- Search `56`: Found at index `4` in 1 call (Best Case).
- Search `23`: Found at index `1` in 2 calls (Average Case).
- Search `99`: Found at index `9` in 4 calls (Worst Case).
- Search `50`: Not found (`-1`) in 4 calls (Absent Case).

---

## 8. Execution Command
```bash
python binary_search_recursive.py
```
