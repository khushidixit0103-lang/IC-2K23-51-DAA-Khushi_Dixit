"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 05: Traversal and Search
Experiment: Binary Tree Creation and Traversals (Recursive & Iterative)

Problem Statement:
Construct a Binary Tree and implement all three standard depth traversals:
1. Pre-order Traversal (Root, Left, Right)
2. In-order Traversal (Left, Root, Right)
3. Post-order Traversal (Left, Right, Root)
Provides both Recursive (function call-stack) and Iterative (explicit user stack) implementations.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# --- Recursive Implementations ---
def preorder_recursive(root, res=None):
    if res is None:
        res = []
    if root:
        res.append(root.val)
        preorder_recursive(root.left, res)
        preorder_recursive(root.right, res)
    return res

def inorder_recursive(root, res=None):
    if res is None:
        res = []
    if root:
        inorder_recursive(root.left, res)
        res.append(root.val)
        inorder_recursive(root.right, res)
    return res

def postorder_recursive(root, res=None):
    if res is None:
        res = []
    if root:
        postorder_recursive(root.left, res)
        postorder_recursive(root.right, res)
        res.append(root.val)
    return res

# --- Iterative Implementations ---
def preorder_iterative(root):
    if not root:
        return []
    res = []
    stack = [root]
    while stack:
        curr = stack.pop()
        res.append(curr.val)
        # Push right first so that left is popped and processed first
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return res

def inorder_iterative(root):
    res = []
    stack = []
    curr = root
    while curr or stack:
        # Traverse left subtree down to deepest leaf
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res

def postorder_iterative(root):
    if not root:
        return []
    res = []
    stack1 = [root]
    stack2 = []
    # Using 2-stack approach for clean iterative postorder
    while stack1:
        curr = stack1.pop()
        stack2.append(curr)
        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)
    while stack2:
        res.append(stack2.pop().val)
    return res


def build_sample_tree():
    """
    Constructs sample binary tree:
             1
           /   \\
          2     3
         / \\   / \\
        4   5 6   7
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 5 - BINARY TREE TRAVERSALS (RECURSIVE & ITERATIVE)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    root = build_sample_tree()
    print("Sample Binary Tree Architecture:")
    print("            [1]")
    print("          /     \\")
    print("       [2]       [3]")
    print("      /   \\     /   \\")
    print("    [4]   [5] [6]   [7]\n")
    
    # 1. Pre-order
    pre_rec = preorder_recursive(root)
    pre_iter = preorder_iterative(root)
    print(f"Pre-order Traversal (Root -> Left -> Right):")
    print(f"  Recursive : {pre_rec}")
    print(f"  Iterative : {pre_iter}")
    print(f"  Matches   : {'PASSED' if pre_rec == pre_iter else 'FAILED'}\n")
    
    # 2. In-order
    in_rec = inorder_recursive(root)
    in_iter = inorder_iterative(root)
    print(f"In-order Traversal (Left -> Root -> Right):")
    print(f"  Recursive : {in_rec}")
    print(f"  Iterative : {in_iter}")
    print(f"  Matches   : {'PASSED' if in_rec == in_iter else 'FAILED'}\n")
    
    # 3. Post-order
    post_rec = postorder_recursive(root)
    post_iter = postorder_iterative(root)
    print(f"Post-order Traversal (Left -> Right -> Root):")
    print(f"  Recursive : {post_rec}")
    print(f"  Iterative : {post_iter}")
    print(f"  Matches   : {'PASSED' if post_rec == post_iter else 'FAILED'}")
    
    print("=" * 70)


if __name__ == "__main__":
    main()
