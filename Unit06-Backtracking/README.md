# Unit 06: Backtracking

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Outcome:** CO4 — Ability to design, formulate, and analyze backtracking search strategies using depth-first tree traversal and bounding functions.

---

## Unit Overview
Backtracking is a systematic method for exploring candidate solution spaces to solve combinatorial satisfaction and optimization problems. It organizes candidates into an implicit state-space tree and prunes non-promising paths early using problem-specific bounding constraints.

---

## Experiments

| Exp No. | Experiment Title | Directory | Key Concepts Covered |
| :---: | :--- | :--- | :--- |
| **1** | [General Backtracking](./General-Backtracking/) | `General-Backtracking/` | Generic template, State-space tree, Pruning invalid subtrees |
| **2** | [Queens Problem](./Queens-Problem/) | `Queens-Problem/` | 4-Queens, 8-Queens, Scalable N-Queens, Diagonal conflict formulas |
| **3** | [Sum of Subsets](./Sum-of-Subsets/) | `Sum-of-Subsets/` | Binary inclusion tree, Dual upper and lower bounding criteria |
| **4** | [Backtracking vs Exhaustive Search](./Backtracking-vs-Exhaustive/) | `Backtracking-vs-Exhaustive/` | Empirical state-space evaluation, CSV logging, Pruning visualization plots |

---

## Complexity Summary

| Problem | Solution Vector | Worst-Case Complexity | Average Nodes Explored with Backtracking |
| :--- | :--- | :---: | :---: |
| **N-Queens** | $X = (x_1, \dots, x_N)$ where $x_i \in \{0..N-1\}$ | $O(N!)$ | $\ll N!$ ($99.98\%$ states pruned at $N=8$) |
| **Sum of Subsets** | $X = (x_1, \dots, x_n)$ where $x_i \in \{0, 1\}$ | $O(2^n)$ | Bound-pruned binary decision tree |
| **Constrained Permutations** | Distinct sequence | $O(N!)$ | Local difference pruning |

---

## Execution Instructions
```bash
# Exp 1: General Backtracking Framework
python Unit06-Backtracking/General-Backtracking/general_backtracking.py

# Exp 2: N-Queens Problem
python Unit06-Backtracking/Queens-Problem/n_queens.py

# Exp 3: Sum of Subsets
python Unit06-Backtracking/Sum-of-Subsets/sum_of_subsets.py

# Exp 4: Backtracking vs Exhaustive Benchmark
python Unit06-Backtracking/Backtracking-vs-Exhaustive/backtracking_vs_exhaustive.py
```
