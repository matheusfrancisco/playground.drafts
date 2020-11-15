"""
Write a function that takes in an n x m two dimensional array
be square-shaped when n == m and return one dimensional array of all the
array elemetns in spiral order

Spiral order start at the top left corner of the two dimensional array goes to
the right and proceeds in a spiral pattern all the way until every element has 
been visited

Time O(n) ||Space O(n)
"""


def spiral_traverse(array):
    start_row, end_row = 0,  len(array) - 1
    start_coll, end_coll = 0, len(array[0]) - 1
    result = []
    while start_coll <= end_coll and start_row <= end_row:
        for col in range(start_coll, end_coll + 1):
            result.append(array[start_row][col])
        for row in range(start_row + 1, end_row + 1):
            result.append(array[row][end_coll])
        for col in reversed(range(start_coll, end_coll)):
            if start_row == end_row:
                break
            result.append(array[end_row][col])
        for row in reversed(range(start_row + 1, end_row)):
            if start_coll == end_coll:
                break
            result.append(array[row][start_coll])
        start_row += 1
        end_row -= 1
        start_coll += 1
        end_coll -= 1
    return result


def test_spiral_traverse():
    matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] 
    assert spiral_traverse(matrix) == expected
