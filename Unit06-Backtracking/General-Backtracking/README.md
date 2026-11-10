# General Backtracking Framework

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 06:** Backtracking  

---

## 1. Aim
To establish the theoretical and practical framework of Backtracking algorithms, demonstrating systematic state-space tree traversal, bounding functions for early subtree pruning, and candidate rollback.

---

## 2. Problem Statement
Many combinatorial search problems require finding vectors $\vec{x} = (x_1, x_2, \dots, x_n)$ satisfying criterion constraints. Backtracking performs a depth-first traversal of the implicit state-space tree, evaluating bounding functions $B(x_1, \dots, x_k)$ at intermediate node $k$. If the partial configuration violates problem constraints, the entire subtree beneath it is pruned without exploring its leaves.

---

## 3. General Algorithmic Template
```text
Algorithm BACKTRACK(k):
    for each choice c in CANDIDATES(k) do:
        if IS_VALID(k, c) then:
            x[k] <- c
            if IS_SOLUTION(x[1..k]) then:
                RECORD_SOLUTION(x[1..k])
            else:
                BACKTRACK(k + 1)
            UNDO_MOVE(k, c)   // Backtrack
```

---

## 4. Execution Command
```bash
python general_backtracking.py
```
