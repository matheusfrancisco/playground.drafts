
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniques = {}
        for num in nums:
            if uniques.get(num, 0) != 0:
                v = uniques.get(num) + 1
                if v >= 2:
                    return True
                uniques[num] = v
            else:
                uniques[num] = 1
        return False
