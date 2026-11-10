# Unit 04: Dynamic Programming

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Outcome:** CO3 — Ability to design, formulate, and analyze dynamic programming algorithms using principle of optimality and state transition equations.

---

## Unit Overview
Dynamic Programming (DP) is a powerful algorithmic paradigm used to solve complex problems by breaking them down into overlapping subproblems and storing the subproblem results to avoid exponential recomputation. Unlike Divide-and-Conquer where subproblems are completely disjoint, Dynamic Programming thrives when subproblems recur frequently.

---

## Experiments

| Exp No. | Experiment Title | Directory | Key Concepts Covered |
| :---: | :--- | :--- | :--- |
| **1** | [Fibonacci Comparison](./Fibonacci-Comparison/) | `Fibonacci-Comparison/` | Naive recursion vs Top-down memoization vs Bottom-up tabulation ($O(1)$ space) |
| **2** | [0/1 Knapsack](./Knapsack-01-DP/) | `Knapsack-01-DP/` | 2D table state transition, Backtracking selection, Pseudo-polynomial time |
| **3** | [Multistage Graph](./Multistage-Graph/) | `Multistage-Graph/` | Backward DP, Stage-wise topological relaxation, Shortest path $O(V + E)$ |
| **4** | [Floyd-Warshall](./Floyd-Warshall/) | `Floyd-Warshall/` | All-pairs shortest path, $O(V^3)$ state matrix, Negative cycle detection |
| **5** | [Bellman-Ford](./Single-Source-Shortest-Path/) | `Single-Source-Shortest-Path/` | Single-source shortest path, $O(V \cdot E)$ edge relaxation, Negative edge support |
| **6** | [TSP (Held-Karp)](./TSP-DP/) | `TSP-DP/` | Bitmask state space, $O(n^2 2^n)$ vs $O(n!)$ brute force, Hamiltonian tour |
| **7** | [Greedy vs DP](./Greedy-vs-DP-Comparison/) | `Greedy-vs-DP-Comparison/` | Counterexample demonstration, Suboptimality analysis, Benchmark plots |

---

## Algorithmic Complexity Comparison

| Algorithm | State Representation | Recurrence Transition | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :---: | :---: |
| **Fibonacci (Memoized)** | $F(n)$ | $F(n-1) + F(n-2)$ | $\Theta(n)$ | $O(n)$ |
| **Fibonacci (Tabulation)**| $prev_1, prev_2$ | $prev_1 + prev_2$ | $\Theta(n)$ | $O(1)$ |
| **0/1 Knapsack** | $dp[i][w]$ | $\max(dp[i-1][w], dp[i-1][w-w_i] + v_i)$ | $\Theta(n \cdot W)$ | $O(n \cdot W)$ |
| **Multistage Graph** | $cost(u)$ | $\min_{v} \{ c(u, v) + cost(v) \}$ | $O(V + E)$ | $O(V)$ |
| **Floyd-Warshall** | $D^{(k)}[i][j]$ | $\min(D^{(k-1)}[i][j], D^{(k-1)}[i][k] + D^{(k-1)}[k][j])$ | $\Theta(V^3)$ | $\Theta(V^2)$ |
| **Bellman-Ford** | $dist^{(k)}[v]$ | $\min(dist^{(k-1)}[v], dist^{(k-1)}[u] + w(u, v))$ | $O(V \cdot E)$ | $O(V)$ |
| **TSP (Held-Karp)** | $C(S, j)$ | $\min_{i \in S} \{ C(S \setminus \{j\}, i) + dist(i, j) \}$ | $\Theta(n^2 2^n)$ | $\Theta(n 2^n)$ |

---

## Execution Instructions
```bash
# Exp 1: Fibonacci Comparison
python Unit04-Dynamic-Programming/Fibonacci-Comparison/fibonacci_comparison.py

# Exp 2: 0/1 Knapsack DP
python Unit04-Dynamic-Programming/Knapsack-01-DP/knapsack_01_dp.py

# Exp 3: Multistage Graph
python Unit04-Dynamic-Programming/Multistage-Graph/multistage_graph.py

# Exp 4: Floyd-Warshall
python Unit04-Dynamic-Programming/Floyd-Warshall/floyd_warshall.py

# Exp 5: Bellman-Ford
python Unit04-Dynamic-Programming/Single-Source-Shortest-Path/bellman_ford.py

# Exp 6: TSP Held-Karp
python Unit04-Dynamic-Programming/TSP-DP/tsp_dp.py

# Exp 7: Greedy vs DP Knapsack
python Unit04-Dynamic-Programming/Greedy-vs-DP-Comparison/greedy_vs_dp_comparison.py
```
