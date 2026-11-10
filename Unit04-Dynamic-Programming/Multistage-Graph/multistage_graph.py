"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 04: Dynamic Programming
Experiment: Multistage Graph (Shortest Path via Dynamic Programming)

Problem Statement:
Find the minimum cost path from source node s (Stage 1) to destination node t (Stage k)
in a directed, weighted, multistage graph where edges only exist between consecutive stages.
Uses backward dynamic programming recurrence:
    cost(u) = min_{v in Adj(u)} { c(u, v) + cost(v) }
"""

def multistage_graph_shortest_path(n, stages, graph):
    """
    Computes shortest path in a multistage graph using backward DP.
    
    Parameters:
        n (int): Total number of vertices (0 to n-1).
        stages (dict): Mapping from node to stage number.
        graph (dict): graph[u] = list of tuples (v, weight)
        
    Returns:
        tuple: (min_cost, path)
    """
    INF = float("inf")
    cost = [INF] * n
    decision = [-1] * n
    
    # Destination node is n - 1 (in final stage k)
    cost[n - 1] = 0
    
    # Process vertices in reverse topological order (from n - 2 down to 0)
    for u in range(n - 2, -1, -1):
        if u in graph:
            for v, w in graph[u]:
                if w + cost[v] < cost[u]:
                    cost[u] = w + cost[v]
                    decision[u] = v
                    
    # Reconstruct optimal path from source (0) to destination (n - 1)
    path = [0]
    curr = 0
    while curr != n - 1 and decision[curr] != -1:
        curr = decision[curr]
        path.append(curr)
        
    return cost[0], path, cost, decision


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 4 - MULTISTAGE GRAPH (DYNAMIC PROGRAMMING)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    # Standard 4-stage, 8-vertex graph:
    # Stage 1: {0} (Source)
    # Stage 2: {1, 2, 3}
    # Stage 3: {4, 5, 6}
    # Stage 4: {7} (Sink)
    stages = {
        0: 1,
        1: 2, 2: 2, 3: 2,
        4: 3, 5: 3, 6: 3,
        7: 4
    }
    
    graph = {
        0: [(1, 1), (2, 2), (3, 5)],
        1: [(4, 4), (5, 11)],
        2: [(4, 9), (5, 5), (6, 16)],
        3: [(6, 2)],
        4: [(7, 18)],
        5: [(7, 13)],
        6: [(7, 2)]
    }
    
    node_names = [f"V{i}" for i in range(8)]
    
    print("Multistage Graph Structure:")
    for stage_num in range(1, 5):
        nodes_in_stage = [node_names[i] for i, s in stages.items() if s == stage_num]
        print(f"  Stage {stage_num}: {nodes_in_stage}")
        
    print("\nDirected Weighted Edges:")
    for u in sorted(graph.keys()):
        for v, w in graph[u]:
            print(f"  {node_names[u]} -> {node_names[v]} (Weight: {w})")
            
    min_cost, path, cost_table, dec_table = multistage_graph_shortest_path(8, stages, graph)
    
    print("\n--- Backward Dynamic Programming Evaluation ---")
    for u in range(7, -1, -1):
        next_hop = node_names[dec_table[u]] if dec_table[u] != -1 else "Sink"
        print(f"  Node {node_names[u]:<3} | Min Cost to Target: {cost_table[u]:<4} | Optimal Next Hop: {next_hop}")
        
    print("\n--- Optimal Shortest Path ---")
    path_str = " -> ".join(node_names[i] for i in path)
    print(f"  Path: {path_str}")
    print(f"  Total Path Weight: {min_cost}")
    print("=" * 70)


if __name__ == "__main__":
    main()
