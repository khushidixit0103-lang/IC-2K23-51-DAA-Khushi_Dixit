# Comparative Analysis: BFS vs DFS

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 05:** Traversal and Search  

---

## 1. Aim
To theoretically and empirically compare Breadth-First Search (BFS) and Depth-First Search (DFS) on large-scale graphs, examining frontier data structures, memory bounds, and algorithmic performance.

---

## 2. Comparative Matrix

| Characteristic | Breadth-First Search (BFS) | Depth-First Search (DFS) |
| :--- | :--- | :--- |
| **Frontier Structure** | Queue (FIFO) | Stack (LIFO) or Recursion |
| **Search Progression** | Level by level (shallowest first) | Path by path (deepest first) |
| **Shortest Path** | Guarantees shortest path in unweighted graphs | Does not guarantee shortest paths |
| **Time Complexity** | $\Theta(V + E)$ | $\Theta(V + E)$ |
| **Space Complexity** | $O(\text{Width}) \approx O(b^d)$ | $O(\text{Depth}) \approx O(b \cdot d)$ |
| **Cycle Detection** | Cross edges indicate cycles | Back edges indicate cycles |
| **Target Use-Cases** | Routing, social network hops, web crawlers | Topological sort, strong connectivity, maze solving |

---

## 3. Generated Artifacts
- **Benchmark Data:** `results.csv` and `docs/performance-analysis/unit05_bfs_vs_dfs_comparison.csv`
- **Visualization:** `bfs_vs_dfs.png` and `docs/performance-analysis/unit05_bfs_vs_dfs_plot.png`

---

## 4. Execution Command
```bash
python bfs_vs_dfs_comparison.py
```
