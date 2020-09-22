

def max_subset_sum(array):
    """
      O(n): time
      O(n): space
    """
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    max_sum = array[:]
    max_sum[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        max_sum[i] = max(max_sum[i-1], max_sum[i-2] + array[i])
    return max_sum[-1]


def test_max_subset_sum_no_adjacent():
    assert 330 == max_subset_sum([75, 105, 120, 75, 90, 135])
