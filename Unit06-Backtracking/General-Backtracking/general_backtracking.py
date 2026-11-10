"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 06: Backtracking
Experiment: General Backtracking Framework and State-Space Tree Exploration

Problem Statement:
Formalize and demonstrate the general Backtracking algorithmic template.
Explores the state-space tree via Depth-First Search with bounding/pruning functions
to eliminate infeasible subtrees early without full exhaustive enumeration.
"""

class BacktrackingTemplate:
    """
    General Backtracking Solver Template:
    - is_valid(state, choice): Bounding function (prunes invalid branches)
    - is_solution(state): Goal test
    - make_move(state, choice): State transition
    - undo_move(state, choice): Backtrack step
    """
    def __init__(self):
        self.nodes_explored = 0
        self.solutions = []

    def solve(self, initial_state):
        self.nodes_explored = 0
        self.solutions = []
        self._backtrack(initial_state, depth=0)
        return self.solutions, self.nodes_explored

    def _backtrack(self, state, depth):
        self.nodes_explored += 1
        
        if self.is_solution(state):
            self.solutions.append(self.format_solution(state))
            return
            
        for choice in self.get_candidates(state):
            if self.is_valid(state, choice):
                self.make_move(state, choice)
                self._backtrack(state, depth + 1)
                self.undo_move(state, choice)

    # Subclasses override these abstract methods:
    def is_solution(self, state):
        raise NotImplementedError
    def get_candidates(self, state):
        raise NotImplementedError
    def is_valid(self, state, choice):
        raise NotImplementedError
    def make_move(self, state, choice):
        raise NotImplementedError
    def undo_move(self, state, choice):
        raise NotImplementedError
    def format_solution(self, state):
        return list(state)


class ConstrainedPermutationGenerator(BacktrackingTemplate):
    """
    Concrete example: Generates permutations of numbers 1..N such that
    no two adjacent elements differ by exactly 1 (constrained state space).
    """
    def __init__(self, n):
        super().__init__()
        self.n = n

    def is_solution(self, state):
        return len(state) == self.n

    def get_candidates(self, state):
        used = set(state)
        return [x for x in range(1, self.n + 1) if x not in used]

    def is_valid(self, state, choice):
        # Bounding condition: no adjacent difference == 1
        if state and abs(state[-1] - choice) == 1:
            return False  # PRUNED!
        return True

    def make_move(self, state, choice):
        state.append(choice)

    def undo_move(self, state, choice):
        state.pop()


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 6 - GENERAL BACKTRACKING FRAMEWORK")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    n = 5
    solver = ConstrainedPermutationGenerator(n)
    solutions, nodes = solver.solve([])
    
    total_permutations = 1
    for i in range(1, n + 1):
        total_permutations *= i
        
    print(f"Problem: Permutations of (1..{n}) where |P[i] - P[i-1]| != 1")
    print(f"Total Theoretical Permutations without Pruning: {total_permutations}")
    print(f"Total State-Space Tree Nodes Explored with Backtracking: {nodes}")
    print(f"Valid Constrained Solutions Discovered: {len(solutions)}\n")
    
    print("Discovered Valid Sequences:")
    for idx, sol in enumerate(solutions, 1):
        print(f"  Solution {idx:2d}: {sol}")
        
    print("=" * 70)


if __name__ == "__main__":
    main()
