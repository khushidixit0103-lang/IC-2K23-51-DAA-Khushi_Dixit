# Comparative Analysis: 0/1 Knapsack - Dynamic Programming vs Branch and Bound

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 07:** NP-Hard and NP-Complete Problems  

---

## 1. Aim
To empirically and theoretically compare Dynamic Programming (Tabulation) with Least-Cost Branch and Bound (LCBB) on the 0/1 Knapsack problem across varying input sizes ($N \in [10, 35]$), examining execution times, states evaluated, and capacity dependency.

---

## 2. Theoretical Breakdown

| Parameter | Dynamic Programming (Tabulation) | Branch and Bound (LCBB) |
| :--- | :--- | :--- |
| **Strategy** | Evaluates all table subproblems bottom-up | Best-first state-space exploration via Max-Heap |
| **Time Complexity** | $\Theta(N \cdot W)$ (Pseudo-polynomial) | $O(2^N)$ worst-case, often sub-exponential in practice |
| **Space Complexity** | $\Theta(N \cdot W)$ or $O(W)$ | $O(2^N)$ priority queue nodes in worst case |
| **Capacity Sensitivity**| Highly sensitive: large $W$ blows up memory/time | Weakly dependent on numeric $W$; governed by ratios |
| **Bounding Technique** | Overlapping subproblem memoization | Fractional knapsack linear relaxation upper bound |

---

## 3. Generated Artifacts
- **Data Log:** `results.csv` and `docs/performance-analysis/unit07_knapsack_dp_vs_bnb.csv`
- **Visualization:** `knapsack_dp_vs_bnb.png` and `docs/performance-analysis/unit07_knapsack_dp_vs_bnb_plot.png`

---

## 4. Execution Command
```bash
python knapsack_dp_vs_bnb.py
```
