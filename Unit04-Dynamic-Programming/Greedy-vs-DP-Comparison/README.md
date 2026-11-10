# Comparative Analysis: Greedy Method vs Dynamic Programming

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 04:** Dynamic Programming  

---

## 1. Aim
To contrast the Greedy algorithmic strategy with Dynamic Programming using the 0/1 Knapsack optimization problem, demonstrating why local greedy heuristics fail on discrete decisions and proving DP's guarantee of global optimality.

---

## 2. Theoretical Breakdown

| Dimension | Greedy Method | Dynamic Programming |
| :--- | :--- | :--- |
| **Decision Nature** | Irrevocable local choice at each step | Explores all viable subproblems systematically |
| **Overlapping Subproblems** | Not required | Required (avoids redundant recalculation) |
| **Substructure Requirement**| Greedy-choice property + Optimal substructure | Optimal substructure |
| **Applicability to 0/1 Knapsack**| Fails to guarantee optimal answer | Guarantees exact global optimal answer |
| **Time Complexity (0/1 Knapsack)**| $O(n \log n)$ (sorting by ratio) | $\Theta(n \cdot W)$ (pseudo-polynomial) |
| **Space Complexity** | $O(n)$ | $\Theta(n \cdot W)$ or $O(W)$ |

---

## 3. Classic Counterexample
- **Item 1:** $v_1 = 60, w_1 = 10 \implies r_1 = 6.0$
- **Item 2:** $v_2 = 100, w_2 = 20 \implies r_2 = 5.0$
- **Item 3:** $v_3 = 120, w_3 = 30 \implies r_3 = 4.0$
- **Capacity:** $W = 50$

### Greedy Heuristic Choice:
- Picks Item 1 ($w=10$, profit 60) and Item 2 ($w=20$, profit 100).
- Remaining capacity = $50 - 30 = 20$. Item 3 ($w=30$) cannot fit.
- Total weight = 30, **Total Profit = 160**.

### Dynamic Programming Solution:
- Picks Item 2 ($w=20$) and Item 3 ($w=30$).
- Total weight = 50, **Total Profit = 220**.
- **Result:** DP achieves 37.5% higher profit ($+\$60$) over Greedy!

---

## 4. Generated Artifacts
- **Data Log:** `results.csv` and `docs/performance-analysis/unit04_greedy_vs_dp_comparison.csv`
- **Visualization:** `greedy_vs_dp.png` and `docs/performance-analysis/unit04_greedy_vs_dp_plot.png`

---

## 5. Execution Command
```bash
python greedy_vs_dp_comparison.py
```
