




def insert(intervals, new_interval):

    new_intervals = []
    for interval in intervals:
        if interval[0] > new_interval[1]:
            new_intervals.append(new_interval)
            new_interval = interval
        elif interval[1] < new_interval[0]:
            new_intervals.append(interval)
        else: 
            new_interval = [
                min(new_interval[0], interval[0]), 
                max(new_interval[1], interval[1])
            ]
        
    return new_intervals + [new_interval]
            
        


print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
