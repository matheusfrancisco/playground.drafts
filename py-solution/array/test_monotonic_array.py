"""
  Write a function that takes in an array of integers and returns a 
  boolean representing whether the array is monotonic.

  An array is said to be monotonic if its elements, from left to right, are
  entirely non-incresing or entirely non-decreasing.
  
  Non-increasing elements aren't necessarily exclusively decreasing
  they simply don't increase. Similary non-decreasing elements aren't
  necessarily exclusively increasing they simply don't decrease

  note that empty arrays and arrays of one element are monotonic


  time O(n) where n is len of array
  space O(1)
"""


def test_monotonic():
    array = [-1, -5, -10, -1100, -1101, -1102, -9001]
    assert is_monotonic(array) is True
    assert is_monotonic_simple(array) is True


def is_monotonic(array):
    if len(array) <= 2:
        return True
    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue
        if breaks_direction(direction, array[i - 1], array[i]):
            return False
    return True


def is_monotonic_simple(array):
    is_non_decreasing = True
    is_non_increasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            is_non_decreasing = False
        if array[i] > array[i - 1]:
            is_non_increasing = False
    return is_non_decreasing or is_non_increasing


def breaks_direction(direction, previous, current):
    difference = current - previous
    if direction > 0:
        return difference < 0
    return difference > 0

