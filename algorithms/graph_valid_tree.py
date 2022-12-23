import collections
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for j in g[node]:
                if j == prev:
                    continue
                if not dfs(j, node):
                    return False

            return True
        return dfs(0, -1) and n == len(visit)
