# Sum of Subsets Problem using Backtracking

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 06:** Backtracking  

---

## 1. Aim
To design, implement, and analyze the Sum of Subsets problem using Backtracking with dual bounding functions, eliminating infeasible state-space subtrees.

---

## 2. Problem Statement
Given a set of $n$ positive numbers $W = \{w_1, w_2, \dots, w_n\}$ and a positive target sum $M$, find all binary selection vectors $\vec{x} \in \{0, 1\}^n$ such that:
$$\sum_{i=1}^n x_i w_i = M$$

---

## 3. State-Space Representation and Bounding Functions
The state space is a binary tree of depth $n$ where the left branch includes element $w_k$ ($x_k = 1$) and the right branch excludes it ($x_k = 0$).

Before generating child states, sort $W$ in ascending order: $w_1 \le w_2 \le \dots \le w_n$.

### Bounding Function 1 (Upper Bound Pruning):
If adding $w_k$ exceeds the target sum:
$$current\_sum + w_k > M$$
prune the inclusion subtree. Since the array is sorted, all subsequent elements will also exceed $M$.

### Bounding Function 2 (Lower Bound Pruning):
If the accumulated sum plus all remaining elements is strictly less than $M$:
$$current\_sum + \sum_{j=k+1}^n w_j < M$$
prune both inclusion and exclusion subtrees, as reaching $M$ is mathematically impossible.

---

## 4. Complexity Analysis
- **Worst-Case Time:** $O(2^n)$ when all combinations are valid or bounding tests never trigger.
- **Average-Case Time:** Significantly reduced via dual pruning functions ($O(2^{n/2})$ or fewer nodes explored in practice).
- **Space Complexity:** $O(n)$ recursion stack memory.

---

## 5. Execution Command
```bash
python sum_of_subsets.py
```
