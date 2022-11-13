""""
Statement#
Given an array of integers, nums, and an integer value, target, 
determine if there are any three integers in nums whose sum equals the target. 
Return TRUE if three such integers are found in the array. 
Otherwise, return FALSE.

""""

def find_sum_of_three(nums, target):
    nums.sort()

    for idx, n in enumerate(nums):
        left = idx + 1
        right = len(nums) - 1
        value = target - n
        while left < right:
            if nums[left] + nums[right] == value:
                return True
            elif nums[left] + nums[right] > value:
                right = right - 1
            elif nums[left] + nums[right] < value:
                left = left + 1
    return False
