# Iterative Binary Search

**Course:** IC-709 B: Design and Analysis of Algorithms Lab  
**Student:** Khushi Dixit (Roll No: IC-2K23-51)  
**Unit 01:** Introduction to Algorithms and Performance Analysis  

---

## 1. Aim
To design, implement, and analyze the Iterative Binary Search algorithm on a sorted list of elements and verify its best, average, and worst-case time complexities.

---

## 2. Problem Statement
Given an array `arr` of $n$ elements sorted in non-decreasing order and a target value `key`, determine the position (index) of `key` within `arr` using an iterative search strategy that halves the search space at each iteration. If `key` is absent, return an indicator value `-1`.

---

## 3. Algorithm
1. Initialize two pointers: `low = 0` and `high = n - 1`.
2. While `low <= high`:
   a. Compute the middle index: `mid = low + (high - low) // 2`.
   b. If `arr[mid] == key`, return `mid` (key found).
   c. If `arr[mid] < key`, set `low = mid + 1` (search right half).
   d. If `arr[mid] > key`, set `high = mid - 1` (search left half).
3. If `low > high`, return `-1` (key not found).

---

## 4. Pseudocode
```text
Algorithm BINARY_SEARCH_ITERATIVE(arr, n, key):
    low <- 0
    high <- n - 1
    while low <= high do:
        mid <- low + (high - low) / 2
        if arr[mid] == key then:
            return mid
        else if arr[mid] < key then:
            low <- mid + 1
        else:
            high <- mid - 1
    end while
    return -1
```

---

## 5. Complexity Analysis

| Case | Condition | Time Complexity | Comparisons |
| :--- | :--- | :--- | :--- |
| **Best Case** | Target matches middle element on first iteration | $\Omega(1)$ | 1 |
| **Average Case** | Target found at some intermediate tree depth | $\Theta(\log n)$ | $\approx \log_2 n$ |
| **Worst Case** | Target at leaves or absent from array | $O(\log n)$ | $\lfloor \log_2 n \rfloor + 1$ |
| **Space Complexity** | Iterative implementation uses $O(1)$ auxiliary space | $O(1)$ | Constant variables |

---

## 6. Sample Input & Output
- **Array:** `[10, 23, 35, 42, 56, 68, 71, 85, 92, 99]` ($n = 10$)
- **Best Case Key:** `56` -> Found at index `4` in `1` comparison.
- **Average Case Key:** `23` -> Found at index `1` in `2` comparisons.
- **Worst Case Key:** `99` -> Found at index `9` in `4` comparisons.
- **Absent Key:** `50` -> Not found (`-1`) in `4` comparisons.

---

## 7. Execution Command
```bash
python binary_search_iterative.py
```

---

## 8. Results & Learning Outcomes
- Successfully implemented iterative binary search with loop boundaries and pointer updates.
- Verified that space complexity is strictly $O(1)$, avoiding call-stack overhead.
- Confirmed logarithmic scaling in comparison count as array size increases.
