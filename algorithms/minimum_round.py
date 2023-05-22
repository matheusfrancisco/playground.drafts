
import collections

def minimumRounds(tasks):
    freq = {}
    for t in tasks:
        if t not in freq:
            freq[t] = 0
        freq[t] += 1
    ans = 0

    for t in freq:
        count = freq[t]
        if count == 1:
            return -1
        if count % 3 == 0:
            ans += count // 3
        else:
            ans += count // 3 + 1
    return ans
