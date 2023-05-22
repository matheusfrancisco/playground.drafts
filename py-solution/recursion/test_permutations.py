"""
Write a function that takes in array of unique
integers and returns an array of all permutations
of those integers in no particular order.

If the input array is empty, the function should return
an ampty array

Time O(N!*N^2)
Space O(N!*N)
"""


def get_permutations(array):
    result = []
    if len(array) == 0:
        return array
    permutation(array, [], result)
    return result


def permutation(array, perm, result):
    if len(array) == 0:
        result.append(perm)
    else:
        for num in array:
            new_arr = [n for n in array if n != num]
            new_perm = perm + [num]
            permutation(new_arr, new_perm, result)


def test_get_permutations():
    arr = [1, 2, 3]
    expected = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    assert get_permutations(arr) == expected
    assert len(get_permutations(arr)) == len(expected)
    assert get_permutations([]) == []
