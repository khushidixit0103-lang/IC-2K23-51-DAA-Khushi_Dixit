# Fractional Knapsack Problem

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 03:** Greedy Method  

---

## 1. Aim
To design, implement, and analyze the Fractional Knapsack problem using the Greedy algorithmic approach, establishing the optimal substructure and greedy-choice property.

---

## 2. Problem Statement
Given $n$ items, each having a weight $w_i > 0$ and value $v_i > 0$, and a knapsack with maximum weight capacity $W$, determine fractions $x_i \in [0, 1]$ to place into the knapsack such that:
$$\sum_{i=1}^n x_i w_i \le W \quad \text{and} \quad \sum_{i=1}^n x_i v_i \text{ is maximized.}$$

Unlike the 0/1 Knapsack problem (which requires Dynamic Programming or Branch & Bound because items cannot be divided), the Fractional Knapsack problem exhibits the greedy-choice property, guaranteeing a globally optimal solution via local greedy decisions.

---

## 3. Algorithm
1. Compute the value-to-weight ratio $r_i = \frac{v_i}{w_i}$ for each item $i \in \{1, \dots, n\}$.
2. Sort items in descending order of $r_i$ using an efficient sorting algorithm ($O(n \log n)$).
3. Initialize `remaining_capacity = W` and `total_value = 0`.
4. Iterate through sorted items:
   - If $w_i \le remaining\_capacity$:
     - Take whole item: $x_i = 1.0$.
     - `remaining_capacity -= w_i`, `total_value += v_i`.
   - Else:
     - Take fractional part: $x_i = remaining\_capacity / w_i$.
     - `total_value += v_i * x_i`.
     - `remaining_capacity = 0`.
     - Break loop.
5. Return `total_value` and selection fractions $\vec{x}$.

---

## 4. Complexity Analysis

| Phase | Operation | Complexity |
| :--- | :--- | :--- |
| **Ratio Computation** | $n$ division operations | $\Theta(n)$ |
| **Sorting** | Sort $n$ items based on ratios | $O(n \log n)$ |
| **Greedy Iteration** | Sequential item placement | $O(n)$ |
| **Overall Time** | Bottlenecked by sorting | $O(n \log n)$ |
| **Space Complexity** | Array of items and fractions | $O(n)$ |

---

## 5. Execution Command
```bash
python fractional_knapsack.py
```
