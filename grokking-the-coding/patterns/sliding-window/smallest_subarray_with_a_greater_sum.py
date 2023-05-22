

"""
Given an array of positive integers and a number ‘S,’ find the length of the
smallest contiguous subarray whose sum is greater than or equal to ‘S’.
Return 0 if no such subarray exists.



solution 
First, we will add-up elements from the beginning of the array until their sum becomes greater than or equal to ‘S.’
These elements will constitute our sliding window. We are asked to find the smallest such window having a sum greater than or equal to ‘S.’ We will remember the length of this window as the smallest window so far.

Time complexity: O(N + N)
Space: O(1)

"""

def solution(arr, s):
    start, sw = 0,0
    mlen = float("inf")

    for end in range(len(arr)):
        sw += arr[end]
        while sw >= s:
            mlen = min(end - start + 1, mlen)
            sw -= arr[start]
            start += 1
            
    if mlen == float("inf"):
        return 0
    return mlen


assert 2 == solution([2, 1, 5, 2, 3, 2], 7)
assert 1 == solution([2, 1, 5, 2, 8], 7)
