# Comparative Analysis: TSP - Dynamic Programming vs Branch and Bound

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 07:** NP-Hard and NP-Complete Problems  

---

## 1. Aim
To theoretically and empirically compare Held-Karp Dynamic Programming with Least-Cost Branch and Bound (Reduced Matrix Method) for solving the Travelling Salesperson Problem across varying city counts ($N \in [4, 12]$).

---

## 2. Comparative Matrix

| Characteristic | Held-Karp Dynamic Programming | Branch and Bound (LCBB) |
| :--- | :--- | :--- |
| **Strategy** | Subset bitmasking state transitions | Min-Heap priority queue state-space search |
| **Time Complexity** | $\Theta(N^2 \cdot 2^N)$ deterministic | $O(N!)$ worst case, often much lower via pruning |
| **Space Complexity** | $\Theta(N \cdot 2^N)$ memory table | Dynamic based on active priority queue nodes |
| **Pruning Behavior** | No branch pruning; solves all subproblems | Aggressive pruning via cost matrix reductions |
| **Optimal For** | Precise guarantees when $N \le 20$ | Graphs with non-uniform edge variance ($N \le 30$) |

---

## 3. Generated Artifacts
- **Data CSV:** `results.csv` and `docs/performance-analysis/unit07_tsp_dp_vs_bnb.csv`
- **Visualization:** `tsp_dp_vs_bnb.png` and `docs/performance-analysis/unit07_tsp_dp_vs_bnb_plot.png`

---

## 4. Execution Command
```bash
python tsp_dp_vs_bnb.py
```
