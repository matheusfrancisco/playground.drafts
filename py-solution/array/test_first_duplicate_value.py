"""
Given an arary of integers between 1 and n, inclusive, where n is the length
array, write a function that return the first integer that appear more than
once  (when the array is read from left to right)

if no integer apperars more than once, yout function should return -1
"""


def first_duplicate_value_best_space(array):
    """
      Where n is the length of the input array
      O(n) time
      O(1) space
    """
    for value in array:
        abs_value = abs(value)
        if array[abs_value - 1] < 0:
            return abs_value
        array[abs_value - 1] *= -1
    return -1


def first_duplicate_value_set(array):
    """
      Where n is the length of the input array
      O(n) time
      O(n) space
    """
    seen = set()
    for value in array:
        if value in seen:
            return value
        seen.add(value)
    return -1


def first_duplicate_value(array):
    """
      Where n is the length of the input array
      O(n) time
      O(n) space
    """
    occ = {}
    for idx, value in enumerate(array):
        if occ.get(value, None) is not None:
            return value
        else:
            occ[value] = idx
    return -1


def test_first_duplicate_value():
    input_array = [2, 1, 5, 2, 3, 3, 4]
    expected = 2
    assert first_duplicate_value(input_array) == expected
    assert first_duplicate_value_set(input_array) == expected
