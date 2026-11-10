# Graph Representations: Adjacency Matrix vs Adjacency List

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 05:** Traversal and Search  

---

## 1. Aim
To construct, implement, and benchmark the two canonical in-memory representations of graph data structures: Adjacency Matrix and Adjacency List, evaluating time/space trade-offs for sparse and dense graphs.

---

## 2. Theoretical Breakdown

| Operation / Metric | Adjacency Matrix | Adjacency List | Preferred Structure |
| :--- | :--- | :--- | :--- |
| **Space Complexity** | $\Theta(V^2)$ | $\Theta(V + E)$ | List for sparse ($E \ll V^2$), Matrix for dense ($E \approx V^2$) |
| **Check Edge $(u, v)$** | $\Theta(1)$ | $O(\text{deg}(u))$ | Matrix |
| **Find All Neighbors of $u$** | $\Theta(V)$ | $\Theta(\text{deg}(u))$ | List |
| **Add Edge** | $\Theta(1)$ | $\Theta(1)$ | Both |
| **Delete Edge** | $\Theta(1)$ | $O(\text{deg}(u))$ | Matrix |
| **Memory Overhead for Zeroes** | Yes (stores zeroes for non-edges) | No (stores actual edges only) | List |

---

## 3. Execution Command
```bash
python graph_representations.py
```
