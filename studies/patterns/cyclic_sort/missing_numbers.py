from typing import List


def find_disappeared_numbers(self, nums: List[int]) -> List[int]:
    i = 0
    while i < len(nums):
        x = nums[i]
        if x != (i+1) and x <= len(nums) and x != nums[x-1]:
            nums[i] = nums[x-1]
            nums[x-1] = x
        else:
            i += 1

    out = []
    for i, n in enumerate(nums):
        if i != n-1:
            out.append(i+1)
    return out
