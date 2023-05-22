import collections

def dfs(g, source, visited):
    q = collections.deque()
    out = []
    q.append(source)
    while q:
        c = q.pop()
        if c not in visited:
            out.append(c)
            visited.add(c)
        for nbr in g[c]:
            if nbr not in visited:
                q.append(nbr)
    return out


def connect_comp(g):
    visited = set()
    result = []

    for node in range(len(g) + 1):
        if node not in visited:
            result.append(dfs(g, node, visited))
    return result


g = collections.defaultdict(list)

for u, v in [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6]]:
    g[u].append(v)

print(connect_comp(g))
