"""
Problem:
Maximum Profit in a Grid
A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).
Each cell contains a coin the robot can collect.
What is the maximum profit the robot can accumulate?
+---+---+---+---+
| S | 2 | 2 | 1 |
+---+---+---+---+
| 3 | 1 | 1 | 1 |
+---+---+---+---+
| 4 | 4 | 2 | E |
+---+---+---+---+

// Time complexity:
// Space complexity:
// f(i,j) = max(f(i-1, j), f(i, j-1)) + grid(i,j)
"""

def get_path(dp, i, j, path):
    if i == 0 and j == 0:
        path.append([i, j])
        return path
    elif i == 0:
        path = get_path(dp, i, j-1, path)
    elif j == 0:
        path = get_path(dp, i-1, j, path)
    else:
        if dp[i-1][j] > dp[i][j-1]:
            path = get_path(dp, i-1, j, path)
        else:
            path = get_path(dp, i, j-1, path)
    path.append([i, j])
    return path


def unique_max_profit(grid):
    m = len(grid)
    n = len(grid[0])

    dp = [[0] * n for i in range(m)]
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            dp[i][j] = grid[i][j]
            if i > 0 and j > 0:
                dp[i][j] += max(dp[i-1][j], dp[i][j-1])
            elif i > 0:
                dp[i][j] += dp[i-1][j]
            elif j > 0:
                dp[i][j] += dp[i][j-1]

    return get_path(dp, m-1, n-1, [])


assert unique_max_profit([[0, 2, 2, 1], [3, 1, 1, 1], [4, 4, 2, 0]]) == [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2], [2, 3]]
assert unique_max_profit([[0, 2, 2, 50], [3, 1, 1, 100], [4, 4, 2, 0]]) == [[0, 0], [0, 1], [0, 2], [0, 3], [1, 3], [2, 3]]
