class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed
    # set the flag for closed/open

    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" \
            if self.closed else \
            "(" + str(self.start) + ", " + str(self.end) + ")"


def merge_intervals(v):
    # If the list is empty
    if not v:
        return None

    result = []

    # Adding pair in the result list
    result.append(Interval(v[0].start, v[0].end))

    for i in range(1, len(v)):
        last_added_interval = result[len(result) - 1]
        cur_start = v[i].start
        cur_end = v[i].end

        prev_end = last_added_interval.end
        # Overlapping condition
        if prev_end >= cur_start:
            last_added_interval.end = max(cur_end, prev_end)
        else:
            result.append(Interval(cur_start, cur_end))
    return result
