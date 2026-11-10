# Job Sequencing with Deadlines

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 03:** Greedy Method  

---

## 1. Aim
To design, implement, and analyze the Job Sequencing with Deadlines problem using a greedy strategy to maximize aggregate profit within discrete processing time slots.

---

## 2. Problem Statement
Given a set of $n$ jobs where each job $J_i = (id_i, d_i, p_i)$ has:
- Deadline $d_i \ge 1$
- Profit $p_i > 0$ earned if completed by time $d_i$
- Unit duration (1 time slot per job)
- Single processor capacity (at most 1 job processed simultaneously)

Find a feasible execution sequence that maximizes total profit.

---

## 3. Algorithm
1. Sort all jobs in descending order of profit $p_i$.
2. Determine maximum deadline: $d_{max} = \max_{i} d_i$.
3. Allocate an array `slots[1 ... d_max]` initialized to empty.
4. For each job $J_i$ in sorted order:
   - Search backwards for an unoccupied slot $k \in \{d_i, d_i-1, \dots, 1\}$.
   - If found:
     - Assign `slots[k] = J_i`.
     - Accumulate profit $p_i$.
   - If no slot is free before or at $d_i$, discard job $J_i$.
5. Return scheduled jobs and total profit.

---

## 4. Complexity Analysis

| Component | Standard Implementation | Disjoint-Set Union (DSU) Variant |
| :--- | :--- | :--- |
| **Sorting Jobs** | $O(n \log n)$ | $O(n \log n)$ |
| **Slot Allocation** | $O(n \cdot d_{max})$ worst-case | $O(n \cdot \alpha(d_{max}))$ |
| **Overall Time** | $O(n \log n + n \cdot d_{max})$ | $O(n \log n)$ |
| **Space Complexity** | $O(d_{max} + n)$ | $O(d_{max} + n)$ |

---

## 5. Execution Command
```bash
python job_sequencing.py
```
