# Depth-First Search (DFS)

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 05:** Traversal and Search  

---

## 1. Aim
To design, implement, and analyze Depth-First Search (DFS) for graph traversal using recursive call stacks and iterative explicit stacks, establishing discovery and finishing timestamps and detecting graph cycles via back edges.

---

## 2. Problem Statement
Given a graph $G = (V, E)$, explore edges out of the most recently discovered vertex $v$ that still has unexplored edges leaving it, backtracking when all edges of $v$ have been explored.

---

## 3. Algorithm
1. Color all vertices WHITE, set $time = 0$.
2. For each vertex $u \in V$:
   - If $color[u] == \text{WHITE}$:
     - Call `DFS_VISIT(u)`.
3. `DFS_VISIT(u)`:
   - $time \leftarrow time + 1$; $d[u] \leftarrow time$; $color[u] \leftarrow \text{GRAY}$.
   - For each $v \in Adj[u]$:
     - If $color[v] == \text{WHITE}$:
       - $parent[v] \leftarrow u$; call `DFS_VISIT(v)` (Tree edge).
     - Else if $color[v] == \text{GRAY}$ and $parent[u] \neq v$:
       - Cycle detected (Back edge).
   - $color[u] \leftarrow \text{BLACK}$; $time \leftarrow time + 1$; $f[u] \leftarrow time$.

---

## 4. Complexity Analysis
- **Time Complexity:**
  - Every vertex is colored WHITE $\to$ GRAY $\to$ BLACK once: $O(V)$.
  - Adjacency list scanned once per vertex: $O(E)$.
  - Total Time: $\Theta(V + E)$ (Adjacency List) / $\Theta(V^2)$ (Adjacency Matrix).
- **Space Complexity:** Recursion/explicit stack consumes $O(V)$ auxiliary memory in the worst case (e.g., linear chain graph).

---

## 5. Execution Command
```bash
python dfs.py
```
