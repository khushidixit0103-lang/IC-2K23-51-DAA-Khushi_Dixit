# Binary Tree Traversals (Recursive and Iterative)

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 05:** Traversal and Search  

---

## 1. Aim
To construct a binary tree data structure and implement Pre-order, In-order, and Post-order depth-first traversals using both recursive function calls and explicit iterative stack simulations.

---

## 2. Theoretical Background

| Traversal | Processing Sequence | Primary Applications |
| :--- | :--- | :--- |
| **Pre-order** | Root $\to$ Left $\to$ Right | Cloning trees, Prefix expressions (Polish notation), Serializing tree topologies |
| **In-order** | Left $\to$ Root $\to$ Right | Yields non-decreasing sorted order on Binary Search Trees (BST) |
| **Post-order** | Left $\to$ Right $\to$ Root | Deleting/freeing nodes, Postfix evaluation (Reverse Polish notation), Bottom-up property synthesis |

---

## 3. Complexity Analysis
- **Time Complexity:** Every node in the tree of size $N$ is visited exactly once:
  $$\Theta(N)$$
- **Space Complexity:**
  - **Recursive:** $O(h)$ auxiliary stack memory where $h$ is tree height ($O(\log N)$ best/balanced, $O(N)$ worst/skewed).
  - **Iterative:** $O(h)$ explicit stack memory ($O(N)$ for two-stack post-order).

---

## 4. Execution Command
```bash
python tree_traversals.py
```
