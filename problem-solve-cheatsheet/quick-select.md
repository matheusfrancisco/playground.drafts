## Quick Select


```python
## Average: O(n)
## Worst: O(n²)
## n = size(array)
def findKthLargest(self, nums: List[int], k: int) -> int:
    def qselect(nums: List[int], l: int, r: int, k: int) -> None:
        p = partition(nums, l, r)
        
        if p < k: 
            return qselect(nums, p + 1, r, k)
        if p > k: 
            return qselect(nums, l, p - 1, k)
        
        return nums[p]

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

    return qselect(nums, 0, len(nums) - 1, len(nums) - k)
```

Finds the kth smallest/largest element

Average: O(n)
Worst: O(n²)
```python
def quickSelect(list: List[int], l: int, r: int, k: int): -> int
    if l == r: 
        return list[l]
    # Select a pivot index p between left and right
    p = partition(list, l, r, p)
    if k == p: 
        return list[k]
    elif k < p: 
        r = p - 1
    else: 
        l = p + 1

```
Given an integer array, find the kth largest element. 

The easiest way? Sort the array. But that’s O(n log n).
Can we do better?
Sure! How about using a PriorityQueue? That’s O(n log k)!
Can we do even better? 
Use Quick Select; the algorithm’s linear on average.

Why O(n)? The algorithm recurs only for the part that contains the kth largest element. If we assume it recurs half the list each time, it processes n elements in the first recursive call, n/2 in the second, n/4 in the third, and so on, until there’s only 1 element remaining. 
Remember geometric series? 

1 + (1 / 2) + (1 / 4) + ... + (1 / n) = 2. Similarly, 

n + (n / 2) + (n / 4) + ... + 1 = 2n. 

Average:  O(n) 
Worst: O(n²) if the array is already sorted
