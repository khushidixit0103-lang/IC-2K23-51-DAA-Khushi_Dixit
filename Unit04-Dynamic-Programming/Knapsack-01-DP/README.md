# 0/1 Knapsack using Dynamic Programming

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 04:** Dynamic Programming  

---

## 1. Aim
To design, implement, and analyze the 0/1 Knapsack problem using Dynamic Programming, contrasting its pseudopolynomial behavior with the continuous greedy method and recovering the optimal subset via table backtracking.

---

## 2. Problem Statement
Given $n$ items, each with value $v_i > 0$ and weight $w_i > 0$, and a knapsack of capacity $W$, choose binary inclusion variables $x_i \in \{0, 1\}$ such that:
$$\sum_{i=1}^n x_i w_i \le W \quad \text{and} \quad \sum_{i=1}^n x_i v_i \text{ is maximized.}$$

---

## 3. Dynamic Programming Formulation
Let $dp[i][w]$ denote the maximum value achievable considering a subset of the first $i$ items with total weight not exceeding $w$.

### Base Cases:
$$dp[0][w] = 0 \quad \forall 0 \le w \le W$$
$$dp[i][0] = 0 \quad \forall 0 \le i \le n$$

### Recurrence Relation:
$$dp[i][w] = \begin{cases}
dp[i-1][w] & \text{if } w_i > w \\
\max\Big(dp[i-1][w], \; dp[i-1][w - w_i] + v_i\Big) & \text{if } w_i \le w
\end{cases}$$

---

## 4. Complexity Analysis
- **Time Complexity:** $\Theta(n \cdot W)$ operations to fill the $(n+1) \times (W+1)$ matrix. This is **pseudo-polynomial** because it depends on the numerical value of $W$ rather than the bit length $\log W$.
- **Space Complexity:** $O(n \cdot W)$ for the full 2D table, reducible to $O(W)$ using 1D rolling array if only the optimal value is sought.
- **Item Reconstruction:** $O(n)$ by tracing backwards from $dp[n][W]$.

---

## 5. Execution Command
```bash
python knapsack_01_dp.py
```
