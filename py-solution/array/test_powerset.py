"""

Wirte a function that takes in an array of unique integers and returns its 
powerset the powerset P(x)  of a set X is the set of all subsets of X. 
For example, the powerset of [1, 2] is [[]], [1], [2], [1,2]
note that the sets in the powerset do not need to be in any particular order

"""

def powerset(arr):
    """
      Time: O(n*2^n)
      Space: O(n*2^n)
    """
    subsets = [[]]
    for ele in arr:
        for i in range(len(subsets)):
            current_subset = subsets[i]
            subsets.append(current_subset + [ele])
    return subsets


def powerset_rec(arr, idx=None):
    if len(arr) == 0:
        return [[]]
    if idx is None:
        idx = len(arr) - 1
    elif idx < 0:
        return [[]]
    ele = arr[idx]
    subsets = powerset_rec(arr, idx - 1)
    for i in range(len(subsets)):
        current_subset = subsets[i]
        subsets.append(current_subset + [ele])
    return subsets


def test_powerset():
    output = list(map(lambda x: set(x), powerset([1, 2, 3])))
    assert len(output) == 8
    assert set([]) in output
    assert set([1]) in output
    assert set([2]) in output
    assert set([1, 2]) in output
    assert set([3]) in output
    assert set([1, 3]) in output
    assert set([2, 3]) in output
    assert set([1, 2, 3]) in output
    output = list(map(lambda x: set(x), powerset_rec([1, 2, 3])))
    assert len(output) == 8
    assert set([]) in output
    assert set([1]) in output
    assert set([2]) in output
    assert set([1, 2]) in output
    assert set([3]) in output
    assert set([1, 3]) in output
    assert set([2, 3]) in output
    assert set([1, 2, 3]) in output
