"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 03: Greedy Method
Experiment: Prim's Minimum Spanning Tree (MST)

Problem Statement:
Find the Minimum Spanning Tree (MST) of a connected, undirected, weighted graph
using Prim's Algorithm.
Greedy Choice: At each step, select the minimum-weight edge connecting any vertex
in the currently formed tree to any vertex outside the tree.
"""

import sys

def prims_mst(graph, num_vertices, start_vertex=0):
    """
    Computes MST using Prim's algorithm on an adjacency matrix.
    graph[u][v] = weight of edge between u and v, 0 indicates no edge.
    
    Returns:
        tuple: (mst_edges, total_cost)
    """
    INF = float("inf")
    
    # Key values used to pick minimum weight edge in cut
    key = [INF] * num_vertices
    # Array to store constructed MST: parent[v] = u
    parent = [None] * num_vertices
    # True if vertex is included in MST
    in_mst = [False] * num_vertices
    
    # Initialize start vertex
    key[start_vertex] = 0
    parent[start_vertex] = -1  # First node is always root of MST
    
    for _ in range(num_vertices):
        # Pick the minimum key vertex from the set of vertices not yet in MST
        min_key = INF
        u = -1
        for v in range(num_vertices):
            if not in_mst[v] and key[v] < min_key:
                min_key = key[v]
                u = v
                
        if u == -1:
            break
            
        in_mst[u] = True
        
        # Update key and parent of adjacent vertices of picked vertex
        for v in range(num_vertices):
            weight = graph[u][v]
            # weight > 0 means there is an edge
            if weight > 0 and not in_mst[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u
                
    # Collect MST edges and compute total cost
    mst_edges = []
    total_cost = 0
    for v in range(num_vertices):
        if parent[v] is not None and parent[v] != -1:
            u = parent[v]
            w = graph[u][v]
            mst_edges.append((u, v, w))
            total_cost += w
            
    return mst_edges, total_cost


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 3 - PRIM'S MINIMUM SPANNING TREE (MST)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    # Vertex names: 0: A, 1: B, 2: C, 3: D, 4: E, 5: F
    vertex_names = ["A", "B", "C", "D", "E", "F"]
    V = len(vertex_names)
    
    # Adjacency matrix for weighted undirected graph
    #      A   B   C   D   E   F
    graph = [
        [  0,  4,  2,  0,  0,  0 ],  # A
        [  4,  0,  1,  5,  0,  0 ],  # B
        [  2,  1,  0,  8, 10,  0 ],  # C
        [  0,  5,  8,  0,  2,  6 ],  # D
        [  0,  0, 10,  2,  0,  3 ],  # E
        [  0,  0,  0,  6,  3,  0 ]   # F
    ]
    
    print(f"Number of Vertices (|V|): {V}")
    print(f"Vertices: {', '.join(vertex_names)}\n")
    print("Graph Adjacency Matrix:")
    for i, row in enumerate(graph):
        print(f"  {vertex_names[i]}: {row}")
        
    mst_edges, total_cost = prims_mst(graph, V, start_vertex=0)
    
    print("\n--- Minimum Spanning Tree Edges Selected ---")
    for u, v, w in mst_edges:
        print(f"  Edge ({vertex_names[u]} - {vertex_names[v]}) with Weight: {w}")
        
    print("-" * 70)
    print(f"  Total Spanning Tree Edges : {len(mst_edges)} (|V| - 1 = {V - 1})")
    print(f"  Minimum Total Cost        : {total_cost}")
    print("=" * 70)


if __name__ == "__main__":
    main()
