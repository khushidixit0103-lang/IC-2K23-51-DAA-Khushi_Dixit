"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 04: Dynamic Programming
Experiment: All-Pairs Shortest Path (Floyd-Warshall Algorithm)

Problem Statement:
Find shortest path distances between every pair of vertices in a directed weighted graph
(permitting negative edge weights, but no negative weight cycles).
Dynamic Programming Recurrence:
    D^(k)[i][j] = min( D^(k-1)[i][j], D^(k-1)[i][k] + D^(k-1)[k][j] )
Tracks predecessors to reconstruct exact path between any source-destination pair.
"""

def floyd_warshall(graph, num_vertices):
    """
    Computes all-pairs shortest paths using Floyd-Warshall DP.
    
    Parameters:
        graph: 2D adjacency matrix where graph[i][j] is edge weight (INF if no edge, 0 if i==j)
        num_vertices (int): Number of nodes |V|
        
    Returns:
        tuple: (dist, pred, has_negative_cycle)
    """
    INF = float("inf")
    n = num_vertices
    
    # Initialize distance and predecessor matrices
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    pred = [[None if (i == j or graph[i][j] == INF) else i for j in range(n)] for i in range(n)]
    
    # 3 nested loops: k is the intermediate vertex
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        pred[i][j] = pred[k][j]
                        
    # Check for negative weight cycles (any negative value on main diagonal)
    has_negative_cycle = False
    for i in range(n):
        if dist[i][i] < 0:
            has_negative_cycle = True
            break
            
    return dist, pred, has_negative_cycle


def reconstruct_path(pred, u, v):
    """Reconstructs shortest path from u to v using predecessor matrix."""
    if pred[u][v] is None:
        return []
    path = [v]
    curr = v
    while curr != u:
        curr = pred[u][curr]
        path.append(curr)
    path.reverse()
    return path


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 4 - FLOYD-WARSHALL (ALL-PAIRS SHORTEST PATH)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    INF = float("inf")
    vertex_names = ["1", "2", "3", "4"]
    n = len(vertex_names)
    
    # 4-vertex directed weighted graph
    # 1 -> 3 (weight -2)
    # 2 -> 1 (weight 4), 2 -> 3 (weight 3)
    # 3 -> 4 (weight 2)
    # 4 -> 2 (weight -1)
    cost_matrix = [
        [0,   INF, -2,  INF],
        [4,   0,    3,  INF],
        [INF, INF,  0,   2 ],
        [INF, -1,  INF,  0 ]
    ]
    
    print("Initial Cost Adjacency Matrix D^(0):")
    for i in range(n):
        row_str = "  [" + ", ".join(f"{cost_matrix[i][j]:4}" if cost_matrix[i][j] != INF else " INF" for j in range(n)) + "]"
        print(row_str)
        
    dist, pred, has_neg_cycle = floyd_warshall(cost_matrix, n)
    
    print("\nNegative Cycle Detected:", "YES" if has_neg_cycle else "NO")
    
    print("\n--- Final All-Pairs Shortest Distance Matrix D^(4) ---")
    header = "       " + " ".join(f"To {vertex_names[j]:<3}" for j in range(n))
    print(header)
    for i in range(n):
        row = f"From {vertex_names[i]}: "
        for j in range(n):
            val = f"{dist[i][j]:4d}" if dist[i][j] != INF else " INF"
            row += f"{val:6} "
        print(row)
        
    print("\n--- Sample Path Reconstructions ---")
    queries = [(1, 0), (1, 3), (3, 0), (0, 1)]
    for u, v in queries:
        p = reconstruct_path(pred, u, v)
        p_str = " -> ".join(vertex_names[node] for node in p)
        print(f"  Shortest Path {vertex_names[u]} -> {vertex_names[v]}: {p_str} (Distance: {dist[u][v]})")
        
    print("=" * 70)


if __name__ == "__main__":
    main()
