from collections import deque


class Graph:
    def __init__(self, vertices, directed):
        # Total number of vertices
        self.directed = directed
        self.vertices = vertices
        # definining a list which can hold multiple LinkedLists
        # equal to the number of vertices in the graph
        # Creating a new Linked List for each vertex/index of the list
        # TODO change this to LinkedLists implementation
        self.array = [deque() for _ in range(vertices)]

    def add_edge(self, source, destination):
        if (source < self.vertices and destination < self.vertices):
            self.array[source].appendleft(destination)
            if (self.directed is False):
                self.array[destination].appendleft(source)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i]
            for t in temp:
                print("[", t, end=" ] -> ")
            print("None")


def bfs_tranversal_not_opt(g: Graph, source: int):
    result = []
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return result

    visited = []
    for i in range(num_of_vertices):
        visited.append(False)

    q = deque()
    q.append(source)

    while len(q) > 0:
        current = q.pop()
        if not visited[current]:
            result.append(current)
        nodes = g.array[current]
        for node in nodes:
            if not visited[node]:
                result.append(node)
                q.append(node)
                visited[node] = True

    return result


if __name__ == "__main__":
    g = Graph(4, True)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.print_graph()

    print(bfs_tranversal_not_opt(g, 0))


# eval (buf): ...sco/m/data-structures-playground/ds-python/graph.py
# (out) >>Adjacency List of Directed Graph<<
# (out) | 0 | => [ 1 ] -> [ 2 ] -> None
# (out) | 1 | => [ 3 ] -> None
# (out) | 2 | => [ 3 ] -> None
# (out) | 3 | => None
