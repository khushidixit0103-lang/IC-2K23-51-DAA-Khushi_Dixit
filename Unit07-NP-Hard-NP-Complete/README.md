# Unit 07: NP-Hard and NP-Complete Problems

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Outcomes:** CO5, CO7 — Ability to formulate NP-Complete / NP-Hard problems, analyze exponential bottlenecks, and apply Branch and Bound optimization.

---

## Unit Overview
Unit 07 addresses intractable problems for which no polynomial-time deterministic algorithms are known ($P \neq NP$). The unit demonstrates the combinatorial explosion of exhaustive search and explores state-of-the-art exact optimization techniques—specifically **Branch and Bound** with continuous relaxations (Fractional Knapsack) and matrix reductions (TSP).

---

## Experiments

| Exp No. | Experiment Title | Directory | Key Concepts Covered |
| :---: | :--- | :--- | :--- |
| **1** | [Exhaustive Search](./Exhaustive-Search/) | `Exhaustive-Search/` | Exponential state-space generation ($2^N$), Combinatorial explosion, Hardness boundaries |
| **2** | [0/1 Knapsack BnB](./Knapsack-Branch-and-Bound/) | `Knapsack-Branch-and-Bound/` | LCBB (Least-Cost Branch & Bound), Max-Heap, Fractional relaxation upper bound |
| **3** | [TSP Branch and Bound](./TSP-Branch-and-Bound/) | `TSP-Branch-and-Bound/` | Reduced Cost Matrix lower bounding, Row & column reductions, Min-Heap expansion |
| **4** | [Knapsack: DP vs BnB](./Knapsack-DP-vs-BnB/) | `Knapsack-DP-vs-BnB/` | Pseudo-polynomial DP vs LCBB, Capacity sensitivity, Memory evaluation |
| **5** | [TSP: DP vs BnB](./TSP-DP-vs-BnB/) | `TSP-DP-vs-BnB/` | Held-Karp $O(N^2 2^N)$ vs Matrix LCBB, State exploration, Performance curves |

---

## Paradigmatic Comparison

| Method | Paradigm | 0/1 Knapsack Complexity | TSP Complexity | Memory Model |
| :--- | :--- | :---: | :---: | :---: |
| **Exhaustive Search** | Brute Force | $\Theta(2^N)$ | $\Theta(N!)$ | $O(N)$ stack |
| **Dynamic Programming** | Optimal Substructure | $\Theta(N \cdot W)$ | $\Theta(N^2 2^N)$ | Large table memory |
| **Branch and Bound** | Pruned State Space | $O(2^N)$ worst, fast avg | $O(N!)$ worst, pruned avg | Priority Queue |

---

## Execution Instructions
```bash
# Exp 1: Exhaustive Search
python Unit07-NP-Hard-NP-Complete/Exhaustive-Search/exhaustive_search.py

# Exp 2: 0/1 Knapsack Branch and Bound
python Unit07-NP-Hard-NP-Complete/Knapsack-Branch-and-Bound/knapsack_bnb.py

# Exp 3: TSP Branch and Bound
python Unit07-NP-Hard-NP-Complete/TSP-Branch-and-Bound/tsp_bnb.py

# Exp 4: Knapsack DP vs BnB Benchmark
python Unit07-NP-Hard-NP-Complete/Knapsack-DP-vs-BnB/knapsack_dp_vs_bnb.py

# Exp 5: TSP DP vs BnB Benchmark
python Unit07-NP-Hard-NP-Complete/TSP-DP-vs-BnB/tsp_dp_vs_bnb.py
```
