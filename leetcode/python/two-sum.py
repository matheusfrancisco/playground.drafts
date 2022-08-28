
def two_sum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        if target - n in d:
            return [d.get(target-n), i]
        d[n] = i

print(two_sum([2,7,11,15], 9))
