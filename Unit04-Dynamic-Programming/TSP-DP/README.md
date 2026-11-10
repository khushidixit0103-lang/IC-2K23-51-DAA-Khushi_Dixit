# Travelling Salesperson Problem using Dynamic Programming (Held-Karp)

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 04:** Dynamic Programming  

---

## 1. Aim
To formulate, implement, and analyze the Travelling Salesperson Problem (TSP) using the Held-Karp Dynamic Programming algorithm with subset bitmasking, demonstrating an exponential reduction from $O(n!)$ brute force down to $O(n^2 2^n)$.

---

## 2. Problem Statement
Given an $n \times n$ distance matrix $D$ between $n$ cities, find a permutation $\pi$ of $\langle 0, 1, \dots, n-1 \rangle$ starting and ending at city 0 that visits every city exactly once such that the tour length:
$$C(\pi) = \sum_{i=0}^{n-2} D[\pi(i)][\pi(i+1)] + D[\pi(n-1)][\pi(0)]$$
is minimized.

---

## 3. Held-Karp Formulation
Let $S \subseteq \{0, 1, \dots, n-1\}$ be a subset of vertices containing city $0$, and let $C(S, j)$ be the length of the shortest path starting at $0$, visiting every city in $S$ exactly once, and terminating at city $j \in S$.

### Base Case:
$$C(\{0\}, 0) = 0$$

### Recurrence Relation:
For any subset $S$ with $|S| \ge 2$ and $j \in S, j \neq 0$:
$$C(S, j) = \min_{i \in S, i \neq j} \Big\{ C(S \setminus \{j\}, i) + D[i][j] \Big\}$$

### Optimal Tour Closure:
$$C_{opt} = \min_{j \in \{1, \dots, n-1\}} \Big\{ C(V, j) + D[j][0] \Big\}$$

---

## 4. Complexity Comparison

| Algorithm | Design Paradigm | Time Complexity | Auxiliary Space |
| :--- | :--- | :--- | :--- |
| **Exhaustive Brute-Force** | Generate all $(n-1)!$ tours | $O(n!)$ | $O(n)$ recursion stack |
| **Held-Karp** | Dynamic Programming + Bitmasking | $O(n^2 2^n)$ | $O(n 2^n)$ DP state table |

For $n = 20$:
- Brute Force: $19! \approx 1.21 \times 10^{17}$ operations (impractical).
- Held-Karp: $20^2 \times 2^{20} \approx 4.19 \times 10^8$ operations (solvable in seconds).

---

## 5. Execution Command
```bash
python tsp_dp.py
```
