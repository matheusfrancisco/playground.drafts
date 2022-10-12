
"""
Given an array of sorted numbers, remove all duplicate number 
instances from it in-place, such that each element appears only once. 
The relative order of the elements should be kept the same and you 
should not use any extra space so that that the solution have a 
space complexity of O(1).

Pattern: Two Pointers
"""

def solution(arr):
    no_duplicated = 1
    i = 0

    while i < len(arr):
        n = arr[i]
        if n != arr[no_duplicated - 1]:
            arr[no_duplicated] = n
            no_duplicated += 1

        i += 1
    
    print(arr[0:no_duplicated])
    return no_duplicated


assert 4 == solution([2, 3, 3, 3, 6, 9, 9])
