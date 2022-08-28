def two_sum(self, nums: List[int], target: int) -> List[int]:
    d = {}
    for i, n in enumerate(nums):
        if target - n in d:
            return [d.get(target-n), i]
        d[n] = i




