from typing import List


def min_value(arr: List):
    min_v = float("inf")
    for num in arr:
        min_v = min(num, min_v)

    return min_v


def min_value_sort(arr: List):
    if len(arr) <= 0:
        return None
    arr.sort()
    return arr[0]
