# Sorting Algorithms Performance Comparison: Merge Sort vs Quick Sort vs Heap Sort

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 02:** Divide and Conquer  

---

## 1. Aim
To experimentally benchmark and compare the empirical execution times of three fundamental $O(n \log n)$ sorting algorithms—Merge Sort, Quick Sort, and Heap Sort—across varying input sizes ($N \in [500, 20000]$), validating their asymptotic growth curves and practical constant factor differences.

---

## 2. Theoretical Comparison

| Algorithm | Design Paradigm | Best Case | Average Case | Worst Case | Space Complexity | Stability |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Merge Sort** | Divide & Conquer | $\Omega(n \log n)$ | $\Theta(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes |
| **Quick Sort** | Divide & Conquer (Partition) | $\Omega(n \log n)$ | $\Theta(n \log n)$ | $O(n^2)$ | $O(\log n)$ stack | No |
| **Heap Sort** | Complete Binary Tree Max-Heap | $\Omega(n \log n)$ | $\Theta(n \log n)$ | $O(n \log n)$ | $O(1)$ | No |

---

## 3. Experimental Findings & Analysis
- **Cache Locality:** Quick Sort exhibits superior cache performance due to contiguous in-place scanning and swapping, routinely outperforming Merge Sort and Heap Sort on random arrays.
- **Auxiliary Memory:** Merge Sort requires $O(n)$ temporary buffer memory during the merge operation. Heap Sort operates strictly in-place ($O(1)$ additional space), making it memory-optimal.
- **Worst-Case Guarantees:** Merge Sort and Heap Sort guarantee strict $O(n \log n)$ time regardless of input distribution. Quick Sort with median pivot selection avoids quadratic degeneration on sorted inputs.

---

## 4. Generated Artifacts
- **Data CSV:** `results.csv` and `docs/performance-analysis/unit02_sorting_performance.csv`
- **Visualization Plot:** `sorting_performance.png` and `docs/performance-analysis/unit02_sorting_plot.png`

---

## 5. Execution Command
```bash
python sorting_performance_analysis.py
```
