# Prim's Minimum Spanning Tree Algorithm

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 03:** Greedy Method  

---

## 1. Aim
To design, implement, and analyze Prim's Algorithm for finding a Minimum Spanning Tree (MST) of a weighted, connected, undirected graph using a greedy cut-property strategy.

---

## 2. Problem Statement
Given an undirected, connected, weighted graph $G = (V, E, w)$, find an acyclic subgraph $T = (V, E')$ that spans all vertices $V$ with $|V| - 1$ edges such that total weight:
$$w(T) = \sum_{e \in E'} w(e)$$
is minimized.

---

## 3. Algorithm
1. Initialize a set $S = \{s\}$ where $s$ is an arbitrary source vertex.
2. Maintain array `key[v]` initialized to $\infty$ for all $v \in V \setminus \{s\}$, and `key[s] = 0`.
3. While $|S| < |V|$:
   - Select vertex $u \notin S$ with minimum `key[u]`.
   - Add $u$ to $S$ ($S \leftarrow S \cup \{u\}$).
   - For every adjacent vertex $v$ of $u$:
     - If $v \notin S$ and weight $w(u, v) < key[v]$:
       - Update $key[v] = w(u, v)$.
       - Set `parent[v] = u`.
4. The set of edges $\{(parent[v], v) \mid v \in V \setminus \{s\}\}$ defines the MST.

---

## 4. Complexity Analysis

| Data Structure Used | Extract-Min Time | Key Update (Decrease-Key) | Total Time Complexity |
| :--- | :--- | :--- | :--- |
| **Adjacency Matrix + Array** | $O(V)$ | $O(1)$ | $O(V^2)$ (Optimal for dense graphs) |
| **Adjacency List + Binary Heap** | $O(\log V)$ | $O(\log V)$ | $O(E \log V)$ (Optimal for sparse graphs) |
| **Fibonacci Heap** | $O(\log V)$ amortized | $O(1)$ amortized | $O(E + V \log V)$ |
| **Space Complexity** | $O(V^2)$ matrix / $O(V + E)$ list | - | - |

---

## 5. Execution Command
```bash
python prims_mst.py
```
