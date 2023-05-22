import collections


def bfs(g, source):
    q = collections.deque()
    q.append(source)
    visited = set()
    visited.add(source)

    while q:
        curr = q.popleft()

        for nbr in g[curr]:
            if nbr not in visited:
                q.append(nbr)
                visited.add(nbr)

    return visited

def dfs(g, source, visited=set()):
    visited.add(source)

    for nbr in g[source]:
        if nbr not in visited:
            dfs(g, nbr, visited)


g = collections.defaultdict(list)
# Directed graph
for u, v in [[1, 2], [2, 3], [2, 4], [2, 5]]:
    g[u].append(v)
print(bfs(g, 1))

g1 = collections.defaultdict(list)
for u, v in [(0, 1), (0, 2), (1, 3), (2, 3)]:
    g1[u].append(v)

print(bfs(g1, 0))
v = set()
dfs(g1, 0, visited=v)
print(v)

v = set()
dfs(g, 1, visited=v)
print(v)
