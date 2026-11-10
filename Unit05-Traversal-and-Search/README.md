# Unit 05: Traversal and Search

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Outcome:** CO6 — Ability to design, implement, and analyze tree and graph search strategies, state-space exploration, and complexity boundaries.

---

## Unit Overview
Tree and graph traversals are fundamental to computational algorithmic problem solving. Search algorithms visit every node and edge of structured networks systematically, unlocking foundational capabilities such as component identification, reachability, shortest paths, and topological ordering.

---

## Experiments

| Exp No. | Experiment Title | Directory | Key Concepts Covered |
| :---: | :--- | :--- | :--- |
| **1** | [Binary Tree Traversals](./Tree-Traversals/) | `Tree-Traversals/` | Pre-order, In-order, Post-order; Recursive stack vs Iterative explicit stack |
| **2** | [Graph Representations](./Graph-Representations/) | `Graph-Representations/` | Adjacency Matrix vs Adjacency List, Space efficiency, Edge verification |
| **3** | [Breadth-First Search (BFS)](./BFS/) | `BFS/` | FIFO Queue, Level-order exploration, Unweighted shortest paths, $O(V + E)$ |
| **4** | [Depth-First Search (DFS)](./DFS/) | `DFS/` | LIFO Stack, Discovery/finishing timestamps, Back edges, Cycle detection |
| **5** | [BFS vs DFS Comparison](./BFS-vs-DFS/) | `BFS-vs-DFS/` | Synthetic benchmark ($|V| \le 5000$), CSV logs, Runtime scaling curves |

---

## Complexity Summary

| Search Strategy | Frontier Type | Time Complexity (List) | Time Complexity (Matrix) | Auxiliary Space |
| :--- | :--- | :---: | :---: | :---: |
| **Binary Tree Pre-order** | Stack / Call Frame | $\Theta(N)$ | N/A | $O(h)$ |
| **Binary Tree In-order** | Stack / Call Frame | $\Theta(N)$ | N/A | $O(h)$ |
| **Binary Tree Post-order** | 2-Stack / Call Frame| $\Theta(N)$ | N/A | $O(h)$ / $O(N)$ |
| **Breadth-First Search** | FIFO Queue | $\Theta(V + E)$ | $\Theta(V^2)$ | $O(V)$ |
| **Depth-First Search** | LIFO Stack / Rec | $\Theta(V + E)$ | $\Theta(V^2)$ | $O(V)$ |

---

## Execution Instructions
```bash
# Exp 1: Tree Traversals
python Unit05-Traversal-and-Search/Tree-Traversals/tree_traversals.py

# Exp 2: Graph Representations
python Unit05-Traversal-and-Search/Graph-Representations/graph_representations.py

# Exp 3: BFS
python Unit05-Traversal-and-Search/BFS/bfs.py

# Exp 4: DFS
python Unit05-Traversal-and-Search/DFS/dfs.py

# Exp 5: BFS vs DFS Benchmark
python Unit05-Traversal-and-Search/BFS-vs-DFS/bfs_vs_dfs_comparison.py
```
