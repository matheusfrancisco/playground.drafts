from collections import deque
"""

There are four possible cases:Empty jug1,empty jug2,poor jug1 to jug2,poor jug2 to jug1.Add each of them to queue.If you encounter the same value again,do not add it to queue.If you encounter desired value,return True
I got TLE first but accepted after it with the same code.Not very fast but another point of view

"""

class Solution:
    def canMeasureWater(self, jug1: int, jug2: int, target: int) -> bool:
        seen = set()
        queue = deque([(jug1, jug2)])
        while queue:
            x = queue.popleft()
            c1, c2 = x[0], x[1]
            candidates = [(0, c2), (c1, 0), (min(jug1, c1+c2), max(0, c2-c1)), (max(0, c1-c2), min(jug2, c1+c2))]
            for candidate in candidates:
                if target in [candidate[0], candidate[1], candidate[0]+candidate[1]]:
                    return True
                if candidate not in seen:
                    queue.append(candidate)
                    seen.add(candidate)
        return False
