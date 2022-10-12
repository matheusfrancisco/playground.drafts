from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def min_depth(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    if node.left is None:
        return min_depth(node.right) + 1
    if node.right is None:
        return min_depth(node.left) + 1
    return min(min_depth(node.left), min_depth(node.right)) + 1


def find_minimum_depth(root):
    return min_depth(root)


def find_minimum_depth_q(root):
    """
        The time complexity of the above algorithm is O(N)
        , where ‘N’ is the total number of nodes in the tree.
        This is due to the fact that we traverse each node once.
    """
    if root is None:
        return 0

    q = deque()
    q.append(root)
    _min = 0
    while q:
        _min += 1
        level_size = len(q)
        for _ in range(level_size):
            curr = q.popleft()

            if not curr.left and not curr.right:
                return _min
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth_q(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
