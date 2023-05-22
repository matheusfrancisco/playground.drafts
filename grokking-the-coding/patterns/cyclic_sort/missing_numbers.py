from typing import List


def find_disappeared_number(nums: List[int]) -> List[int]:
    i, n = 0, len(nums)
    print(n)
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    for i in range(n):
        if i != nums[i]:
            return i
    return n


assert 7 == find_disappeared_number([8, 3, 5, 2, 4, 6, 0, 1])
