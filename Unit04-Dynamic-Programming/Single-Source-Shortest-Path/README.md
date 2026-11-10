# Single-Source Shortest Path (Bellman-Ford Algorithm)

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 04:** Dynamic Programming  

---

## 1. Aim
To design, implement, and analyze the Bellman-Ford Dynamic Programming algorithm for computing single-source shortest paths in directed weighted graphs with possible negative edge weights, while reliably detecting negative-weight cycles.

---

## 2. Problem Statement
Given a directed graph $G = (V, E)$, edge weights $w: E \to \mathbb{R}$, and a source vertex $s \in V$, compute shortest paths from $s$ to all $v \in V$, or report that a negative-weight cycle reachable from $s$ exists.

---

## 3. Dynamic Programming Formulation
Let $dist^{(k)}[v]$ be the length of the shortest path from $s$ to $v$ using at most $k$ edges.

### Base Case ($k = 0$):
$$dist^{(0)}[v] = \begin{cases} 0 & \text{if } v = s \\ \infty & \text{if } v \neq s \end{cases}$$

### Relaxation Recurrence ($k = 1, \dots, |V| - 1$):
$$dist^{(k)}[v] = \min\Big( dist^{(k-1)}[v], \; \min_{(u, v) \in E} \{ dist^{(k-1)}[u] + w(u, v) \} \Big)$$

### Negative Cycle Detection:
If on the $|V|$-th iteration:
$$\exists (u, v) \in E \quad \text{such that} \quad dist[u] + w(u, v) < dist[v]$$
then a negative-weight cycle is reachable from $s$.

---

## 4. Complexity Analysis
- **Time Complexity:** Relaxing $|E|$ edges for $|V|-1$ rounds gives $O(|V| \cdot |E|)$ worst-case time.
- **Space Complexity:** $O(|V|)$ auxiliary space for `dist` and `parent` lookup tables.

---

## 5. Execution Command
```bash
python bellman_ford.py
```
