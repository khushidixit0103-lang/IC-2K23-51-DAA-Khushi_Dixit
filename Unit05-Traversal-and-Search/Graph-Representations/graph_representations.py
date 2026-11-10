"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 05: Traversal and Search
Experiment: Graph Representations (Adjacency Matrix vs Adjacency List)

Problem Statement:
Implement and contrast the two principal computer graph representations:
1. Adjacency Matrix: V x V table offering O(1) edge existence queries, but O(V^2) space.
2. Adjacency List: Array of linked collections using O(V + E) space, optimal for sparse topologies.
"""

import sys

class GraphAdjMatrix:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, weight=1, directed=False):
        self.matrix[u][v] = weight
        if not directed:
            self.matrix[v][u] = weight

    def has_edge(self, u, v):
        return self.matrix[u][v] != 0

    def get_neighbors(self, u):
        return [v for v in range(self.V) if self.matrix[u][v] != 0]

    def display(self, node_labels=None):
        print("Adjacency Matrix:")
        for i in range(self.V):
            name = node_labels[i] if node_labels else str(i)
            print(f"  {name}: {self.matrix[i]}")


class GraphAdjList:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.adj = {i: [] for i in range(num_vertices)}

    def add_edge(self, u, v, weight=1, directed=False):
        self.adj[u].append((v, weight))
        if not directed:
            self.adj[v].append((u, weight))

    def has_edge(self, u, v):
        return any(neighbor == v for neighbor, _ in self.adj[u])

    def get_neighbors(self, u):
        return [neighbor for neighbor, _ in self.adj[u]]

    def display(self, node_labels=None):
        print("Adjacency List:")
        for i in range(self.V):
            name = node_labels[i] if node_labels else str(i)
            targets = [f"({node_labels[v] if node_labels else v}, w={w})" for v, w in self.adj[i]]
            print(f"  {name} -> [{', '.join(targets)}]")


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 5 - GRAPH REPRESENTATIONS (MATRIX VS LIST)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    nodes = ["A", "B", "C", "D", "E"]
    n = len(nodes)
    
    # Edges: (0-A, 1-B, 2-C, 3-D, 4-E)
    edges = [
        (0, 1, 4),  # A - B
        (0, 2, 2),  # A - C
        (1, 3, 5),  # B - D
        (2, 3, 1),  # C - D
        (3, 4, 3)   # D - E
    ]
    
    g_mat = GraphAdjMatrix(n)
    g_list = GraphAdjList(n)
    
    for u, v, w in edges:
        g_mat.add_edge(u, v, w)
        g_list.add_edge(u, v, w)
        
    print(f"Graph Order |V| = {n}, Size |E| = {len(edges)}\n")
    g_mat.display(nodes)
    print()
    g_list.display(nodes)
    
    print("\n--- Operation Comparisons ---")
    test_queries = [(0, 1), (0, 3), (2, 3), (1, 4)]
    for u, v in test_queries:
        m_has = g_mat.has_edge(u, v)
        l_has = g_list.has_edge(u, v)
        print(f"  Edge ({nodes[u]} - {nodes[v]}): Matrix -> {m_has} | List -> {l_has}")
        
    print("\n--- Neighbor Traversal ---")
    for u in range(n):
        n_m = [nodes[v] for v in g_mat.get_neighbors(u)]
        n_l = [nodes[v] for v in g_list.get_neighbors(u)]
        print(f"  Neighbors of {nodes[u]}: Matrix -> {n_m} | List -> {n_l}")
        
    print("=" * 70)


if __name__ == "__main__":
    main()
