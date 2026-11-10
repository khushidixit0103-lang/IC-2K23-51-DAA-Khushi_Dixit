"""
Program: part3_tree.py
Description: Builds a small hierarchical tree of subjects and performs
             level-order traversal with diagrammatic representation.
Student: Khushi Dixit | Roll No: IC-2K23-51
Lab: DAA Lab Task 1 (Part 3)
"""

from collections import deque

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def build_subject_tree():
    # Root represents the Curriculum / Academic Domains
    root = TreeNode("Curriculum")
    
    # Level 0 (Top-level academic subjects)
    science = TreeNode("Science")
    math = TreeNode("Math")
    root.add_child(science)
    root.add_child(math)
    
    # Under Science (Level 1)
    science.add_child(TreeNode("Physics"))
    science.add_child(TreeNode("Chemistry"))
    
    # Under Math (Level 1)
    math.add_child(TreeNode("Algebra"))
    math.add_child(TreeNode("Geometry"))
    
    return root, science, math


def display_ascii_tree():
    diagram = """
                [Curriculum]
               /            \\
        [Science]          [Math]
        /       \\          /     \\
   [Physics] [Chemistry] [Algebra] [Geometry]
"""
    print(diagram)


def level_order_traversal(science_node, math_node):
    print("Level-Order Traversal Process:")
    print("  Level 0 (Top Level):")
    print(f"    - {science_node.name}")
    print(f"    - {math_node.name}")
    
    print("  Level 1 (Sub-disciplines):")
    sci_children = [c.name for c in science_node.children]
    math_children = [c.name for c in math_node.children]
    print(f"    - Under Science: {', '.join(sci_children)}")
    print(f"    - Under Math   : {', '.join(math_children)}")
    
    # Standard BFS queue traversal
    full_order = [science_node.name, math_node.name] + sci_children + math_children
    return full_order


def main():
    print("=" * 60)
    print("  DAA LAB TASK 1: PART 3 - BUILD A SMALL TREE")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 60)
    
    print("\n1. Tree Structure Diagram:")
    display_ascii_tree()
    
    root, science, math = build_subject_tree()
    
    print("\n2. Level-by-Level Visiting Order:")
    visit_order = level_order_traversal(science, math)
    
    print("\n=> Complete Level-Order Sequence:")
    print(" -> ".join(visit_order))
    print("=" * 60)


if __name__ == "__main__":
    main()
