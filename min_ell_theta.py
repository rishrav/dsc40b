def learn_theta(data, colors):
    max_blue = float('-inf')
    min_red = float('inf')
    
    for i in range(len(data)):
        if colors[i] == 'blue':
            if data[i] > max_blue:
                max_blue = data[i]
        else:
            if data[i] < min_red:
                min_red = data[i]
    
    if max_blue == float('-inf') or min_red == float('inf'):
        return None
    
    return (max_blue + min_red) / 2.0


def compute_ell(data, colors, theta):
    red_le_theta = 0
    blue_gt_theta = 0
    
    for i in range(len(data)):
        if colors[i] == 'red' and data[i] <= theta:
            red_le_theta += 1
        elif colors[i] == 'blue' and data[i] > theta:
            blue_gt_theta += 1
    
    return float(red_le_theta + blue_gt_theta)


def minimize_ell(data, colors):
    unique_data = sorted(set(data))
    
    if len(unique_data) == 1:
        return unique_data[0]
    
    candidates = []
    for i in range(len(unique_data) - 1):
        candidates.append((unique_data[i] + unique_data[i + 1]) / 2.0)
    candidates.append(unique_data[0] - 1.0)
    candidates.append(unique_data[-1] + 1.0)
    
    min_loss = float('inf')
    best_theta = None
    
    for theta in candidates:
        loss = compute_ell(data, colors, theta)
        if loss < min_loss:
            min_loss = loss
            best_theta = theta
    
    return best_theta


def minimize_ell_sorted(data, colors):
    n = len(data)
    blue_gt_theta = 0
    
    for i in range(n):
        if colors[i] == 'blue':
            blue_gt_theta += 1
    
    red_le_theta = 0
    min_loss = float('inf')
    best_theta = None
    
    for alpha in range(n + 1):
        if alpha > 0:
            if colors[alpha - 1] == 'red':
                red_le_theta += 1
            else:
                blue_gt_theta -= 1
        
        if alpha == 0:
            theta = data[0] - 1.0
        elif alpha == n:
            theta = data[n - 1] + 1.0
        else:
            theta = (data[alpha - 1] + data[alpha]) / 2.0
        
        loss = red_le_theta + blue_gt_theta
        
        if loss < min_loss:
            min_loss = loss
            best_theta = theta
    
    return best_theta

