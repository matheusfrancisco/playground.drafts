
"""

Given an unsorted array containing numbers, find the
smallest missing positive number in it.

Note: Positive numbers start from ‘1’.
"""


def find_first_smallest_missing_positive(nums):
    i = 0
    n = len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return len(nums) + 1


assert 3 == find_first_smallest_missing_positive([-3, 1, 5, 4, 2])
