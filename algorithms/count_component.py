

def count_component(g, n):
    visited = [False] * n
    count = 0

    def dfs(g, k):
        visited[k] = True
        for nbr in g[k]:
            if visited[nbr] is False:
                dfs(g, nbr)

    for p in range(n):
        if visited[p] is False:
            dfs(g, p)
            count += 1
    return count


if __name__ == '__main__':
    d = [[0, 1], [0, 2], [1, 2], [6, 7], [3, 4]]
    g = [[] for _ in range(8)]
    for u, v in d:
        g[u].append(v)
        g[v].append(u)
    c = count_component(g, 8)
    print(c)
