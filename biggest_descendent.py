def biggest_descendent(graph, root, value):
    result = {}
    
    def compute_biggest(node):
        if node in result:
            return result[node]
        
        max_value = value[node]
        
        for child in graph.neighbors(node):
            child_max = compute_biggest(child)
            max_value = max(max_value, child_max)
        
        result[node] = max_value
        return max_value
    
    compute_biggest(root)
    
    return result

