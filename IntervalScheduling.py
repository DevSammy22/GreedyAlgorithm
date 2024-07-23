def interval_scheduling(intervals):
    sorted_intervals = sorted(intervals, key=lambda x:x[1])
    selected_intervals = []
    last_end_time = float('-inf')

    for interval in sorted_intervals:
        start, end = interval
        if start >= last_end_time:
            selected_intervals.append(interval)
            last_end_time = end

    return selected_intervals
'''
eventInterval = [(1, 3), (2, 5), (4, 6), (6, 8), (5, 7)]
selectedIntervals = interval_scheduling(eventInterval)
print("The Selected Non-Overlapping Intervals: ", selectedIntervals)
'''

eventInterval = [(1, 3), (2, 5), (4, 6), (6, 8), (5, 7)]
selectedIntervals = interval_scheduling(eventInterval)
print("The Selected Non-Overlapping Intervals: ")
for interval in selectedIntervals:
    print(f"({interval[0]}, {interval[1]})")



