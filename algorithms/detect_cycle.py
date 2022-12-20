from collections import deque

class Graph:
    def __init__(self, vertices, directed):
        self.directed = directed
        self.vertices = vertices
        self.array = [deque() for _ in range(vertices)]

    def add_edge(self, source, destination):
        if (source < self.vertices and destination < self.vertices):
            self.array[source].appendleft(destination)
            if (self.directed is False):
                self.array[destination].appendleft(source)

def dfs(node, visited, stack, g):
    if stack[node]:
        return True

    if visited[node]:
        return False

    visited[node] = True
    stack[node] = True
    for nbr in g.array[node]:
        if dfs(nbr, visited, stack, g):
            return True

    stack[node] = False
    return False


def has_cycle(g: Graph) -> bool:
    visited = [False] * g.vertices
    stack = [False] * g.vertices

    for node in range(g.vertices):
        if not visited[node]:
            if dfs(node, visited, stack, g):
                return True
    return False


if __name__ == "__main__":
    g = Graph(4, True)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 2)
    print(has_cycle(g))
