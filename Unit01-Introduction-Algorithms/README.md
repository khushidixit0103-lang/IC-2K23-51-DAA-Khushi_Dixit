# Unit 01: Introduction to Algorithms and Performance Analysis

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Outcome:** CO1 — Ability to design, analyze, and benchmark foundational algorithms and complexity bounds.

---

## Unit Overview
Unit 01 lays the foundation for algorithm analysis, formal asymptotic notations ($O, \Omega, \Theta$), and empirical verification. The unit explores fundamental linear and search operations on arrays, contrasting iterative control flow with recursive divide-and-conquer formulations, and measures their practical performance across varying problem dimensions.

---

## Experiments

| Exp No. | Experiment Title | Directory | Key Concepts Covered |
| :---: | :--- | :--- | :--- |
| **1** | [Basic Array Operations](./Basic-Array-Operations/) | `Basic-Array-Operations/` | Traversal, Insertion, Deletion, Linear Search, Update, In-place Reversal, Bounds checking |
| **2** | [Iterative Binary Search](./Iterative-Binary-Search/) | `Iterative-Binary-Search/` | Half-interval search, Loop invariant, $O(1)$ space, Best/Avg/Worst case analysis |
| **3** | [Recursive Binary Search](./Recursive-Binary-Search/) | `Recursive-Binary-Search/` | Divide-and-conquer, Recurrence $T(n) = T(n/2) + \Theta(1)$, Stack frame overhead |
| **4** | [Performance Analysis](./Performance-Analysis/) | `Performance-Analysis/` | Empirical benchmarking, Microsecond timers, CSV data logging, Matplotlib visualization |

---

## Summary of Complexity Results

| Operation / Algorithm | Best Case | Average Case | Worst Case | Space Complexity |
| :--- | :---: | :---: | :---: | :---: |
| **Array Traversal** | $O(n)$ | $O(n)$ | $O(n)$ | $O(1)$ |
| **Array Insertion** | $O(1)$ (end) | $O(n)$ | $O(n)$ (start) | $O(1)$ |
| **Array Deletion** | $O(1)$ (end) | $O(n)$ | $O(n)$ (start) | $O(1)$ |
| **Array Linear Search**| $\Omega(1)$ | $\Theta(n)$ | $O(n)$ | $O(1)$ |
| **Iterative Binary Search** | $\Omega(1)$ | $\Theta(\log n)$ | $O(\log n)$ | $O(1)$ |
| **Recursive Binary Search** | $\Omega(1)$ | $\Theta(\log n)$ | $O(\log n)$ | $O(\log n)$ stack |

---

## Instructions for Execution
Navigate to any experiment directory and invoke the corresponding Python script using the local Python interpreter:
```bash
# Experiment 1
python Unit01-Introduction-Algorithms/Basic-Array-Operations/array_operations.py

# Experiment 2
python Unit01-Introduction-Algorithms/Iterative-Binary-Search/binary_search_iterative.py

# Experiment 3
python Unit01-Introduction-Algorithms/Recursive-Binary-Search/binary_search_recursive.py

# Experiment 4
python Unit01-Introduction-Algorithms/Performance-Analysis/performance_analysis.py
```
