from collections import deque

class Graph:
    def __init__(self, vertices, directed):
        self.directed = directed
        self.vertices = vertices
        self.array = [[] for _ in range(vertices)]

    def add_edge(self, source, destination):
        if (source < self.vertices and destination < self.vertices):
            self.array[source].append(destination)
            if (self.directed is False):
                self.array[destination].appendleft(source)


def topological_sort(g):
    output = []
    visit, cycle = set(), set()

    def dfs(node):
        if node in cycle:
            return False
        if node in visit:
            return True

        cycle.add(node)
        for nbr in g.array[node]:
            if dfs(nbr) is False:
                return False

        cycle.remove(node)
        visit.add(node)
        output.append(node)
        return True

    for node in range(g.vertices):
        if dfs(node) is False:
            return []
    return output


if __name__ == "__main__":
    g = Graph(6, True)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    print(topological_sort(g))
