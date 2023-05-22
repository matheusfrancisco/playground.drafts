"""
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Solution: 
We can utilize the sum of the previous subarray.
For this consider each subarray as a Sliding Window of size
k to calculate the sum of the next subarray.


Time complexity O(N)
Space O(1)

"""

def solution(arr, k):

    win_start, win_sum = 0, 0
    out = 0

    for win_end in range(len(arr)):
        win_sum += arr[win_end]

        if win_end >= k - 1:
            out = max(out, win_sum)
            win_sum -= arr[win_start]
            win_start += 1

    return out


def max_sub_array_of_size_k(k, arr):
    start = 0
    sum_, max_ = 0, 0
    for end, n in enumerate(arr):
        sum_ += n

        if end - start + 1 >= k:
            max_ = max(sum_, max_)
            sum_ -= arr[start]
            start += 1

    return max_




assert 9 == solution([2, 1, 5, 1, 3, 2], 3)
assert 9 == max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])
