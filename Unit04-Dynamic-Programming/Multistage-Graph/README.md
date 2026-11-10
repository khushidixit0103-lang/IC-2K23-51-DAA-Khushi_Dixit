# Multistage Graph Shortest Path using Dynamic Programming

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 04:** Dynamic Programming  

---

## 1. Aim
To design, implement, and analyze the Multistage Graph shortest path problem using the backward Dynamic Programming approach.

---

## 2. Problem Statement
A multistage graph $G = (V, E)$ is a directed, weighted graph whose vertices are partitioned into $k \ge 2$ disjoint stages $V_1, V_2, \dots, V_k$ such that if $(u, v) \in E$, then $u \in V_i$ and $v \in V_{i+1}$ for some $1 \le i < k$.  
Stage $V_1$ contains a single source vertex $s$ and stage $V_k$ contains a single destination vertex $t$. The objective is to find a minimum-cost directed path from $s$ to $t$.

---

## 3. Dynamic Programming Formulation (Backward Approach)
Let $cost(i)$ be the cost of the shortest path from vertex $i$ to destination $t$:
$$cost(t) = 0$$
For any vertex $i \in V_j$ ($1 \le j < k$):
$$cost(i) = \min_{(i, r) \in E} \Big\{ c(i, r) + cost(r) \Big\}$$
The decision array $d(i)$ stores the successor node $r$ that achieves the minimum:
$$d(i) = \arg\min_{(i, r) \in E} \Big\{ c(i, r) + cost(r) \Big\}$$

---

## 4. Complexity Analysis
- **Time Complexity:** Each directed edge in the graph is examined exactly once during the backward scan. Hence, time complexity is:
  $$O(|V| + |E|)$$
- **Space Complexity:** Storing `cost` and `decision` arrays for all vertices requires $O(|V|)$ space.

---

## 5. Execution Command
```bash
python multistage_graph.py
```
