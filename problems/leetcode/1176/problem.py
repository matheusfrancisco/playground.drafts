from typing import List

class Solution:
    def diet_plan_performance(
            self,
            calories: List[int],
            k: int,
            lower: int,
            upper: int
    ) -> int:
        T = sum(calories[:k])
        pts = (T > upper) - (T < lower)
        for i in range(k, len(calories)):
            T += (calories[i] - calories[i - k])
            pts += ((T > upper) - (T < lower))
        return pts


assert 0 == Solution().diet_plan_performance([1, 2, 3, 4, 5], 1, 3, 3)
