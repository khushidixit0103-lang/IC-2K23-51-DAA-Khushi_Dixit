# Kruskal's Minimum Spanning Tree Algorithm

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 03:** Greedy Method  

---

## 1. Aim
To design, implement, and analyze Kruskal's Algorithm for finding the Minimum Spanning Tree of a connected, undirected graph using global edge sorting and Disjoint Set Union (Union-Find) with path compression and rank optimization.

---

## 2. Problem Statement
Given an undirected, weighted graph $G = (V, E)$ with edge weights $w: E \to \mathbb{R}$, select a subset of edges $T \subseteq E$ such that $T$ connects all vertices without cycles and $\sum_{e \in T} w(e)$ is minimized.

---

## 3. Algorithm
1. Treat each vertex $v \in V$ as an individual singleton set (`MakeSet(v)`).
2. Sort all edges $E$ in non-decreasing order of weight $w(e)$ in $O(E \log E)$ time.
3. Initialize empty tree edge list $T = \emptyset$.
4. For each edge $(u, v) \in E$ in sorted order:
   - If $\text{Find}(u) \neq \text{Find}(v)$ (i.e., $u$ and $v$ belong to different connected components):
     - Add $(u, v)$ to $T$.
     - $\text{Union}(u, v)$.
     - If $|T| == |V| - 1$, terminate early.
5. Return spanning tree edges $T$.

---

## 4. Complexity Analysis

| Phase | Operation | Complexity |
| :--- | :--- | :--- |
| **Edge Sorting** | Comparison sort on $\|E\|$ edges | $O(E \log E) = O(E \log V)$ |
| **DSU Operations** | $2E$ `Find` operations + $V - 1$ `Union` operations | $O(E \cdot \alpha(V))$ |
| **Overall Time** | Dominated by edge sorting | $O(E \log E)$ or $O(E \log V)$ |
| **Space Complexity** | Parent array, Rank array, Edge list | $O(V + E)$ |

*(Here $\alpha$ is the extremely slow-growing inverse Ackermann function, where $\alpha(V) \le 4$ for all practical universe sizes).*

---

## 5. Execution Command
```bash
python kruskals_mst.py
```
