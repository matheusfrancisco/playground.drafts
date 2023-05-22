from collections import deque


def find_order_iterative(n, prerequisites):
    sorted_order = []
    # if n is smaller than or equal to zero we will return the empty array
    if n <= 0:
        return sorted_order

    # Store the count of incoming prerequisites in a hashmap
    in_degree = {i: 0 for i in range(n)}
    # a. Initialize the graph
    graph = {i: [] for i in range(n)}  # adjacency list graph

    # b. Build the graph
    for prerequisite in prerequisites:
        parent, child = prerequisite[1], prerequisite[0]
        graph[parent].append(child)  # add the child to its parent's list
        in_degree[child] += 1  # increment child's in_degree

    # c. Find all sources i.e., all nodes with 0 in-degrees
    sources = deque()
    # traverse in in_degree using key
    for key in in_degree:
        # if in_degree[key] is 0 append the key in the deque sources
        if in_degree[key] == 0:
            sources.append(key)

    # d. For each source, add it to the sorted_order and subtract one from
    # all of its children's in-degrees. If a child's in-degree becomes zero,
    # add it to the sources queue
    while sources:
        # pop an element from the start of the sources and store
        # the element in vertex
        vertex = sources.popleft()
        # append the vertex at the end of the sorted_order
        sorted_order.append(vertex)
        # traverse in graph[vertex] using child
        # get the node's children to decrement
        # their in-degrees
        for child in graph[vertex]:
            in_degree[child] -= 1
            # if in_degree[child] is 0 append the child in the deque sources
            if in_degree[child] == 0:
                sources.append(child)

    # topological sort is not possible as the graph has a cycle
    if len(sorted_order) != n:
        return []

    return sorted_order


def find_order(n, prerequisites):
    prereq = {c: [] for c in range(n)}
    for crs, pre in prerequisites:
        prereq[crs].append(pre)

    out = []
    visited = set()
    cycle = set()

    def dfs(node):
        if node in cycle:
            return False
        if node in visited:
            return True

        cycle.add(node)
        for nbr in prereq[node]:
            if dfs(nbr) is False:
                return False
        cycle.remove(node)
        visited.add(node)
        out.append(node)
        return True

    for node in range(n):
        if dfs(node) is False:
            return []

    return out


# Driver code
def main():
    n = [4, 5, 0, 4, 7]
    prerequisites = [
        [[1, 0], [2, 0], [3, 1], [3, 2]],
        [[1, 0], [2, 0], [3, 1]],
        [[1, 0]], [[1, 0], [2, 0], [3, 1], [3, 2]],
        [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]]
    for i in range(len(n)):
        print(i + 1, ".\tPrerequisites: ", prerequisites[i], sep="")
        print("\tTotal number of courses, n:", n[i])
        print("\tValid courses order:", find_order_iterative(n[i], prerequisites[i]))
        print("-"*100)


if __name__ == '__main__':
    main()
