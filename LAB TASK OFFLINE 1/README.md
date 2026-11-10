# Lab Task 1 (Offline Lab 1)

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course:** Design and Analysis of Algorithms Lab (IC-709 B)  

---

## Part 1. Trace It Yourself

### Problem Statement
Given list: `[8, 3, 15, 6, 2]`
1. Find the largest number by checking one number at a time. Record how many comparisons are made.
2. Sort this list from smallest to largest using any method. Record the step-by-step trace.

### Input
- `[8, 3, 15, 6, 2]`

### Output
- Largest number: `15`
- Total comparisons made: `4`
- Sorted array: `[2, 3, 6, 8, 15]`

### Comparisons Made
Total comparisons: **4** (for an array of $n = 5$ elements, comparing indices 1 through 4 with current maximum).

### Dry Run
- Initialize: `max = A[0] = 8`, `comparisons = 0`
- `i = 1, A[i] = 3`: `3 > 8` is False, `max = 8`, `comparisons = 1`
- `i = 2, A[i] = 15`: `15 > 8` is True, `max = 15`, `comparisons = 2`
- `i = 3, A[i] = 6`: `6 > 15` is False, `max = 15`, `comparisons = 3`
- `i = 4, A[i] = 2`: `2 > 15` is False, `max = 15`, `comparisons = 4`

### Sorting Method Used
- **Bubble Sort (Exchange Sort)**

### Sorting Steps
- Initial Array: `[8, 3, 15, 6, 2]`
- Pass 1:
  - Compare 8 and 3 -> Swap -> `[3, 8, 15, 6, 2]`
  - Compare 8 and 15 -> No swap -> `[3, 8, 15, 6, 2]`
  - Compare 15 and 6 -> Swap -> `[3, 8, 6, 15, 2]`
  - Compare 15 and 2 -> Swap -> `[3, 8, 6, 2, 15]`
- Pass 2:
  - Compare 3 and 8 -> No swap -> `[3, 8, 6, 2, 15]`
  - Compare 8 and 6 -> Swap -> `[3, 6, 8, 2, 15]`
  - Compare 8 and 2 -> Swap -> `[3, 6, 2, 8, 15]`
- Pass 3:
  - Compare 3 and 6 -> No swap -> `[3, 6, 2, 8, 15]`
  - Compare 6 and 2 -> Swap -> `[3, 2, 6, 8, 15]`
- Pass 4:
  - Compare 3 and 2 -> Swap -> `[2, 3, 6, 8, 15]`
- Final Sorted Array: `[2, 3, 6, 8, 15]`

### Explanation
The linear scan checks each element sequentially starting from the second element against the current maximum candidate. Every element must be inspected at least once because any uninspected position could potentially contain a strictly larger value.

---

## Part 2. Stack or Queue

### Problem Statement
Tasks arriving one after another: `Task1, Task2, Task3, Task4, Task5`.
1. Order if served using a Stack.
2. Order if served using a Queue.
3. Order for a shared printer.

### Stack Order (LIFO)
`Task5 -> Task4 -> Task3 -> Task2 -> Task1`

### Queue Order (FIFO)
`Task1 -> Task2 -> Task3 -> Task4 -> Task5`

### Printer Should Use
**Queue (FIFO)**

### Reason
A printer requires First-Come, First-Served (FCFS) processing to ensure fairness among multi-user print jobs. The earliest submitted document must be printed first, preventing newer print jobs from indefinitely starving older requests.

### Dry Run
- **Stack (LIFO):** Push `Task1`, `Task2`, `Task3`, `Task4`, `Task5`. Popping removes the most recent element first: `Task5`, then `Task4`, `Task3`, `Task2`, `Task1`.
- **Queue (FIFO):** Enqueue `Task1`, `Task2`, `Task3`, `Task4`, `Task5`. Dequeuing removes from front: `Task1`, then `Task2`, `Task3`, `Task4`, `Task5`.

### Explanation
A printer is an asynchronous shared resource where starvation must be prevented. A Queue enforces First-In, First-Out (FIFO) ordering by operating strictly from opposite ends (enqueue at rear, dequeue from front), which mathematically guarantees arrival-order fairness.

---

## Part 3. Build a Small Tree

### Tree Diagram
```
                [Curriculum]
               /            \\
        [Science]          [Math]
        /       \\          /     \\
   [Physics] [Chemistry] [Algebra] [Geometry]
```

### Dry Run
- **Level 0 (Top Level):** Science, Math
- **Level 1 under Science:** Physics, Chemistry
- **Level 1 under Math:** Algebra, Geometry

### Level Order Traversal Sequence
`Science -> Math -> Physics -> Chemistry -> Algebra -> Geometry`

### Explanation
Level-order traversal performs Breadth-First Search (BFS) across the hierarchical tree. It visits all immediate children of the root (depth 0) before advancing downward to visit grandchildren (depth 1), using a FIFO queue to systematically explore siblings at the same depth first.

---

## Part 4. Count the Steps & Complexity Analysis

### Single Loop Runs
- For loop $i = 1$ to $5$: **5 times**
- For $n = 20$: **20 times**

### Nested Loop Total Prints
- For $i = 1$ to $5$ and $j = 1$ to $5$: **25 times** ($5 \times 5$)
- For $n = 10$: **100 times** ($10 \times 10$)

### Dry Run
- **Single loop:** $i = 1, 2, 3, 4, 5 \implies$ runs 5 times.
- **Nested loop:** for each $i \in \{1..5\}$, inner loop runs 5 times $\implies 5 \times 5 = 25$ total prints.
- **For $n = 10$:** Single loop runs 10 times; Nested loop runs $10 \times 10 = 100$ times.

### Explanation & Growth Rate
- **Single Loop ($O(n)$):** Effort grows linearly. If input size $n$ grows 100 times (e.g. from 10 to 1,000), total operations increase **proportionally** (by exactly 100 times).
- **Nested Loop ($O(n^2)$):** Effort grows quadratically. If input size $n$ grows 100 times, total operations grow **explosively** ($100^2 = 10,000$ times), because every outer step triggers a complete inner scan.

---

## Acceptance Criteria Verification
1. **Inputs:** Specified lists, arrival sequences, hierarchical subject groupings, loop upper bounds ($n$).
2. **Outputs:** Monitored comparisons, sorted states, FIFO/LIFO orders, BFS traversals, exact iteration counts.
3. **Data Structures:** Python dynamic lists, `collections.deque` for FIFO queue, LIFO stack, and Linked Tree Nodes (`TreeNode`).

---

## How to Run
```bash
python part1_trace.py
python part2_stack_queue.py
python part3_tree.py
python part4_complexity.py
```
