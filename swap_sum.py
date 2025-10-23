def swap_sum(A, B):
    n = len(A)
    m = len(B)
    if n == 0 or m == 0:
        return None
    sum_A = sum(A)
    sum_B = sum(B)
    target = (10 - (sum_B - sum_A)) / 2
    i = 0
    j = 0
    while i < n and j < m:
        diff = A[i] - B[j]
        if diff == target:
            return (i, j)
        elif diff < target:
            i += 1
        else:
            j += 1
    return None
