import collections

"""
O(V + E)
"""
def transpose(g):
    new_g = collections.defaultdict(list)
    for source in range(len(g)):
        for nbr in g[source]:
            new_g[nbr].append(source)

    return new_g


g = collections.defaultdict(list)

for u, v in [[0, 1], [0, 2], [1, 3], [1, 4]]:
    g[u].append(v)

print(g)
print(transpose(g))
