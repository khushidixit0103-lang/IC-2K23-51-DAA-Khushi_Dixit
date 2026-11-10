# Comparative Analysis: Prim's vs Kruskal's MST Algorithms

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 03:** Greedy Method  

---

## 1. Aim
To theoretically and empirically compare the performance of Prim's Algorithm and Kruskal's Algorithm across diverse graph topologies, evaluating running times on sparse and dense graphs with varying edge densities.

---

## 2. Theoretical Comparison

| Feature | Prim's Algorithm | Kruskal's Algorithm |
| :--- | :--- | :--- |
| **Strategy** | Vertex-centric; grows a single tree from a start node | Edge-centric; merges a forest of trees |
| **Data Structures** | Adjacency matrix/list + Priority Queue | Edge list + Disjoint Set Union (Union-Find) |
| **Cycle Handling** | Inherently acyclic (only cross-cut edges evaluated) | DSU cycle detection via `Find(u) == Find(v)` |
| **Time Complexity (Matrix)** | $\Theta(V^2)$ | $O(E \log E)$ |
| **Time Complexity (Heap)** | $O(E \log V)$ | $O(E \log V)$ |
| **Graph Suitability** | Highly preferred for **Dense graphs** ($E \approx V^2$) | Highly preferred for **Sparse graphs** ($E \ll V^2$) |
| **Space Complexity** | $O(V^2)$ or $O(V + E)$ | $O(V + E)$ |

---

## 3. Empirical Observations
1. **Sparse Graphs:** When edge count $|E| = O(V)$, Kruskal's algorithm requires sorting very few edges, yielding faster convergence.
2. **Dense Graphs:** When edge count approaches complete connectivity ($|E| \approx \frac{V(V-1)}{2}$), sorting all edges incurs a high penalty ($O(V^2 \log V)$), making matrix-based Prim's algorithm ($\Theta(V^2)$) more efficient.
3. **Correctness Check:** Both algorithms always yield identical total minimum spanning tree weights across all generated benchmark graphs.

---

## 4. Generated Artifacts
- **Benchmark Data:** `results.csv` and `docs/performance-analysis/unit03_mst_comparison.csv`
- **Visualization Graphs:** `mst_comparison.png` and `docs/performance-analysis/unit03_mst_comparison_plot.png`

---

## 5. Execution Command
```bash
python mst_comparison.py
```
