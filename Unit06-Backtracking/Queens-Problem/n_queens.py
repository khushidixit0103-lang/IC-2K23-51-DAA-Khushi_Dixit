"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 06: Backtracking
Experiment: N-Queens Problem (4-Queens, 8-Queens, and Scalable N-Queens)

Problem Statement:
Place N non-attacking queens on an N x N chessboard using Backtracking.
No two queens may share the same row, column, or diagonal.
Solves and visualizes 4-Queens, 8-Queens, and measures solution counts and
backtracking node expansions for arbitrary N.
"""

def is_safe(board, row, col):
    """
    Checks if a queen can be placed at board[row][col].
    Since queens are placed row by row, we only need to check:
    1. Upper column
    2. Upper-left diagonal
    3. Upper-right diagonal
    """
    for i in range(row):
        # Same column
        if board[i] == col:
            return False
        # Diagonals: |row_diff| == |col_diff|
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_n_queens(n):
    """
    Solves N-Queens using Backtracking.
    board[i] stores the column index of the queen in row i.
    
    Returns:
        tuple: (solutions, total_recursive_nodes)
    """
    solutions = []
    board = [-1] * n
    nodes_expanded = [0]
    
    def backtrack(row):
        nodes_expanded[0] += 1
        if row == n:
            solutions.append(list(board))
            return
            
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Reset/backtrack
                
    backtrack(0)
    return solutions, nodes_expanded[0]


def print_board(solution):
    n = len(solution)
    print("  +" + "---+" * n)
    for row in range(n):
        line = "  |"
        for col in range(n):
            if solution[row] == col:
                line += " Q |"
            else:
                line += " . |"
        print(line)
        print("  +" + "---+" * n)


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 6 - N-QUEENS PROBLEM (BACKTRACKING)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    # 1. 4-Queens Demonstration
    print("\n--- 1. 4-Queens Demonstration ---")
    sols_4, nodes_4 = solve_n_queens(4)
    print(f"Total Solutions for 4-Queens: {len(sols_4)}")
    print(f"Nodes Explored: {nodes_4} (vs 4^4 = 256 brute force)\n")
    for idx, sol in enumerate(sols_4, 1):
        print(f"Solution {idx} (Queen columns: {sol}):")
        print_board(sol)
        print()
        
    # 2. 8-Queens Demonstration
    print("--- 2. 8-Queens Demonstration ---")
    sols_8, nodes_8 = solve_n_queens(8)
    print(f"Total Valid Solutions for 8-Queens: {len(sols_8)}")
    print(f"State-Space Tree Nodes Explored: {nodes_8}")
    print(f"Theoretical Search Space without Pruning: 8^8 = 16,777,216 positions")
    print(f"Pruning Efficiency: {(1 - nodes_8 / (8**8)) * 100:.4f}% search space eliminated!\n")
    
    print("First Solution for 8-Queens (Queen columns):", sols_8[0])
    print_board(sols_8[0])
    
    # 3. Scalable N-Queens summary table
    print("\n--- 3. Scalable N-Queens Summary (N = 4 to 10) ---")
    print(f"{'N':<5} | {'Solutions Found':<18} | {'Nodes Explored':<16} | {'Brute Space (N^N)':<20}")
    print("-" * 65)
    for n in range(4, 11):
        sols, nodes = solve_n_queens(n)
        print(f"{n:<5} | {len(sols):<18} | {nodes:<16} | {n**n:<20}")
        
    print("=" * 70)


if __name__ == "__main__":
    main()
