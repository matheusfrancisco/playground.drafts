"""
/*
Problem:
Unique Paths with Obstales
A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).
Now consider if some obstacles are added to the grids.
How many unique paths would there be?
+---+---+---+---+
| S |   |   |   |
+---+---+---+---+
|   | 1 | 1 | 1 |
+---+---+---+---+
|   |   |   | E |
+---+---+---+---+
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
*/
"""

def unique(grid) -> int:
    m = len(grid)
    n = len(grid[0])

    dp = [[0] * n for i in range(m)]
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j] = 0
                continue
            if i > 0 and j > 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            elif i > 0:
                dp[i][j] = dp[i-1][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1]

    return dp[m-1][n-1]


assert unique([[0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0]]) == 3
assert unique([[0, 0]]) == 1
