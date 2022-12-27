from typing import List
"""
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.

https://leetcode.com/problems/find-eventual-safe-states/description/?envType=study-plan&id=graph-if :
"""
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}

        def dfs(i):
            if i in safe:
                return safe[i]

            safe[i] = False
            for nbr in graph[i]:
                if not dfs(nbr):
                    return safe[i]
            safe[i] = True
            return safe[i]
        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res
