def knn_distance(arr, q, k):
    distances = [(abs(x - q), x) for x in arr]
    
    distances.sort(key=lambda x: x[0])
    
    kth_distance, kth_point = distances[k - 1]
    return (kth_distance, kth_point)
