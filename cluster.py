from collections import deque

def cluster(graph, weights, level):
    visited = set()
    clusters = []
    
    for node in graph.nodes:
        if node in visited:
            continue
        
        cluster_nodes = set()
        queue = deque([node])
        visited.add(node)
        cluster_nodes.add(node)
        
        while queue:
            current = queue.popleft()
            
            for neighbor in graph.neighbors(current):
                edge_weight = weights(current, neighbor)
                if edge_weight >= level:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        cluster_nodes.add(neighbor)
                        queue.append(neighbor)
        
        clusters.append(frozenset(cluster_nodes))
    
    return frozenset(clusters)

