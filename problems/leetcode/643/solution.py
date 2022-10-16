from typing import List

class Solution:
    def find_maxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        start = 0
        sum_ = 0
        for idx, n in enumerate(nums):
            sum_ += n
            if idx - start + 1 >= k:
                avg = sum_ / (idx - start + 1)
                max_avg = max_(max_avg, avg)
                sum_ -= nums[start]
                start += 1

        return max_avg

def max_(a, b):
    if a >= b:
        return a
    return b
