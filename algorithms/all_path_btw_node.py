import collections


# O(E+V)
def find_all_paths_recursive(
        graph, source, destination, visited, path, paths
):
    visited.add(source)
    path.append(source)

    if source == destination:
        paths.append(list(path))
    else:
        for nbr in graph[source]:
            if nbr not in visited:
                find_all_paths_recursive(graph, nbr, destination, visited, path, paths)
    path.pop()
    visited.remove(source)


def find_all_path(g, source, destination):
    visited = set()
    paths = []
    path = []
    find_all_paths_recursive(g, source, destination, visited, path, paths)
    return paths


g = collections.defaultdict(list)
for u, v in [[0, 1], [0, 2], [1, 3], [1, 4], [3, 5], [4, 5], [2, 5]]:
    g[u].append(v)

print(find_all_path(g, 0, 5))



