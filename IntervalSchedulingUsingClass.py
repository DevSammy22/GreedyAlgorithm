class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def interval_scheduling(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda x:x.end)
        selected_intervals = []
        last_end_time = float('-inf')

        for interval in sorted_intervals:
            if interval.start >= last_end_time:
                selected_intervals.append(interval)
                last_end_time = interval.end

        return selected_intervals

intervals = [Interval(1, 3), Interval(2, 4), Interval(3, 5), Interval(0, 6), Interval(5, 7), Interval(8, 9)]
interval_instance = Interval(0,0)
selected_intervals = interval_instance.interval_scheduling(intervals) # Create an instance of Interval (not needed to use the class method, but if necessary)
print("The Selected Non-Overlapping Intervals: ")
for interval in selected_intervals:
    print(f"({interval.start}, {interval.end})")