"""
You are given an unordered array consisting of 
consecutive integers [1, 2, 3, …, n] without any
duplicates. You are allowed to swap any two elements. 
You need to find the minimum number of swaps required 
to sort the array in ascending order.
"""


def error_minimum_swaps(arr):
    hash_map = {}
    for item in arr:
        hash_map[item] = False

    swaps = 0

    for index in range(len(arr)):
        real_index = index + 1
        if hash_map.get(real_index) is False:
            hash_map[real_index] is True
            if index == arr[index] - 1:
                continue
            else:
                current = arr[index]
                while hash_map[current] is False:
                    hash_map[current] = True
                    next_item = arr[current - 1]
                    current = next_item
                    swaps += 1
    return swaps - 1


def minimum_swaps(arr):
    """
      Time Complexity: O(n)
      Sapce complexity O(1)
    """
    swaps = 0
    n = len(arr)
    for idx in range(n):
        while arr[idx]-1 != idx:
            ele = arr[idx]
            arr[ele-1], arr[idx] = arr[idx], arr[ele-1]
            swaps += 1
    return swaps


def test_minimun_swaps():
    # assert minimum_swaps([7, 1, 3, 2, 4, 5, 6]) == 5
    # assert minimum_swaps([6, 5, 4, 3, 2, 1]) == 3
    assert minimum_swaps([6, 5, 4, 3, 2, 1]) == 3
