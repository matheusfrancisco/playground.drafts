from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        if not grid or not grid[0]:
            return 0

        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r, c) not in visit:
                visit.add((r, c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)

        for c in range(1, cols-1):
            dfs(0, c)
            dfs(rows-1, c)

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    res += 1
        return res
