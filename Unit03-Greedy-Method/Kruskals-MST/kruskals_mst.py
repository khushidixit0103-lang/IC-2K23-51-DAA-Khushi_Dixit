"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 03: Greedy Method
Experiment: Kruskal's Minimum Spanning Tree (MST)

Problem Statement:
Find the Minimum Spanning Tree (MST) of a connected, undirected, weighted graph
using Kruskal's Algorithm with Disjoint Set Union (DSU / Union-Find).
Greedy Choice: Sort all edges globally in ascending order of weight. Greedily pick
edges that do not form a cycle until |V| - 1 edges are included.
"""

class DisjointSetUnion:
    """Disjoint Set Union with Path Compression and Union by Rank."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False  # Already in same connected component (cycle detected)


def kruskals_mst(num_vertices, edges):
    """
    Computes MST using Kruskal's algorithm.
    edges: list of tuples (u, v, weight)
    
    Returns:
        tuple: (mst_edges, total_cost)
    """
    # 1. Sort all edges in non-decreasing order of weight
    sorted_edges = sorted(edges, key=lambda e: e[2])
    
    dsu = DisjointSetUnion(num_vertices)
    mst_edges = []
    total_cost = 0
    
    for u, v, w in sorted_edges:
        # Check if adding edge creates a cycle
        if dsu.union(u, v):
            mst_edges.append((u, v, w))
            total_cost += w
            if len(mst_edges) == num_vertices - 1:
                break
                
    return mst_edges, total_cost


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 3 - KRUSKAL'S MINIMUM SPANNING TREE (MST)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    vertex_names = ["A", "B", "C", "D", "E", "F"]
    V = len(vertex_names)
    
    # Graph edges corresponding to the same graph tested in Prim's experiment
    # (u, v, weight)
    edges = [
        (0, 1, 4),   # A - B : 4
        (0, 2, 2),   # A - C : 2
        (1, 2, 1),   # B - C : 1
        (1, 3, 5),   # B - D : 5
        (2, 3, 8),   # C - D : 8
        (2, 4, 10),  # C - E : 10
        (3, 4, 2),   # D - E : 2
        (3, 5, 6),   # D - F : 6
        (4, 5, 3)    # E - F : 3
    ]
    
    print(f"Number of Vertices (|V|) : {V}")
    print(f"Total Edges (|E|)        : {len(edges)}")
    print(f"Vertices: {', '.join(vertex_names)}\n")
    print("Edge List (u, v, weight):")
    for u, v, w in edges:
        print(f"  ({vertex_names[u]} - {vertex_names[v]}) : {w}")
        
    mst_edges, total_cost = kruskals_mst(V, edges)
    
    print("\n--- Kruskal's Edge Inclusion Sequence ---")
    for step, (u, v, w) in enumerate(mst_edges, 1):
        print(f"  Step {step}: Accepted Edge ({vertex_names[u]} - {vertex_names[v]}) with Weight {w}")
        
    print("-" * 70)
    print(f"  Total Edges in MST   : {len(mst_edges)} (|V| - 1 = {V - 1})")
    print(f"  Total MST Cost       : {total_cost}")
    print("=" * 70)


if __name__ == "__main__":
    main()
