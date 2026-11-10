# Exhaustive Search on NP-Hard Problems

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 07:** NP-Hard and NP-Complete Problems  

---

## 1. Aim
To formulate, implement, and analyze Exhaustive Search on NP-Hard combinatorial problems, demonstrating the combinatorial explosion of $2^n$ state spaces and establishing why heuristic, approximation, or branch-and-bound techniques are essential.

---

## 2. Theoretical Background
- **Class P:** Problems solvable in deterministic polynomial time ($O(n^k)$).
- **Class NP:** Decision problems whose solutions can be verified in deterministic polynomial time.
- **NP-Complete:** The hardest problems in NP; every problem in NP is polynomial-time reducible to them (Cook-Levin Theorem).
- **NP-Hard:** Problems at least as hard as NP-Complete problems, not necessarily in NP (e.g., optimization versions of TSP, Knapsack, Subset Sum).
- If $P \neq NP$, no polynomial-time algorithm exists for any NP-Hard problem.

---

## 3. Combinatorial Scaling
For an input of size $N$, exhaustive search investigates $2^N$ candidate configurations.  
Even assuming modern hardware executing $10^7$ candidate verifications per second:
- $N = 30$: Takes $\approx 1.79$ minutes.
- $N = 40$: Takes $\approx 1.27$ days.
- $N = 50$: Takes $\approx 3.57$ years.
- $N = 60$: Takes $\approx 3,660$ years.

---

## 4. Execution Command
```bash
python exhaustive_search.py
```
