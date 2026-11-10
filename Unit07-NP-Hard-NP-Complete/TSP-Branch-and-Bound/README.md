# Travelling Salesperson Problem using Branch and Bound (Reduced Matrix Method)

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 07:** NP-Hard and NP-Complete Problems  

---

## 1. Aim
To design, implement, and analyze the Travelling Salesperson Problem (TSP) using Least-Cost Branch and Bound (LCBB) with the Reduced Cost Matrix lower bounding technique.

---

## 2. Problem Statement
Given an $n \times n$ cost matrix representing travel costs between $n$ cities, find a tour of minimal cost visiting every city once and returning to the starting point.

---

## 3. Reduced Cost Matrix Algorithm
1. **Matrix Reduction:**
   - Subtract the minimum element of each row from all entries in that row.
   - Subtract the minimum element of each column from all entries in that column.
   - The sum of all subtracted values gives the lower bound $L_0$ for the root node.
2. **Branching:**
   - From current vertex $i$ to unvisited vertex $j$:
     - Set row $i$ and column $j$ in the reduced matrix to $\infty$.
     - Set entry $(j, 0) = \infty$ to prevent premature return to origin.
     - Perform row and column reductions on the remaining matrix, yielding reduction cost $r$.
     - Lower bound of child node:
       $$\text{cost}(child) = \text{cost}(parent) + \hat{A}[i][j] + r$$
       where $\hat{A}[i][j]$ is the value in the parent's reduced matrix.
3. **State Exploration:**
   - Enqueue child nodes into a Min-Heap.
   - Prune any node whose cost exceeds the best complete tour cost discovered so far.

---

## 4. Execution Command
```bash
python tsp_bnb.py
```
