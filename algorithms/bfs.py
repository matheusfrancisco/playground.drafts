from collections import deque


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []

        for i in range(vertices):
            self.array.append(deque())

    # Function to add an edge from source to destination
    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            self.array[source].appendleft(destination)
            # Uncomment the following line for undirected graph 
            # self.array[destination].insert_at_head(source)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temps = self.array[i]
            for temp in temps:
                print("[", temp, end=" ] -> ")
            print("None")


def bfs_traversal_helper(g, source, visited):
    result = ""
    queue = deque()
    queue.append(source)
    visited[source] = True # Mark as visited

    while queue:
        current_node = queue.popleft()
        result += str(current_node)
        temps = g.array[current_node]
        for temp in temps:
            if not visited[temp]:
                queue.append(temp)
                visited[temp] = True  # Visit the current Node
    return result, visited


def bfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return result
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)

    result, visited = bfs_traversal_helper(g, source, visited)
    for i in range(num_of_vertices):
        if not visited[i]:
            result_new, visited = bfs_traversal_helper(g, i, visited)
            result += result_new
    return result



if __name__ == "__main__" :
    g = Graph(4)
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        print(bfs_traversal(g, 0))
