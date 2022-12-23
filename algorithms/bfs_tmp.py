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


def bfs(g, source):
    out = [source]
    q = deque([source])
    visited = set()
    visited.add(source)

    while q:
        node = q.popleft()
        for nbr in g.array[node]:
            if nbr not in visited:
                visited.add(nbr)
                out.append(nbr)
                q.append(nbr)
    return out


if __name__ == "__main__":
    g = Graph(4, True)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    print(bfs(g, 0))

