# Performance Analysis: Iterative vs Recursive Binary Search

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 01:** Introduction to Algorithms and Performance Analysis  

---

## 1. Aim
To empirically benchmark and compare the execution-time performance of Iterative and Recursive Binary Search across varying problem sizes ($N \in [1000, 500000]$) under Best, Average, and Worst cases, recording output to CSV and plotting scaling curves.

---

## 2. Experimental Setup
- **Input Generation:** Arrays of sorted even integers $\langle 0, 2, 4, \dots, 2N-2 \rangle$.
- **Best Case Scenario:** Target element positioned at exact array midpoint `arr[N // 2]`.
- **Worst Case Scenario:** Target element is an odd number greater than the maximum element (`arr[-1] + 1`), forcing full tree traversal down to absent leaves ($\lfloor \log_2 N \rfloor + 1$ iterations/calls).
- **Average Case Scenario:** Uniform random selection of elements present within the array.
- **Trial Repetition:** 200 trials per measurement point using Python's high-resolution `time.perf_counter()` to obtain reliable microsecond ($\mu s$) averages.

---

## 3. Asymptotic vs Empirical Performance Comparison

| Case | Theoretical Time | Theoretical Space | Iterative Empirical Trend | Recursive Empirical Trend |
| :--- | :--- | :--- | :--- | :--- |
| **Best Case** | $\Omega(1)$ | $O(1)$ | $\approx 0.3 - 0.5\ \mu s$ | $\approx 0.4 - 0.7\ \mu s$ |
| **Average Case** | $\Theta(\log N)$ | $O(1)$ (Iter) / $O(\log N)$ (Rec) | Logarithmic scaling | Slightly higher slope due to frame allocation |
| **Worst Case** | $O(\log N)$ | $O(1)$ (Iter) / $O(\log N)$ (Rec) | strictly $\approx c_1 \cdot \log_2 N$ | $\approx c_2 \cdot \log_2 N$ where $c_2 > c_1$ |

---

## 4. Generated Artifacts
1. **Raw Benchmark Data:** `results.csv` and `docs/performance-analysis/unit01_binary_search_performance.csv`
2. **Visual Graphs:** `binary_search_performance.png` and `docs/performance-analysis/unit01_binary_search_plot.png`

---

## 5. Execution Command
```bash
python performance_analysis.py
```

---

## 6. Key Observations & Inferences
1. **Logarithmic Verification:** Both iterative and recursive algorithms show sub-linear, logarithmic scaling matching $O(\log n)$. Increasing $N$ from $1,000$ to $500,000$ ($500\times$ increase) increases execution time by only a factor of $\approx 1.8\times$ ($\log_2 500000 \approx 19$ vs $\log_2 1000 \approx 10$).
2. **Constant Factor Overhead:** The recursive version incurs approximately $30\% - 60\%$ higher constant-factor execution time than the iterative version due to call-stack activation record push/pop operations.
3. **Space Utilization:** Iterative binary search remains strictly $O(1)$ auxiliary space throughout execution, whereas recursive binary search consumes $O(\log n)$ stack frames.
