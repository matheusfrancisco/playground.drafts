from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        set_ = set()
        for idx, n in enumerate(nums):
            if n in set_:
                return True
            set_.add(n)
            if len(set_) > k:
                set_.remove(nums[idx-k])

        return False


def contains_nearby_duplicate(self, nums: List[int], k: int) -> bool:
    # To store the (value,index) pair of element of nums
    index_dict = {}
    # Loop through the elements of nums
    # and check if element is present in dict
    for i in range(len(nums)):

        # If not present, then add (element,index)
        # as key-val pair in index_dict
        if nums[i] not in index_dict:
            index_dict[nums[i]] = i

        # If the element is present in the dict,
        # then the current one is a duplicate
        else:

            # Return true if the diff between the
            # current and stored indices is less than k
            if i - index_dict[nums[i]] <= k:
                return True

            # Otherwise update stored index to latest index of the element
            else:
                index_dict[nums[i]] = i

    # Return false if the duplicate and less than k conditions are not met
    return False


assert Solution().containsNearbyDuplicate([1, 2, 3, 1], 3) is True
assert Solution().containsNearbyDuplicate([1, 0, 1, 1], 1) is True
assert Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False
