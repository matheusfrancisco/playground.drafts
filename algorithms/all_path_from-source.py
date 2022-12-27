# Time O(2^N * N)
# Spac O(N)

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        out = []

        def dfs(cur_path, node):
            if node == len(graph) - 1:
                out.append(list(cur_path))

            for nbr in graph[node]:
                cur_path.append(nbr)
                dfs(cur_path, nbr)
                cur_path.pop()

        dfs([0], 0)
        return out
