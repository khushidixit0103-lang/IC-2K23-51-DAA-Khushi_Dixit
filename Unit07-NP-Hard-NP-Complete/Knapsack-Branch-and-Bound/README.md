# 0/1 Knapsack using Branch and Bound (LCBB)

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 07:** NP-Hard and NP-Complete Problems  

---

## 1. Aim
To design, implement, and analyze the 0/1 Knapsack problem using Least-Cost / Best-First Branch and Bound (LCBB) with continuous upper bounding via Fractional Knapsack.

---

## 2. Problem Statement
Given $n$ items each characterized by $(v_i, w_i)$ and a knapsack capacity $W$, maximize total integer profit without exceeding $W$ using Branch and Bound state-space exploration.

---

## 3. Algorithm (Best-First Search via Max-Heap)
1. Sort items by value-to-weight ratio $v_i / w_i$ in descending order.
2. Initialize priority queue (Max-Heap) prioritized by upper bound.
3. Compute upper bound of root node using Fractional Knapsack on entire capacity $W$. Enqueue root.
4. While priority queue is not empty:
   - Extract node $u$ with maximum upper bound.
   - If $u.bound \le max\_profit$, prune $u$ (cannot lead to better solution).
   - Generate two child states:
     - **Child 1 (Include next item):** Check feasibility ($weight \le W$). If feasible, update $max\_profit$ if $profit > max\_profit$. Calculate upper bound; enqueue if $bound > max\_profit$.
     - **Child 2 (Exclude next item):** Calculate upper bound without including item; enqueue if $bound > max\_profit$.
5. Return $max\_profit$ and optimal item set.

---

## 4. Complexity Analysis
- **Worst-Case Time:** $O(2^n)$ when bounding functions fail to prune branches.
- **Average-Case Time:** $O(2^{k})$ with $k \ll n$ due to aggressive bounding via linear programming relaxation.
- **Space Complexity:** $O(2^n)$ in the worst case to maintain priority queue state records.

---

## 5. Execution Command
```bash
python knapsack_bnb.py
```
