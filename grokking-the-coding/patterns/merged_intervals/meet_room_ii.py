import heapq
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


def find_sets(intervals_input):
    if len(intervals_input) < 0:
        return 0
    intervals = []

    for i in intervals_input:
        intervals.extend(i)

    intervals.sort(key=lambda x: x.start)
    free_rooms = []
    heapq.heappush(free_rooms, intervals[0].end)

    for interval in intervals[1:]:
        if free_rooms[0] <= interval.start:
            heapq.heappop(free_rooms)
        heapq.heappush(free_rooms, interval.end)

    # your code will replace this placeholder return statement
    return len(free_rooms)




def find_sets_1(intervals):
    if len(intervals) < 0:
        return 0

    intervals.sort(key=lambda x: x[0])

    free_rooms = []
    heapq.heappush(free_rooms, intervals[0][1])

    for interval in intervals[1:]:
        if free_rooms[0] <= interval[0]:
            heapq.heappop(free_rooms)
        heapq.heappush(free_rooms, interval[1])

    # your code will replace this placeholder return statement
    return len(free_rooms)

i = [[2, 8], [3, 4], [3, 9], [5, 11], [8, 20], [11, 15]]
