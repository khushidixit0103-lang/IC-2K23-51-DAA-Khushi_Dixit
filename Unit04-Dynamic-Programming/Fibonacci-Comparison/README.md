# Fibonacci: Recursion vs Memoization vs Tabulation

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 04:** Dynamic Programming  

---

## 1. Aim
To contrast the exponential complexity of Naive Recursion with linear Top-Down Memoization and space-optimized Bottom-Up Tabulation for calculating the $n$-th Fibonacci number.

---

## 2. Problem Statement
The Fibonacci sequence is defined by recurrence:
$$F(0) = 0, \quad F(1) = 1, \quad F(n) = F(n-1) + F(n-2) \quad \forall n \ge 2$$

Compute $F(n)$ using:
1. Pure Recursion (divide-and-conquer without caching)
2. Top-Down Dynamic Programming with Memoization
3. Bottom-Up Tabulation with $O(1)$ space

---

## 3. Comparison of Paradigms

| Feature | Naive Recursion | Memoized DP (Top-Down) | Tabulated DP (Bottom-Up) |
| :--- | :--- | :--- | :--- |
| **Strategy** | Recomputes overlapping states | Computes on demand; caches answers | Evaluates from base cases upward |
| **Call Tree** | Exploding binary tree | Pruned linear DAG | Single iterative loop |
| **Time Complexity** | $O(2^n)$ or $O(\phi^n)$ ($\phi \approx 1.618$) | $\Theta(n)$ | $\Theta(n)$ |
| **Space Complexity** | $O(n)$ call stack | $O(n)$ memo table + call stack | $O(1)$ scalar variables |
| **Recursion Overhead** | Extreme | Moderate | None |

---

## 4. Empirical Scaling Results
- At $n = 35$:
  - Naive Recursion: **29,860,703 function calls**, **18.19 seconds**.
  - Memoization: **69 function calls**, **0.048 ms** ($> 370,000\times$ faster).
  - Tabulation: Evaluated up to $n = 200$ in **0.052 ms**.

---

## 5. Execution Command
```bash
python fibonacci_comparison.py
```
