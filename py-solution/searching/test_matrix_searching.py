
"""
Searching in sorted matrix
you're given a two-dimensional array
of distinct integers an a target integer. Each row
in the matrix is sorted, and each column is also sorted;

the matrix doesn't necessarily have the same height and width

write a function that returns an array of the row and
column indices of the target integer if it's contained
in the matrix, otherwise [-1 -'']
"""


def search_in_sorted_matrix(matrix, target):
    """
      Time O(n + m)
      Space O(1)
    """
    if len(matrix) == 0 or matrix == []:
        return [-1, -1]

    row = 0
    col = len(matrix[0]) - 1
    while col >= 0 and row < len(matrix):
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]
    return [-1, -1]


def test_search_matrix():
    matrix = [
           [1, 4, 7, 12, 15, 1000],
           [2, 5, 19, 31, 32, 1001],
           [3, 8, 24, 33, 35, 1002],
           [40, 41, 42, 44, 45, 1003],
           [99, 100, 103, 106, 128, 1004],
    ]
    result = search_in_sorted_matrix(matrix, 44)
    assert result == [3, 3]
