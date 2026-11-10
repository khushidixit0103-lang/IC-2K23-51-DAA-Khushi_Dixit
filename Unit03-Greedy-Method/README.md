# Unit 03: Greedy Method

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Outcome:** CO2 — Ability to formulate greedy choice properties, establish optimal substructure, and design efficient greedy algorithms for discrete optimization.

---

## Unit Overview
The Greedy algorithmic paradigm builds a global solution piece by piece, always choosing the locally optimal candidate at each decision point without back-tracking. It is applicable to problems exhibiting both the **greedy-choice property** (a global optimum can be reached through local optimal choices) and **optimal substructure** (an optimal solution to the problem contains optimal solutions to subproblems).

---

## Experiments

| Exp No. | Experiment Title | Directory | Key Concepts Covered |
| :---: | :--- | :--- | :--- |
| **1** | [Fractional Knapsack](./Fractional-Knapsack/) | `Fractional-Knapsack/` | Value-to-weight ratio ordering, Continuous item partitioning, $O(n \log n)$ time |
| **2** | [Job Sequencing with Deadlines](./Job-Sequencing/) | `Job-Sequencing/` | Profit maximization, Discrete timeline slotting, Greedy allocation |
| **3** | [Prim's MST](./Prims-MST/) | `Prims-MST/` | Vertex-centric cut property, Adjacency matrix, Dense graph optimization |
| **4** | [Kruskal's MST](./Kruskals-MST/) | `Kruskals-MST/` | Edge-centric spanning forest, Disjoint Set Union (DSU), Path compression & rank |
| **5** | [MST Comparative Analysis](./MST-Comparison/) | `MST-Comparison/` | Sparse vs Dense graph empirical benchmarking, Matplotlib visual graphs, CSV logging |

---

## Algorithmic Comparison

| Algorithm | Optimization Goal | Sorting Metric | Time Complexity | Auxiliary Space |
| :--- | :--- | :--- | :---: | :---: |
| **Fractional Knapsack** | Maximize value in capacity $W$ | Ratio $v_i / w_i$ (descending) | $O(n \log n)$ | $O(n)$ |
| **Job Sequencing** | Maximize total scheduled profit | Profit $p_i$ (descending) | $O(n \log n + n \cdot d_{max})$ | $O(d_{max} + n)$ |
| **Prim's MST** | Minimize total spanning tree weight | Minimum key edge in cut | $O(V^2)$ (Matrix) / $O(E \log V)$ | $O(V^2)$ or $O(V+E)$ |
| **Kruskal's MST** | Minimize total spanning tree weight | Edge weight $w(e)$ (ascending) | $O(E \log E) = O(E \log V)$ | $O(V + E)$ |

---

## Execution Instructions
```bash
# Exp 1: Fractional Knapsack
python Unit03-Greedy-Method/Fractional-Knapsack/fractional_knapsack.py

# Exp 2: Job Sequencing with Deadlines
python Unit03-Greedy-Method/Job-Sequencing/job_sequencing.py

# Exp 3: Prim's MST
python Unit03-Greedy-Method/Prims-MST/prims_mst.py

# Exp 4: Kruskal's MST
python Unit03-Greedy-Method/Kruskals-MST/kruskals_mst.py

# Exp 5: MST Empirical Comparison
python Unit03-Greedy-Method/MST-Comparison/mst_comparison.py
```
