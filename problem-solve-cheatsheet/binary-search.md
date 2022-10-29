## Binary Search

O(log n)
n = size(array)

```python 
# If the target exists, returns its leftmost index.
# Else, returns the index of where it should be.
def binarySearch(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    while l < r :
        m = (l + r) // 2;
        if nums[m] < target:
            l = m + 1;
        else: 
            r = m;
    return l;
```

## Leftmost Binary Search

If the element exists, finds its leftmost index
If it doesn’t exists, locate the index of where it should be

Given arr = \[ 1, 2, 3, 3, 3, 6, 9\], this binary search implementation can: 

·  check whether the target exists. 
    arr \[ binarySearch(arr, 2) \] == 2

·  find the leftmost index of the target if it exists. 
    binarySearch(arr, 3) = 2
    binarySearch(arr, 9) = 6

·  find the index of where the target should be if it doesn't exist. 
    binarySearch(arr, 4) = 5
    binarySearch(arr, -5) = 0
    binarySearch(arr, 100) = 7

