"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 05: Traversal and Search
Experiment: Breadth-First Search (BFS)

Problem Statement:
Traverse a graph level-by-level using a FIFO Queue to find the BFS visitation order,
level distances from a source node, and shortest path in an unweighted graph.
Time Complexity: O(V + E), Auxiliary Space: O(V).
"""

from collections import deque

def bfs(graph, num_vertices, start_node=0):
    """
    Executes Breadth-First Search starting from start_node.
    
    Parameters:
        graph: Adjacency list dict {u: [v1, v2, ...]}
        num_vertices (int): Total number of vertices
        start_node (int): Source vertex index
        
    Returns:
        tuple: (traversal_order, distances, parents)
    """
    visited = [False] * num_vertices
    dist = [-1] * num_vertices
    parent = [None] * num_vertices
    
    queue = deque([start_node])
    visited[start_node] = True
    dist[start_node] = 0
    
    traversal_order = []
    
    while queue:
        u = queue.popleft()
        traversal_order.append(u)
        
        for v in graph.get(u, []):
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                parent[v] = u
                queue.append(v)
                
    return traversal_order, dist, parent


def get_shortest_path(parent, target):
    """Traces parent pointers to reconstruct shortest unweighted path."""
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    return path


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 5 - BREADTH-FIRST SEARCH (BFS)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    node_names = ["A", "B", "C", "D", "E", "F", "G"]
    n = len(node_names)
    
    # 0:A, 1:B, 2:C, 3:D, 4:E, 5:F, 6:G
    graph = {
        0: [1, 2],       # A -> B, C
        1: [0, 3, 4],    # B -> A, D, E
        2: [0, 5],       # C -> A, F
        3: [1],          # D -> B
        4: [1, 5, 6],    # E -> B, F, G
        5: [2, 4],       # F -> C, E
        6: [4]           # G -> E
    }
    
    start_vertex = 0  # Node A
    print(f"Graph Vertices (|V|): {n} ({', '.join(node_names)})")
    print(f"Starting BFS from Source: {node_names[start_vertex]}\n")
    
    order, dist, parent = bfs(graph, n, start_vertex)
    
    print("--- BFS Traversal Sequence ---")
    order_str = " -> ".join(node_names[v] for v in order)
    print(f"  Order: {order_str}\n")
    
    print("--- Level Distances and Shortest Paths from Source ---")
    for v in range(n):
        path = get_shortest_path(parent, v)
        path_str = " -> ".join(node_names[node] for node in path)
        print(f"  Vertex {node_names[v]}: Distance = {dist[v]} hops | Shortest Path: {path_str}")
        
    print("=" * 70)


if __name__ == "__main__":
    main()
