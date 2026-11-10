"""
Program: part4_complexity.py
Description: Counts loop execution steps for single and nested loops,
             demonstrating linear O(n) and quadratic O(n^2) complexity growth.
Student: Khushi Dixit | Roll No: IC-2K23-51
Lab: DAA Lab Task 1 (Part 4)
"""

def count_single_loop(n):
    count = 0
    print(f"\n--- Single Loop Execution (1 to {n}) ---")
    for i in range(1, n + 1):
        count += 1
        if n <= 10 or i <= 5 or i == n:
            print(f"  Step {i}: i = {i}")
        elif i == 6:
            print("  ... [steps omitted for brevity] ...")
    return count


def count_nested_loop(n):
    count = 0
    print(f"\n--- Nested Loop Execution (i=1..{n}, j=1..{n}) ---")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            count += 1
            if n <= 5:
                print(f"  Print step {count}: (i={i}, j={j})")
            elif count <= 5 or count == n * n:
                print(f"  Print step {count}: (i={i}, j={j})")
            elif count == 6:
                print("  ... [nested steps omitted for brevity] ...")
    return count


def main():
    print("=" * 65)
    print("  DAA LAB TASK 1: PART 4 - COUNT THE STEPS & COMPLEXITY ANALYSIS")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)
    
    # 1. Single loop i = 1 to 5
    print("\n[Case 1: Single Loop with n = 5]")
    c1 = count_single_loop(5)
    print(f"Total iterations (n=5): {c1}")
    
    # 2. Single loop with n = 20
    print("\n[Case 2: Single Loop with n = 20]")
    c2 = count_single_loop(20)
    print(f"Total iterations (n=20): {c2}")
    
    # 3. Nested loop i = 1 to 5, j = 1 to 5
    print("\n[Case 3: Nested Loop with n = 5]")
    c3 = count_nested_loop(5)
    print(f"Total PRINT executions (5 x 5): {c3}")
    
    # 4. Nested loop with n = 10
    print("\n[Case 4: Nested Loop with n = 10]")
    c4 = count_nested_loop(10)
    print(f"Total PRINT executions (10 x 10): {c4}")
    
    # Theoretical growth comparison
    print("\n" + "=" * 65)
    print("GROWTH ANALYSIS (If input size n grew 100 times):")
    print("-" * 65)
    print("1. Single Loop: O(n) Linear Growth")
    print("   - If n increases by 100x (e.g., from 10 to 1,000),")
    print("     the number of operations grows PROPORTIONALLY (exactly 100 times).")
    print("\n2. Nested Loop: O(n^2) Quadratic Growth")
    print("   - If n increases by 100x,")
    print("     the number of operations grows EXPLOSIVELY (100^2 = 10,000 times!).")
    print("=" * 65)


if __name__ == "__main__":
    main()
