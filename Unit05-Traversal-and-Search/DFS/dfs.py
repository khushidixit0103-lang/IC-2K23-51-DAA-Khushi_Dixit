"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 05: Traversal and Search
Experiment: Depth-First Search (DFS) (Recursive & Iterative with Timestamps)

Problem Statement:
Perform Depth-First Search on a graph using:
1. Recursive formulation with discovery and finishing timestamps (CLRS convention).
2. Iterative formulation using an explicit LIFO Stack.
Detects back edges (cycles) and tracks graph component connectivity.
"""

def dfs_recursive(graph, num_vertices):
    """
    Executes full DFS covering all components with discovery/finish timestamps.
    """
    color = ["WHITE"] * num_vertices  # WHITE=unvisited, GRAY=in-progress, BLACK=finished
    discovery = [-1] * num_vertices
    finish = [-1] * num_vertices
    parent = [None] * num_vertices
    time = [0]
    traversal_order = []
    has_cycle = [False]
    
    def dfs_visit(u):
        color[u] = "GRAY"
        time[0] += 1
        discovery[u] = time[0]
        traversal_order.append(u)
        
        for v in graph.get(u, []):
            if color[v] == "WHITE":
                parent[v] = u
                dfs_visit(v)
            elif color[v] == "GRAY" and parent[u] != v:
                has_cycle[0] = True  # Back edge detected in undirected graph
                
        color[u] = "BLACK"
        time[0] += 1
        finish[u] = time[0]
        
    for u in range(num_vertices):
        if color[u] == "WHITE":
            dfs_visit(u)
            
    return traversal_order, discovery, finish, has_cycle[0]


def dfs_iterative(graph, num_vertices, start_node=0):
    """
    Executes iterative DFS from a designated source using an explicit stack.
    """
    visited = [False] * num_vertices
    traversal_order = []
    stack = [start_node]
    
    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            traversal_order.append(u)
            # Push neighbors in reverse order to explore lowest indices first
            for v in reversed(graph.get(u, [])):
                if not visited[v]:
                    stack.append(v)
                    
    return traversal_order


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 5 - DEPTH-FIRST SEARCH (DFS)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    node_names = ["A", "B", "C", "D", "E", "F"]
    n = len(node_names)
    
    # Graph edges:
    # 0: A, 1: B, 2: C, 3: D, 4: E, 5: F
    graph = {
        0: [1, 2],       # A -> B, C
        1: [0, 3, 4],    # B -> A, D, E
        2: [0, 4],       # C -> A, E
        3: [1, 5],       # D -> B, F
        4: [1, 2, 5],    # E -> B, C, F
        5: [3, 4]        # F -> D, E
    }
    
    print(f"Graph Vertices (|V|): {n} ({', '.join(node_names)})\n")
    
    order_rec, disc, fin, cycle = dfs_recursive(graph, n)
    order_iter = dfs_iterative(graph, n, start_node=0)
    
    print("--- DFS Traversal Sequences ---")
    rec_str = " -> ".join(node_names[v] for v in order_rec)
    iter_str = " -> ".join(node_names[v] for v in order_iter)
    print(f"  Recursive Order : {rec_str}")
    print(f"  Iterative Order : {iter_str}\n")
    
    print("--- Discovery and Finishing Timestamps (Parenthesis Theorem) ---")
    for v in range(n):
        print(f"  Vertex {node_names[v]}: Discovered d[{node_names[v]}] = {disc[v]:2d} | Finished f[{node_names[v]}] = {fin[v]:2d} | Interval: [{disc[v]}/{fin[v]}]")
        
    print(f"\nCycle Detected (Back Edges): {'YES' if cycle else 'NO'}")
    print("=" * 70)


if __name__ == "__main__":
    main()
