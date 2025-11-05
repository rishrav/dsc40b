def mode(numbers):
    result = {}
    mode_elem = None
    mode_count = 0

    for num in numbers:
        if num not in result:
            result[num] = 1
        else:
            result[num]+=1
    
    for key, value in result.items():
        if value > mode_count:
            mode_elem = key
            mode_count = value
    
    return mode_elem
