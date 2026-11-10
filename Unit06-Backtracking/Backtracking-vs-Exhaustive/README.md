# Comparative Analysis: Backtracking vs Exhaustive Search

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 06:** Backtracking  

---

## 1. Aim
To quantitatively analyze the computational advantages of Backtracking over brute-force Exhaustive Search by measuring state-space tree nodes evaluated and CPU running times across scaling problem sizes ($N \in [4, 9]$) on the $N$-Queens problem.

---

## 2. Experimental Principles
- **Exhaustive Search:** Generates the entire combinatorial permutation space of candidate vectors ($N!$), verifying constraints only upon reaching the leaf level.
- **Backtracking:** Employs incremental candidate testing via bounding functions, terminating exploration of an entire subtree the moment a constraint violation is detected at depth $k < N$.

---

## 3. Empirical Results Summary
- At $N = 9$:
  - Exhaustive search explores **986,410 nodes**.
  - Backtracking explores **8,394 nodes**.
  - **Pruning Rate:** $> 99.15\%$ of the search space is pruned without visiting.
  - **Speedup:** Backtracking is orders of magnitude faster while finding the exact identical solution set.

---

## 4. Generated Artifacts
- **Benchmark Data:** `results.csv` and `docs/performance-analysis/unit06_backtracking_vs_exhaustive.csv`
- **Visualization:** `backtracking_vs_exhaustive.png` and `docs/performance-analysis/unit06_backtracking_vs_exhaustive_plot.png`

---

## 5. Execution Command
```bash
python backtracking_vs_exhaustive.py
```
