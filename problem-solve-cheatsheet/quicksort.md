### Quick sort
```python
def qsort(nums: List[int]) -> None:
    def qsort_helper(nums: List[int], l: int, r: int) -> None:
        if l >= r: return

        p = partition(nums, l, r)
        qsort_helper(nums, l, p - 1)
        qsort_helper(nums, p + 1, r)

    def partition(nums: List[int], l: int, r: int) -> int:
        pivot, p = nums[r], r

        i = l
        while i < p:
            if nums[i] > pivot: 
                nums[i], nums[p - 1] = nums[p - 1], nums[i]
                nums[p], nums[p - 1] = nums[p - 1], nums[p]
                i -= 1
                p -= 1
            i += 1

        return p
        
    qsort_helper(nums, 0, len(nums) - 1)
    
```
