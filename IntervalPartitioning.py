def interval_partitioning(intervals):
    sorted_intervals = sorted(intervals, key=lambda x:x[0])
    end_time = []

    for interval in sorted_intervals:
        start, end = interval
        isReusable = False #Traching if the resource is reusable
        for time in range(len(end_time)):
            if start >= end_time[time]:
                end_time[time] = end
                isReusable = True
                break

        if not isReusable:
                # Create a new resource
                end_time.append(end)
    # The number of resources needed is the length of end_times list
    return len(end_time)


intervals = [(30, 75), (0, 50), (60, 150), (0, 20), (50, 70), (80, 120)]
print("Minimum number of resources needed:", interval_partitioning(intervals))