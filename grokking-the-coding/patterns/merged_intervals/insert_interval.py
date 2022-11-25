from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
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


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed

    # set the flag for closed/open
    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) \
            + "]" if self.closed else "(" + str(self.start) + ", " \
              + str(self.end) + ")"


def insert_interval(existing_intervals, new_interval):
    new_intervals = []
    for interval in existing_intervals:
        if interval.start > new_interval.end:
            print(interval)
            new_intervals.append(new_interval)
            new_interval = interval
        elif interval.end < new_interval.start:
            new_intervals.append(interval)
        else:
            new_interval = Interval(
                start=min(new_interval.start, interval.start),
                end=max(new_interval.end, interval.end)
            )

    new_intervals.append(new_interval)
    return new_intervals
