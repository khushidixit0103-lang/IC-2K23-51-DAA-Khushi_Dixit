# Strassen's Matrix Multiplication

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 02:** Divide and Conquer  

---

## 1. Aim
To design, implement, and evaluate Strassen's Matrix Multiplication algorithm using the Divide-and-Conquer paradigm, demonstrating a reduction in scalar multiplications from 8 to 7, resulting in sub-cubic asymptotic time complexity $O(n^{\log_2 7}) \approx O(n^{2.807})$.

---

## 2. Problem Statement
Given two square matrices $A, B \in \mathbb{R}^{n \times n}$, compute their product $C = A \times B$ where:
$$C_{ij} = \sum_{k=1}^n A_{ik} B_{kj}$$
Standard matrix multiplication performs $n^3$ scalar multiplications and $n^2(n-1)$ additions ($O(n^3)$). Strassen's approach optimizes the multiplication count using clever algebraic combinations.

---

## 3. Algorithm
1. **Partitioning:** Divide $A$ and $B$ each into four equal submatrices of dimension $\frac{n}{2} \times \frac{n}{2}$:
   $$A = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}, \quad B = \begin{pmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{pmatrix}$$
2. **7 Recursive Products:**
   - $M_1 = (A_{11} + A_{22})(B_{11} + B_{22})$
   - $M_2 = (A_{21} + A_{22}) B_{11}$
   - $M_3 = A_{11} (B_{12} - B_{22})$
   - $M_4 = A_{22} (B_{21} - B_{11})$
   - $M_5 = (A_{11} + A_{12}) B_{22}$
   - $M_6 = (A_{21} - A_{11})(B_{11} + B_{12})$
   - $M_7 = (A_{12} - A_{22})(B_{21} + B_{22})$
3. **Quadrant Recombination:**
   - $C_{11} = M_1 + M_4 - M_5 + M_7$
   - $C_{12} = M_3 + M_5$
   - $C_{21} = M_2 + M_4$
   - $C_{22} = M_1 - M_2 + M_3 + M_6$
4. **Dimension Handling:** If $n$ is not a power of 2, pad matrices with rows and columns of zeros up to the next power of 2, compute the product, and extract the valid $n \times n$ submatrix.

---

## 4. Recurrence Relation & Master Theorem
$$T(n) = 7 T(n/2) + \Theta(n^2)$$

Here: $a = 7, b = 2, f(n) = \Theta(n^2)$.
$$\log_b a = \log_2 7 \approx 2.80735$$
Since $f(n) = O(n^{\log_b a - \epsilon})$ for $\epsilon \approx 0.807 > 0$, Master Theorem Case 1 applies:
$$T(n) = \Theta(n^{\log_2 7}) \approx \Theta(n^{2.807})$$

---

## 5. Comparison: Standard vs Strassen

| Metric | Standard Matrix Multiplication | Strassen's Algorithm |
| :--- | :--- | :--- |
| **Scalar Multiplications** | $n^3$ | $n^{\log_2 7} \approx n^{2.807}$ |
| **Scalar Additions** | $n^3 - n^2$ | $18(n/2)^2 = 4.5 n^2$ additions per level |
| **Time Complexity** | $\Theta(n^3)$ | $\Theta(n^{2.807})$ |
| **Space Complexity** | $O(1)$ auxiliary | $O(n^2)$ recursion buffers |
| **Crossover Point** | Faster for small matrices ($n \le 64$) | Asymptotically faster for large matrices |

---

## 6. Execution Command
```bash
python strassen_matrix_mult.py
```
