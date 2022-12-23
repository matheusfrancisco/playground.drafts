from collections import deque

def find_compilation_order(dependencies):
    order = []
    graph = {}
    in_degree = {}
    for x in dependencies:
        parent, child = x[1], x[0]
        graph[parent], graph[child] = [], []
        in_degree[parent], in_degree[child] = 0, 0

    if len(graph) <= 0:
        return order

    for dep in dependencies:
        parent, child = dep[1], dep[0]
        graph[parent].append(child)
        in_degree[child] += 1

    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    while sources:
        vertx = sources.popleft()
        order.append(vertx)
        for child in graph[vertx]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    if len(order) != len(graph):
        return []

    return order


def main():
    dependencies = [[['B', 'A'], ['C', 'A'], ['D', 'C'], ['E', 'D'], ['E', 'B']],
                    [['B', 'A'], ['C', 'A'], ['D', 'B'], ['E', 'B'], ['E', 'D'], ['E', 'C'], ['F', 'D'], ['F', 'E'], ['F', 'C']],
                    [['A', 'B'], ['B', 'A']],
                    [['B', 'C'], ['C', 'A'], ['A', 'F']],
                    [['C', 'C']]]
    for i in range(len(dependencies)):
        print(find_compilation_order(dependencies[i]))


if __name__ == "__main__":
    main()
