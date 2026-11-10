# N-Queens Problem using Backtracking

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 06:** Backtracking  

---

## 1. Aim
To design, implement, and analyze the N-Queens problem using Backtracking, examining safe positioning constraints, bounding function pruning, and visual board layouts for 4-Queens, 8-Queens, and general $N$.

---

## 2. Problem Statement
Place $N$ chess queens on an $N \times N$ chessboard such that no two queens attack each other:
1. No two queens in the same row.
2. No two queens in the same column.
3. No two queens on the same major or minor diagonal.

---

## 3. Mathematical Constraints
Let $board[i]$ denote the column index of the queen placed on row $i$.  
For any pair of queens on rows $i$ and $j$ ($i \neq j$):
1. **Column Conflict:** $board[i] \neq board[j]$
2. **Diagonal Conflict:** $|board[i] - board[j]| \neq |i - j|$

---

## 4. Backtracking Pruning Efficiency
- For $N = 4$: Explores **17 nodes** out of $4^4 = 256$ candidates ($93.4\%$ pruned), discovering **2 valid solutions**.
- For $N = 8$: Explores **2,057 nodes** out of $8^8 = 16,777,216$ states ($99.9877\%$ pruned), finding all **92 valid solutions**.

---

## 5. Execution Command
```bash
python n_queens.py
```
