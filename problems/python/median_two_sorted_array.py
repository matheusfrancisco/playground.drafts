def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    nums = nums1 + nums2
    n = sorted(nums)
    n_len = len(n)
    if n_len % 2 == 1:
        return n[int(n_len/2)]
    else:
        return (n[math.floor(n_len/2)] + n[math.floor(n_len/2) -1]) /2
