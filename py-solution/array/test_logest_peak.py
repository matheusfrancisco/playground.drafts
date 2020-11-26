"""
Write a function that takes in an array of
integers and return the length of the longest peak

peak is defined as adjacent integers in the array
that are strictly increasing until they reach a tip
(the highest value in the peak), at which point they
become strictly decreasing, at least three integers are
reuired to form a peak

for example the 4, 6, 1 is a peak

Time: O(n)
Space: O(1)
"""


def logest_peak(array):
    longest_peak_length = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue
        left_idx = i - 2
        while left_idx >= 0 and array[left_idx] < array[left_idx + 1]:
            left_idx -= 1
        right_idx = i + 2
        while right_idx < len(array) and array[right_idx] < array[right_idx - 1]: # noqa
            right_idx += 1

        current_peak_length = right_idx - left_idx - 1
        longest_peak_length = max(longest_peak_length, current_peak_length)
        i = right_idx
    return longest_peak_length


def test_logest_peak():
    array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    expected = 6
    assert logest_peak(array) == expected
