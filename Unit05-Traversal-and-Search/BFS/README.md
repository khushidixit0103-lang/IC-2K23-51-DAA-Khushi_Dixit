# Breadth-First Search (BFS)

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 05:** Traversal and Search  

---

## 1. Aim
To design, implement, and analyze Breadth-First Search (BFS) for graph exploration, establishing its level-order properties and unweighted shortest path guarantees.

---

## 2. Problem Statement
Given an undirected or directed graph $G = (V, E)$ and a source vertex $s \in V$, systematically explore all reachable vertices of $G$ such that all vertices at distance $k$ from $s$ are discovered before any vertices at distance $k+1$.

---

## 3. Algorithm
1. Initialize array `visited[v] = False`, `dist[v] = \infty`, and `parent[v] = None` for all $v \in V$.
2. Enqueue source $s$: `visited[s] = True`, `dist[s] = 0`.
3. While queue is not empty:
   - Dequeue front vertex $u$.
   - Append $u$ to traversal result.
   - For each adjacent vertex $v \in Adj[u]$:
     - If not `visited[v]`:
       - `visited[v] = True`
       - `dist[v] = dist[u] + 1`
       - `parent[v] = u`
       - Enqueue $v$.

---

## 4. Complexity Analysis
- **Time Complexity:**
  - Every vertex is enqueued and dequeued at most once: $O(V)$.
  - The adjacency list of each vertex is scanned only when dequeued: $\sum_{u \in V} \text{deg}(u) = 2E$ (undirected).
  - Total Time: $\Theta(V + E)$ (Adjacency List) / $\Theta(V^2)$ (Adjacency Matrix).
- **Space Complexity:** Queue and auxiliary lookup arrays require $O(V)$ auxiliary memory.

---

## 5. Execution Command
```bash
python bfs.py
```
