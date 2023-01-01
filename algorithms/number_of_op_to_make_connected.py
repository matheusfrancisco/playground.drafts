import collections
from typing import List

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        g = collections.defaultdict(list)
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)

        visit = set()
        disconnect = 0

        def dfs(node):
            q = collections.deque([node])
            while q:
                c = q.popleft()

                if c in visit:
                    continue
                visit.add(c)
                for nbr in g[c]:
                    if nbr not in visit:
                        q.append(nbr)

        for i in range(n):
            if i not in visit:
                disconnect += 1
                dfs(i)
        return disconnect - 1
