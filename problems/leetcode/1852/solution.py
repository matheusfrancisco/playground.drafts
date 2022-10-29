from collections import Counter
from typing import List

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums[:k])
        result = [len(c)]

        for i in range(k, len(nums)):
            c[nums[i]] += 1
            c[nums[i-k]] -= 1
            if c[nums[i-k]] == 0:
                del c[nums[i-k]]

            result.append(len(c))

        return result

