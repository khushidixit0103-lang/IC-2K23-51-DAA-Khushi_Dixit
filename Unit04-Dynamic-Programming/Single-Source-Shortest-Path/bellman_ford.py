"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 04: Dynamic Programming
Experiment: Single-Source Shortest Path (Bellman-Ford Algorithm)

Problem Statement:
Find shortest path distances from a single source vertex to all other vertices
in a directed weighted graph that may contain negative edge weights.
Dynamic Programming Principle:
Relax all edges |V| - 1 times. If any edge can be further relaxed on the |V|-th pass,
a negative-weight cycle reachable from the source is detected.
"""

def bellman_ford(vertices, edges, source):
    """
    Computes single-source shortest paths using the Bellman-Ford DP approach.
    
    Parameters:
        vertices (list): List of vertex identifiers.
        edges (list): List of tuples (u, v, weight).
        source: Source vertex identifier.
        
    Returns:
        tuple: (dist, parent, has_negative_cycle)
    """
    INF = float("inf")
    dist = {v: INF for v in vertices}
    parent = {v: None for v in vertices}
    dist[source] = 0
    
    num_vertices = len(vertices)
    
    # Relax all edges |V| - 1 times
    for iteration in range(1, num_vertices):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        # Early termination if no relaxation occurred in current round
        if not updated:
            break
            
    # Check for negative-weight cycles (|V|-th relaxation pass)
    has_negative_cycle = False
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            has_negative_cycle = True
            break
            
    return dist, parent, has_negative_cycle


def get_path(parent, target):
    """Reconstructs path from source to target."""
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    return path


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 4 - BELLMAN-FORD (SINGLE-SOURCE SHORTEST PATH)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    vertices = ["S", "A", "B", "C", "D", "E"]
    
    # Directed weighted edges (u, v, weight)
    edges = [
        ("S", "A", 10),
        ("S", "E", 8),
        ("A", "C", 2),
        ("B", "A", 1),
        ("C", "B", -2),
        ("D", "A", -4),
        ("D", "C", -1),
        ("E", "D", 1)
    ]
    
    source = "S"
    print(f"Source Vertex: {source}")
    print(f"Total Vertices (|V|): {len(vertices)}")
    print(f"Total Edges (|E|)   : {len(edges)}\n")
    print("Edge List (u -> v, weight):")
    for u, v, w in edges:
        print(f"  {u} -> {v} : {w}")
        
    dist, parent, has_cycle = bellman_ford(vertices, edges, source)
    
    print("\nNegative Cycle Detected:", "YES" if has_cycle else "NO")
    
    print("\n--- Shortest Distance and Path from Source (S) ---")
    for v in vertices:
        if dist[v] != float("inf"):
            path = get_path(parent, v)
            path_str = " -> ".join(path)
            print(f"  To Vertex {v:<2} | Min Distance: {dist[v]:<4} | Path: {path_str}")
        else:
            print(f"  To Vertex {v:<2} | Min Distance: INF  | Path: Unreachable")
            
    print("=" * 70)


if __name__ == "__main__":
    main()
