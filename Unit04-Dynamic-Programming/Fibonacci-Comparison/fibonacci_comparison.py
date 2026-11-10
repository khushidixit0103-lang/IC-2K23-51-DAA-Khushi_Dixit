"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 04: Dynamic Programming
Experiment: Fibonacci Comparison (Naive Recursion vs Memoization vs Tabulation)

Problem Statement:
Compute the N-th Fibonacci number using three distinct paradigms:
1. Naive Divide-and-Conquer Recursion: O(2^n) time, redundant subproblems.
2. Memoization (Top-Down Dynamic Programming): O(n) time, caches overlapping subproblems.
3. Tabulation (Bottom-Up Dynamic Programming): O(n) time, O(1) space optimization.
"""

import time
import sys

def fib_recursive(n, call_count):
    """Naive exponential recursive approach."""
    call_count[0] += 1
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1, call_count) + fib_recursive(n - 2, call_count)


def fib_memoized(n, memo=None, call_count=None):
    """Top-down DP with memoization dictionary."""
    if call_count is not None:
        call_count[0] += 1
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fib_memoized(n - 1, memo, call_count) + fib_memoized(n - 2, memo, call_count)
    return memo[n]


def fib_tabulation(n):
    """Bottom-up DP with constant auxiliary space."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    prev2 = 0
    prev1 = 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1


def main():
    print("=" * 75)
    print("  IC-709 B: UNIT 4 - FIBONACCI (RECURSION VS MEMOIZATION VS TABULATION)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 75)
    
    test_values = [5, 10, 20, 30, 35]
    
    print(f"{'N':<5} | {'Fib(N)':<12} | {'Naive Rec Calls':<18} | {'Naive Time (ms)':<16} | {'Memo Calls':<12} | {'Memo Time (ms)':<15}")
    print("-" * 80)
    
    for n in test_values:
        # 1. Naive recursive
        c_rec = [0]
        t0 = time.perf_counter()
        val_rec = fib_recursive(n, c_rec)
        t_rec = (time.perf_counter() - t0) * 1000.0
        
        # 2. Memoized DP
        c_memo = [0]
        t0 = time.perf_counter()
        val_memo = fib_memoized(n, {}, c_memo)
        t_memo = (time.perf_counter() - t0) * 1000.0
        
        # 3. Tabulation
        val_tab = fib_tabulation(n)
        
        assert val_rec == val_memo == val_tab, "Value mismatch!"
        
        print(f"{n:<5} | {val_rec:<12} | {c_rec[0]:<18} | {t_rec:<16.3f} | {c_memo[0]:<12} | {t_memo:<15.4f}")
        
    print("-" * 80)
    print("\nDemonstrating Large N with Bottom-Up Dynamic Programming (Tabulation):")
    for large_n in [50, 100, 200]:
        t0 = time.perf_counter()
        ans = fib_tabulation(large_n)
        dt = (time.perf_counter() - t0) * 1000.0
        print(f"  Fib({large_n}) = {ans} (Calculated in {dt:.4f} ms)")
        
    print("=" * 75)


if __name__ == "__main__":
    main()
