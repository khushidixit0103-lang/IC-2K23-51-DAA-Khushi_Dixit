# Floyd-Warshall Algorithm (All-Pairs Shortest Path)

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 04:** Dynamic Programming  

---

## 1. Aim
To design, implement, and analyze the Floyd-Warshall algorithm for finding the shortest paths between all pairs of vertices in a directed weighted graph, identifying negative-weight cycles and reconstructing shortest path trajectories.

---

## 2. Problem Statement
Given a directed graph $G = (V, E)$ with edge weights $w: E \to \mathbb{R}$ that may include negative values, determine the shortest path weight $d(u, v)$ for all pairs of vertices $u, v \in V$, or report if the graph contains a negative-weight cycle.

---

## 3. Dynamic Programming Formulation
Let $D^{(k)}[i][j]$ represent the length of the shortest path from vertex $i$ to vertex $j$ with all intermediate vertices chosen from the subset $\{1, 2, \dots, k\}$.

### Base Case ($k = 0$):
$$D^{(0)}[i][j] = \begin{cases} 0 & \text{if } i = j \\ w(i, j) & \text{if } (i, j) \in E \\ \infty & \text{otherwise} \end{cases}$$

### Recursive Step ($k = 1, \dots, |V|$):
$$D^{(k)}[i][j] = \min\Big( D^{(k-1)}[i][j], \; D^{(k-1)}[i][k] + D^{(k-1)}[k][j] \Big)$$

### Predecessor Update:
$$\Pi^{(k)}[i][j] = \begin{cases} \Pi^{(k-1)}[k][j] & \text{if } D^{(k-1)}[i][k] + D^{(k-1)}[k][j] < D^{(k-1)}[i][j] \\ \Pi^{(k-1)}[i][j] & \text{otherwise} \end{cases}$$

### Negative Cycle Detection:
If $\exists i \in V$ such that $D^{(|V|)}[i][i] < 0$, a negative-weight cycle exists.

---

## 4. Complexity Analysis
- **Time Complexity:** $\Theta(|V|^3)$ operations from three deeply nested loops iterating from $1$ to $|V|$.
- **Space Complexity:** $\Theta(|V|^2)$ storage for distance and predecessor matrices.

---

## 5. Execution Command
```bash
python floyd_warshall.py
```
