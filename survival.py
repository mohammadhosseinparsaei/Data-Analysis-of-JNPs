def median_survival_time(times, statuses):
    n = len(times)
    sorted_times = sorted(times)

    if n % 2 == 0:
        middle_idx1 = n // 2 - 1
        middle_idx2 = n // 2
        
        if statuses[middle_idx1] or statuses[middle_idx2] == 1:
            median_time = (sorted_times[middle_idx1] + sorted_times[middle_idx2]) / 2
        else:
            median_time = None
    else:
        middle_idx = n // 2
        
        if statuses[middle_idx] == 1:
            median_time = sorted_times[middle_idx]
        else:
            median_time = None
    
    return median_time