def histogram(points, bins):
    n = len(points)
    k = len(bins)
    densities = [0.0] * k
    
    if n == 0:
        return densities
    
    point_idx = 0
    bin_idx = 0
    
    while point_idx < n and bin_idx < k:
        point = points[point_idx]
        bin_start, bin_end = bins[bin_idx]
        
        if point < bin_start:
            point_idx += 1
        elif bin_start < point <= bin_end:
            count = 0
            temp_idx = point_idx
            
            while temp_idx < n and bins[bin_idx][0] < points[temp_idx] <= bins[bin_idx][1]:
                count += 1
                temp_idx += 1
            
            bin_width = bin_end - bin_start
            density = count / (n * bin_width)
            densities[bin_idx] = density
            
            bin_idx += 1
            point_idx = temp_idx
        else:
            bin_idx += 1
    
    return densities
